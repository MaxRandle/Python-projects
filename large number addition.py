def add(string1, string2):
    
    longest_string = ""
    shortest_string = ""
    new_string = ""
    
    if len(string1) >= len(string2):
        longest_string = string1
        shortest_string = string2
    else:
        longest_string = string2
        shortest_string = string1

    remainder = 0
    for i in range(len(shortest_string)-1, -1, -1):
        remainder = 0
        partial_sum = int(longest_string[i]) + int(shortest_string[i])
        new_string += str(partial_sum)[-1]
        if partial_sum > 9:
            remainder = 1
            
        partial_sum = 0
        new_string += longest_string[len(longest_string)-(len(shortest_string)):0:-1]
    print(new_string)
