import time
def code_1():
    for n in range(100, 1001, 100):
        start_time = time.clock()
        result = 0
        for i in range(100000):
            result = result ^ i 
        end_time = time.clock()
        time_taken = end_time - start_time
        print("Algorithm 1: n {0} is {1}sec".format(n, time_taken))

def code_2():
    for n in range(100, 1001, 100):
        start_time = time.clock()
        result = 0
        for i in range(n):
            result = result ^ i 
        end_time = time.clock()
        time_taken = end_time - start_time
        print("Algorithm 2: n {0} is {1}sec".format(n, time_taken))

def code_3():
    for n in range(100, 1001, 100):
        start_time = time.clock()
        result = 0
        for r in range(n):
            c = n
            while c > 1:
                result = result ^ c
                c = c // 2 
        end_time = time.clock()
        time_taken = end_time - start_time
        print("Algorithm 3: n {0} is {1}sec".format(n, time_taken))

def code_4():
    for n in range(100, 1001, 100):
        start_time = time.clock()
        result = 0
        for r in range(n):
            for c in range(n):
                result = result ^ c
        end_time = time.clock()
        time_taken = end_time - start_time
        print("Algorithm 4: n {0} is {1}sec".format(n, time_taken))
