import math
def balance(num_list):
    mid_point = math.ceil(len(num_list)/2)
    list1 = num_list[0:mid_point:1]
    list2 = num_list[mid_point:len(num_list):1]
    print(list1, list2)
    if len(num_list) % 2 == 1:
        list2 += [0]
    print(list1, list2)
    diff = {}
    for i1 in range(0, len(list1), 1):
        for i2 in range(0, len(list1), 1):
            temp1, temp2 = swap_object(list1, i1, list2, i2)
            if check_sum_diff(list1, list2) > check_sum_diff(temp1, temp2):
                   list1, list2 = swap_object(list1, i1, list2, i2)
    return list1, list2

def check_sum_diff(l1, l2):
   return abs(sum(l1) - sum(l2))

def swap_object(l1, i1, l2, i2):
    temp = l1[i1]
    l1[i1] = l2[i2]
    l2[i2] = temp
    return l1, l2
