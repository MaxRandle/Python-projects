def get_neighbours(cell, size):
    x = int(size - 1)
    neighbour_list = []
    strict_list = []
    n1 = (cell[0], cell[1]-1) #top
    n2 = (cell[0], cell[1]+1) #bottom
    n3 = (cell[0]-1, cell[1]) #left
    n4 = (cell[0]+1, cell[1]) #right
    neighbour_list += n3, n1, n2, n4
    for cell in neighbour_list:
        if (cell[0] <= x) and (cell[0] >= 0) and (cell[1] <= x) and (cell[1] >= 0):
            strict_list += ([cell])
    return strict_list
