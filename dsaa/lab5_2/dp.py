import cyaron
import random


print(__import__("os").listdir("."))
for i in range(1, 100):
    N = random.randint(1, 500)
    M = random.randint(N, 1000)
    P = random.randint(1, 10)
    p = []
    for _ in range(P):
        p.append([random.randint(1, 10), random.randint(1, 10)])
    graph = cyaron.Graph.UDAG(N, M, self_loop=True, repeated_edges=True, weight_limit=10)
    test_data = cyaron.IO(file_prefix="apb", data_id=1)

    test_data.input_writeln(N, M)
    test_data.input_writeln(graph)
    test_data.input_writeln(P)
    for j in p:
        test_data.input_writeln(j[0], j[1])


    print(cyaron.Compare.program("lab5_2.exe", input=test_data,  std_program="frank.exe"))
