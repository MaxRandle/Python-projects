def analyse_list(xlist):
    count_list_elements(xlist)
    is_palindrome(xlist)
    sum_list(xlist)


def count_list_elements(xlist):
    used_list = []
    for element in xlist:
        while element not in used_list:
            print(element, "occurs:", xlist.count(element), "times")
            used_list += [element]
    
def sum_list(alist):
    xsum = 0
    for x in alist:
        xsum += x
    return print("integer sum:", xsum)

def is_palindrome(alist):
    if alist == alist[::-1]:
        return print("list is a palindrome")
    else:
        return print("list is not a palindrome")
    
