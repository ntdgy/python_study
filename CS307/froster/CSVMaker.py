from typing import Any, Dict, List, Optional, Tuple
import json
import io
import re


def clean_csv_value(value: Optional[Any]) -> str:
    if value is None:
        return r'\N'
    return str(value).replace('\n', '\\n')


num = 0
courses: Dict[str, List] = {}
accessed: List[str] = []


def get_course_id(course_name: str) -> Optional[str]:
    if course_name not in courses:
        # print("Mismatch: "prerequisite": "(" + course_name)
        return None
    accessed.append(course_name)
    tmp = courses[course_name]
    if tmp[0] < len(tmp[1]):
        tmp[0] += 1
        return tmp[1][tmp[0] - 1]
    else:
        return None


course_list = []


def replace(s: re.Match):
    global num, course_list, courses
    if s.group(0) == "or" or s.group(0) == "and":
        return s.group(0)
    else:
        course_id = get_course_id(s.group(0))
        num += 1
        if course_id != None:
            course_list.append(course_id)
            return "Y" + course_id
        else:
            course_list.append("X" + str(num))
            return "YX" + str(num)


group_id = 1
groups = []


def get_all_truth_tables(s: str) -> List[Tuple[int, str]]:
    global group_id, course_list, num
    res = []
    s = s.replace("或者", "or")
    s = s.replace("并且", "and")
    pattern = re.compile(r"[\u4E00-\u9FA5A-Za-z0-9_\-Ⅱ（）：]+")
    s = pattern.sub(replace, s)
    succeed = []
    for i in range(0, 2**num):
        flag = False
        for n in succeed:
            if n & i == n:
                flag = True
                break
        if flag:
            continue
        bin_str = bin(i).replace("0b", "")
        bin_str = (num - len(bin_str)) * "0" + bin_str
        assign_str = ""
        for j in range(0, num):
            if j < len(bin_str):
                assign_str += ("Y" +
                               course_list[j] + " = " + bin_str[j] + "\n")
            else:
                assign_str += ("Y" + course_list[j] + " = " + "0" + "\n")
        exec(assign_str, globals())
        exec("test=" + s, globals())
        if test:
            succeed.append(i)
            cnt = 0
            for j in range(0, num):
                if j < len(bin_str) and bin_str[j] == "1" and "X" not in course_list[j]:
                    res.append((group_id, course_list[j]))
                    cnt += 1
            if cnt > 0:
                groups.append((group_id, cnt))
                group_id += 1
    for course in accessed:
        courses[course][0] = 0
    course_list = []
    num = 0
    return res


def make_course_csv(path: str) -> Tuple[io.StringIO, io.StringIO, io.StringIO, io.StringIO, io.StringIO, io.StringIO]:
    global courses
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

        course_res = io.StringIO()
        department_res = io.StringIO()
        class_res = io.StringIO()
        prerequisite_group_content = io.StringIO()
        prerequisite_truth_table = io.StringIO()

        departments = {}
        prerequisite_list: Dict[str, str] = {}
        classes_unique = []

        course_serial = 1
        department_serial = 1
        class_serial = 1
        prerequisites_serial = 1

        for course in data:

            # assign course dict
            if course["courseName"] not in courses:
                courses[course["courseName"]] = [0, []]
            courses[course["courseName"]][1].append(str(course_serial))

            # add dept
            try:
                department_id = departments[course["courseDept"]]
            except KeyError:
                department_res.write('|'.join(map(clean_csv_value, (
                    department_serial,
                    course["courseDept"]
                ))) + '\n')
                departments[course["courseDept"]] = department_serial
                department_id = department_serial
                department_serial += 1

            # add prereq to list
            if course["prerequisite"]:
                prerequisite_list[str(course_serial)] = course["prerequisite"]

            # add course
            course_res.write('|'.join(map(clean_csv_value, (
                course["className"],
                course["courseCredit"],
                course["courseHour"],
                course["courseId"],
                course["courseName"],
                course["totalCapacity"],
                department_id,
                course_serial,
                course["prerequisite"]
            ))) + '\n')

            # add class
            for cls in course["classList"]:
                s = str(cls["classTime"]) + cls["location"] + "{" + ", ".join(cls["weekList"]) + "}" + str(cls["weekday"])
                if s not in classes_unique:
                    classes_unique.append(s)
                    class_res.write('|'.join(map(clean_csv_value, (
                        class_serial,
                        cls["classTime"],
                        cls["location"],
                        "{" + ", ".join(cls["weekList"]) + "}",
                        cls["weekday"],
                        course_serial
                    ))) + '\n')
                    class_serial += 1

            course_serial += 1

        # parse prerrequisites
        for course_id in prerequisite_list.keys():
            truth_tables = get_all_truth_tables(prerequisite_list[course_id])
            for line in truth_tables:
                prerequisite_truth_table.write('|'.join(map(clean_csv_value, (
                    prerequisites_serial,
                    course_id,
                    line[0],
                    line[1]
                ))) + '\n')
                prerequisites_serial += 1

        for group in groups:
            prerequisite_group_content.write('|'.join(map(clean_csv_value, (
                group[0],
                group[1]
            ))) + '\n')

        # reset csv
        department_res.seek(0)
        course_res.seek(0)
        class_res.seek(0)
        prerequisite_group_content.seek(0)
        prerequisite_truth_table.seek(0)
    return department_res, course_res, class_res, prerequisite_truth_table, prerequisite_group_content

if __name__ == "__main__":

    s = "(材料力学 或者 材料力学 或者 材料力学) 并且 (CAD与工程制图 或者 (工程制图 并且 CAD技术Ⅱ)) 并且 (理论力学I 或者 理论力学I 或者 理论力学I-B)"
    print(get_all_truth_tables(s))