from os import read
from typing import Dict, Iterator, Any, Optional
from StringIteratorIO import StringIteratorIO
import psycopg2
import time
from psycopg2._psycopg import connection
from psycopg2.extras import execute_batch
from CSVMaker import make_course_csv, clean_csv_value
import csv
from collections import deque


def insertCourse(conn: connection, path: str) -> None:
    with conn.cursor() as cur:
        cur: psycopg2.cursor

        department_csv, course_csv, class_csv, prerequisite_truth_table_csv, prerequisite_group_content_csv = make_course_csv(
            path)
        cur.copy_from(department_csv, "department", sep='|')
        cur.copy_from(course_csv, "course", sep='|')
        cur.copy_from(class_csv, "class", sep='|')
        cur.copy_from(prerequisite_group_content_csv,
                      "prerequisite_group_count", sep='|')
        cur.copy_from(prerequisite_truth_table_csv,
                      "prerequisite_truth_table", sep='|')
        conn.commit()


def addStudents(conn: connection, path: str):
    colleges = {"阿兹卡班": 1, "斯莱特林": 2, "赫奇帕奇": 3, "拉文克劳": 4, "格兰芬多": 5}
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        student_csv = StringIteratorIO((
            '|'.join(map(clean_csv_value, (
                stu[3],
                stu[0],
                stu[1],
                colleges[stu[2][0:4]]
            ))) + '\n'
            for stu in reader
        ))
        with conn.cursor() as cur:
            cur.copy_from(student_csv, "student", sep='|')
            conn.commit()


def selectCourse(conn: connection, path: str):
    with conn.cursor() as cur:
        cur: psycopg2.cursor
        cur.execute(
            ''' PREPARE stmt AS 
            with cid(cid_id, pre_str) as (
                select course.id, course.prerequisite_str
                from course
                where "courseId" = $2
            )
            insert into course_selection(student_id, course_id)
            select $1, cid.cid_id from cid
            where
                cid.pre_str IS NULL
                or (
                select count(*) from (
                select group_id, count(*) over (partition by group_id) as cnt
                from prerequisite_truth_table
                inner join cid
                on prerequisite_truth_table.course_id = cid.cid_id
                inner join course_selection
                on real_prerequisite_course_id = course_selection.course_id
                and student_id = $1
                group by group_id, cid.cid_id
            ) tmp inner join prerequisite_group_count
                on prerequisite_group_count.group_id = tmp.group_id
                and prerequisite_group_count.count = tmp.cnt
            ) != 0;''')
        l = []
        counter = 0
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for stu in reader:
                counter += 1
                if counter > 1000:
                    break
                courses = stu[4:]
                for course in courses:
                    l.append([stu[3], course])
        execute_batch(cur, sql="EXECUTE stmt (%s, %s)", argslist=l)
        cur.execute("DEALLOCATE stmt")
        conn.commit()


if __name__ == "__main__":
    conn = psycopg2.connect(database="project1",
                            user="froster", password="198101602")
    start = time.time()
    try:
        # addStudents(conn, "../data/select_course.csv")
        insertCourse(conn, "../data/course_info.json")
        # selectCourse(conn, "../data/select_course.csv")
    finally:
        print("cost: ", (time.time() - start) * 1000, "ms")
        conn.close()