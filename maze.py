def initialize_maze(size):
    cell_list = get_cells(size)
    maze = {}
    for cell in cell_list:
        maze[cell] = get_neighbours(cell, size)
    return maze
        

def get_cells(size):
    cell_list = []
    for y in range(0, size):
        for x in range(0, size):
            cell = (x, y)
            cell_list += [cell]
    return cell_list

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
