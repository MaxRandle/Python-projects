def get_corridors(src):
    """This method should return a list of all the 
    cells (as x,y tuples) that can be reached from
    the source cell given as a parameter
    """
    neighbour_list = []
    n1 = (cell[0], cell[1]-1) #top
    n2 = (cell[0], cell[1]+1) #bottom
    n3 = (cell[0]-1, cell[1]) #left
    n4 = (cell[0]+1, cell[1]) #right
    neighbour_list += n3, n1, n2, n4
    return neighbour_list

def make_maze(size):
    """This method does the work of creating the maze.  If the size of the
    maze is less than 1, then it should raise a ValueError with the message:
    "Maze must be at least size 1".
    
    *  The size is stored in a state variable called size
    
    When you have implemented full_maze, the constructor
    should call that method to generate the maze.
    """
    if size < 1:
        return "Maze must be at least size 1"
    cell_list = []
    for x in range(0, size):
        for y in range(0, size):
            cell = (x, y)
            maze_list += [cell]
    return cell_list
