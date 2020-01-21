def guess(min_bound, max_bound, repeat):
    import random
    correct = 0
    incorrect = 0
    for n in range(repeat):
        a = random.randint(min_bound, max_bound)
        b = random.randint(min_bound, max_bound)
        k = random.randint(min_bound, max_bound)
        if a > k:
            if a > b:
                correct += 1
            else:
                incorrect += 1
        else:
            if a < b:
                correct += 1
            else:
                incorrect += 1
                
    print("{}%".format(round(correct/(correct+incorrect)*100, 2)))
