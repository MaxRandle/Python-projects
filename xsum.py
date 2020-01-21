def sum_list(alist):
    xsum = 0
    for x in range(0, len(list), 1):
        xsum += list[x]
    return xsum

def is_palindrome(alist):
    if alist == alist[::-1]:
        return True
    else:
        return False

