
def quicksort(array):
    if len(array) > 1:
        import random
        p = random.randint(0, len(array)-1) #pivot
        l, r = 0, len(array)
        temp = array[p]
        while array[l] < array[r]:
            
    else:
        return array
    """
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for n in array:
            if n < pivot:
                less.append(n)
            elif n == pivot:
                equal.append(n)
            else:
                greater.append(n)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array
    """

def mergesort(array):
    result = []
    if len(array) < 2:
        return array
    mid = int(len(array)/2)
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result
