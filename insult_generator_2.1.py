import random
import ast
def insult(x):
    "x is a string containing an entity to be insulted"
    print("Dear {},\nThe following applies to you:".format(x))
    print(choose_insult())
    
def add_new(x):
    "x is a string containing a new insult"
    d = build_dictionary()
    x = [">"] + x.split(" ") + [""]
    d = recurse(d, x)
    update(d)

def update(d):
    f = open("insult_database.txt", "w")
    f.truncate()
    f.write(str(d))
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
    f = open("insult_database.txt", "r")
    d = f.read()
    f.close()
    dic = ast.literal_eval(d)
    return dic

def choose_insult():
    d = build_dictionary()
    insult = ""
    word = ">"
    while word in d:
        n = random.randint(0, len(d[word])-1)
        word = d[word][n]
        insult += word + " "
    return insult
    
