"""
Maxwell Randle
mran520
9607474
"""
def unique_list(original_list):
    """
    This function takes a list containing repeated elements and
    returns a unique list containing each value only once
    
    Arguments:
    original_list - the list to be inputed containing repeated elements
    
    Returns: a list containing each element only once

    test cases
    >>> unique_list(['cat', 'dog', 'cat', 'bug', 'dog', 'ant', 'dog', 'bug'])
    ['cat', 'dog', 'bug', 'ant']
    """
    new_list = []
    for element in original_list:
        if element not in new_list:
            new_list = new_list + [element]
    return new_list


def average_from_file(filename):
    """
    This function takes a list of numerical values separated by spaces
    from a file and calculates the average of those numbers

    Arguments:
    filename - the name of the file containing numbers separeted by spaces
    Returns: the average of those numbers

    test cases
    >>> average_from_file('marks.txt')
    47.5
    """
    input_file = open(filename, 'r')
    data = input_file.read()
    input_file.close()
    new_list = data.split(' ')
    n = len(new_list)
    mark_sum = 0
    for mark in new_list:
        mark_sum = mark_sum + int(mark)
    average = mark_sum / n
    return average

import doctest
doctest.testmod()
 
