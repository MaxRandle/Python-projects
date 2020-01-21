"""
Maxwell Randle
mran520
9607474
"""
def cumulative_sum(sequence):
    """This function calculates the cumulative sum of a list of numbers
    Arguments: secquence - an order-specific list of numbers
    Returns: the cumulative sum of the list
    >>> cumulative_sum([1, 2, 3, 4]) 
    [1, 3, 6, 10]
    >>> cumulative_sum([4, 3, 2, 1]) 
    [4, 7, 9, 10]
    """
    cumulative_sum = []
    nSum = 0
    for number in sequence:
        nSum = nSum + number
        cumulative_sum = cumulative_sum + [nSum]
    return cumulative_sum


def unique_file(filename):
    """
    This function reads the contents of a file then returns
    a file containing each word used only once
    Arguments: filename - the name of the input file
    Returns: a file containing unique words
    """
    input_file = open(filename, 'r')
    contents = input_file.read()
    word_list = contents.split()
    unique_list = []
    for word in word_list:
        if word not in unique_list:
            unique_list = unique_list + [word]
    input_file.close()
    output_file = open('unique_values.txt', 'w')
    for word in unique_list:
        output_file.write(word)
        output_file.write('\n')
    

import doctest
doctest.testmod()
