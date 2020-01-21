import copy

def get_generation(cells, generations):
    rep(cells)
    
    for g in range(generations):
        cells = padGame(cells)
        newcells = copy.deepcopy(cells)
        #rows
        for row in range(len(cells)):
            #cols
            for col in range(len(cells[0])):
                c = countLivingNeighbours(row, col, cells)
                if cells[row][col] == 1:
                    if (c < 2) or (c > 3):
                        newcells[row][col] = 0
                elif c == 3:
                    newcells[row][col] = 1
        newcells = trimGame(newcells)
        cells = copy.deepcopy(newcells)
        rep(cells)
                
    #return cells
    
def countLivingNeighbours(row, col, cells):
    res = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            #if i is an existing row
            if i in range(0, len(cells)):
                #if j is an existing column
                if j in range(0, len(cells[0])):
                    res += cells[i][j]
    #remove center cell to leave neighbours
    res -= cells[row][col]
    return res

def padGame(cells):
    #adds a boarder of 0's around the game to allow room for new growth
    top = []
    bot = []
    for col in range(0, len(cells[0])):
        top += [0]
        bot += [0]
    cells = [top] + cells + [bot]
    for i in range(len(cells)):
        cells[i] = [0] + cells[i] + [0]
    #print(cells)
    return cells

def trimGame(cells):
    #trims outside 0's

    #trim vertical
    while True:
        if 1 not in cells[0]:
            cells.pop(0)
        else:
            break
    while True:
        if 1 not in cells[-1]:
            cells.pop(-1)
        else:
            break

    #trim horizontal
    while True:
        empty = True
        for i in range(len(cells)):
            if cells[i][0] == 1:
                empty = False
        if empty == False:
            break
        else:
            for i in range(len(cells)):
                cells[i].pop(0)
    while True:
        empty = True
        for i in range(len(cells)):
            if cells[i][-1] == 1:
                empty = False
        if empty == False:
            break
        else:
            for i in range(len(cells)):
                cells[i].pop(-1)                
                
    return cells
    

def rep(cells):
    #draws the game and the neighbours
    out = ""
    #rows
    for i in range(len(cells)):
        #cols
        for j in range(len(cells[0])):
            if cells[i][j] == 1:
                out += "#"
            else:
                out += " "
        out += "|\n"
    print(out)
    print("-"*len(cells[0]))
    out = ""
    for i in range(len(cells)):
        for j in range(len(cells)):
            out += str(countLivingNeighbours(i, j, cells))
        out += "\n"
    #print(out)



"""
ACORN

get_generation([[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]], 200)

"""
