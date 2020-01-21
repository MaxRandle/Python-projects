def test():
    x = input("type 1 or 2:\n")
    if x == 1:
        return("1")
        test()
    else:
        return("2")
        test()


def squared(int_list):
    time_start = time.clock()
    square_list = []
    for number in int_list:
        squarelist += [number**2]
    time_end = time.clock()
    return suqare_list


def string_to_integer(string):
    didgits = "0123456789"
    int_string = ""
    for character in string:
        if character in didgits:
            int_string += character
    integer = int(int_string)
    return integer


def stringCompare(s1, s2):
    a1 = s1.split("\n")
    a2 = s2.split("\n")
    for i in range(0, len(a1)):
        if a1[i] != a2[i]:
            print(a1[i])
            print(a2[i])


def validBraces(s):
    return reduce(s) == ""

def reduce(s):
    l = len(s)
    s.replace("()", "").replace("[]", "").replace("{}", "")
    if l == len(s):
        return s
    return reduce(s)
