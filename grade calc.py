def grade(mark):
    """This program inputs a mark out of 100 and returns a meaningful grade
    Arguments:
        mark - the raw mark out of 100 (float)
    Returns:
        the grade as a letter, either A, B, C or D (string)
    >>> grade(24)
    D
    >>> grade(80.0)
    A
    >>> grade(56.32)
    C
    """
    if mark < 50:
        print("D")
    elif mark < 65:
        print("C")
    elif mark < 80:
        print("B")
    else:
        print("A")
        
import doctest
doctest.testmod()
