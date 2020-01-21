import math
def Lucas_numbers(n):
    ratio = ((1+math.sqrt(5))/2)
    lucas_list = [2,1]
    ratio_power_list = []
    if n < 2:
        return "Two or more terms are required to calculate the ratio."
    for number in range(0,n-2,1):
        lucas_list += [lucas_list[-1] + lucas_list[-2]]
    for term in range(0,n,1):
        x1 = lucas_list[term]
        x2 = ratio**term
        print("term_n = {0}: lucas number = {1}, ratio^n = {2}, error = {3}".format(term+1, x1, x2, x1-x2))
    return
