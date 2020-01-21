import random
def insult(x):
    "x is a string containing an entity to be insulted"
    pass

def add_new(x):
    "x is a string containing a new insult"
    d = build_dictionary()
    x = [">"] + x.split(" ")
    d = recurse(d, x)
    update(d)

def update(d):
    """updates the dictionary to the database"""
    f = open("insult_database.txt", "r+")
    f.truncate()
    ds = str(d)[1:-1:].split("], ")
    ws = ""
    for n in range(0, len(ds)):
        ds1 = ds[n].split(": [")
        ws = ds1[0][1:-1:] + ":"
        ds2 = ds1[1].split(", ")
        for n in range(0,len(ds2)):
            if ws[-1] != ":":
                ws += ","
            ws += ds2[n][1:-1:]
            print(ws)
        if n != len(ds) - 1:
            f.write(ws + "\n")
        else:
            f.write(ws)
    f.close()
    
def recurse(d, x):
    """adds the list x to the dictionary d"""
    if len(x) >= 2:
        if x[0] in d:
            if x[1] not in d[x[0]]:
                d[x[0]] += [x[1]]
        else:
            d[x[0]] = [x[1]]
        d = recurse(d, x[1::])
    return d

def build_dictionary():
    """assembles the dictionary d from the file "insult_database.txt" """
    f = open("insult_database.txt", "r")
    d = f.read().split("\n")
    f.close()
    dic = {}
    if len(d) > 1:
        for n in range(0, len(d)):
            ds = d[n].split(":")
            dic[ds[0]] = ds[1].split(",")
    return dic

