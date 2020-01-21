import random

class maze:
    def get_neighbours(self, src):
        """This method returns a list of the cell
        locations that are adjacent to the source cell
        passed as a parameter
        
        Note:  This code is complete.  Do not edit this method.
        """
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        neighbours = []
        for dx,dy in directions:
            x = src[0] + dx
            y = src[1] + dy
            if x in range(self.size) and y in range(self.size):
                neighbours.append((x, y))
        return sorted(neighbours)

    def blank_maze(self):
        """This method creates a blank maze.  Each cell in the grid is 
        connected to every adjacent cell.  In other words, there are no walls
        in this maze.  Useful only for testing.
        
        Note:  This code is complete.  Do not edit this method.
        """
        self.maze = {}
        for y in range(self.size):
            for x in range(self.size):
                self.maze[(x,y)] = self.get_neighbours((x,y))
    
    def __init__(self, size):
        """This method does the work of creating the maze.  If the size of the
        maze is less than 1, then it should raise a ValueError with the message:
        "Maze must be at least size 1".
        
        *  The size is stored in a state variable called size
        
        When you have implemented full_maze, the constructor
        should call that method to generate the maze.
        """
        if size < 1:
            return "Maze must be at least size 1"
        self.size = size
        cell_list = []
        for x in range(0, size):
            for y in range(0, size):
                cell = (x, y)
                maze_list += [cell]
        return cell_list
    
    def get_corridors(self, cell):
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
    
    def __repr__(self):
        """This method should return a string representation of
        the maze.  It should simply format the dictionary containing
        the maze connections with each curly brace on their own line,
        and each entry of the dictionary on a separate line.  The entries
        are given in sorted order based on the keys.  For example, a maze
        with a size of 2 might be represented by the following string:
        {
        (0, 0):[(0, 1)]
        (0, 1):[(0, 0), (1, 1)]
        (1, 0):[(1, 1)]
        (1, 1):[(0, 1), (1, 0)]
        }
        """
        pass

    def pop_random_element(self, the_list):
        """This method picks a random element from a list, removes that
        element from the list and returns the element.  
        
        Note:  the pop() function might be useful here
        """
        x = random.randint(0, len(the_list))
        return the_list.pop(the_list[x])
    
    def add_connection(self, src, dst):
        """This method adds a link in the self.maze dictionary between the 
        src and dst locations.  These links will always occur in pairs, since
        a link from a to b is mirrored in the link from b to a.  
        
        Note:  if the key already exists in the dictionary, then the link must
        be *appended* to the existing list of connections stemming from a, but 
        if the key does not exist, then you will have to create a new entry.
        """
        pass

    def append_unique(self, src, dst):
        """This method appends the elements of the src list to the dst list,
        but only if they are not already in the dst list.  In other words, the
        dst list is increased by adding new elements from the src list.
        """
        pass

    def partition_cells(self, locations):
        """This method divides the cells in the location list into two lists - 
        those cells that are already in the maze (i.e. they are present in the 
        dictionary called self.maze) and those cells that are not in the maze.
        The method should return both the inside and outside lists (in that order).
        
        Note: you can use the syntax:
        
        return inside_list, outside_list
        
        to return two different things from a single function.  When you call
        the function you use:
        
        first, second = self.partition_cells(input_list)
        """
        pass
    
    def full_maze(self):
        """This method generates the maze using Prim's algorithm.  The algorithm
        is repeated below for convenience.
        """
        #Create a new empty dictionary to store the maze
        maze= {}
        #Add the location (0,0) to the maze with no cells connected to it
        #Create a frontier list containing the neighbouring cells of (0,0)
                
        #while the frontier list is not empty
        
            #pick a random cell from the frontier list
            #the picked cell will be the next one we add to the maze
            #ADD CODE        
            
            #get the cells adjacent to the cell we picked
            #ADD CODE        
            
            #divide the adjacent cells into a list of cells that are already 
            #inside the maze, and cells that are not in the maze (outside)
            #ADD CODE        
            
            #pick a random cell from the list of cells that are in the maze
            #ADD CODE        
        
            #add a connection between the cell that we wanted to add, and 
            #the randomly chosen cell from within the maze
            #ADD CODE        
            
            #add the list of cells that was not in the maze (the adjacent cells
            #that are outside the maze) to the frontier list if they are not 
            #already in that list.
            #ADD CODE        
        pass

