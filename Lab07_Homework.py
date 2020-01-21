"""
Maxwell Randle
mran520
9607474
"""

def reverse_numbers(filename):
    file = open(filename, "r")
    contents = file.read()
    file.close()
    number_list = contents.split(" ")
    print(number_list) # <--- delete this line after testing
    reverse_list = []
    print(number_list[-1]) # <--- delete this line after testing
    for index in range(1, len(number_list), 1):
        reverse_list += number_list[-1*index]
    return reverse_list
    
