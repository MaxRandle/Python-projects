import random

def insult(x):
    "x is a string containing an entity to be insulted"
    print("Dear {},\nThe following applies to you:".format(x))
    print(choose_insult())

def add_new(x):
    "x is a string containing a new insult"
    d = build_dictionary()
    x = [">"] + x.split(" ")
    d = recurse(d, x)
    update(d)

def choose_insult():
    """chooses the insult"""
    d = build_dictionary()
    insult = ""
    word = ">"
    while word in d:
        n = random.randint(0, len(d[word])-1)
        word = d[word][n]
        insult += word + " "
    return insult

def build_dictionary():
    """constructs a dictionary from the database"""
    f = open("insult_database.txt", "r+")
    dl = f.read().split("\n")
    d = {}
    for l in dl:
        e = l.split(",")
        k = e[0]
        for v in e[1::]:
            if k in d:
                d[k] += [v]
            else:
                d[k] = [v]
    return d
    
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

def update(d):
    """saves the dictionary d into the database file in the correct format"""
    f = open("insult_database.txt", "r+")
    f.truncate()
    ss = ""
    for k in d:
        ss += str(k)
        for v in d[k]:
            ss += "," + str(v)
        ss += "\n"
    f.write(ss)
    f.close()
