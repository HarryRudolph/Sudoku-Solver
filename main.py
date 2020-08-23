

board = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
         [2, 3, 4, 5, 6, 7, 8, 9, 1],
         [3, 4, 5, 6, 7, 8, 9, 1, 2],
         [4, 5, 6, 7, 8, 9, 1, 2, 3],
         [5, 6, 7, 8, 9, 1, 2, 3, 4],
         [6, 7, 8, 9, 1, 2, 3, 4, 5],
         [7, 8, 9, 1, 2, 3, 4, 5, 6],
         [8, 9, 1, 2, 3, 4, 5, 6, 7],
         [9, 1, 2, 3, 4, 5, 6, 7, 8]]


def renderBoard():
    for y in range(9):
        for x in range(9):
            print(board[x][y], end = '')

            if (x == 2) or (x ==5):
                print(" | ", end = '')
            else:
                print(" ", end = '')

            if (x == 8):
                print()

        if (y == 2) or (y == 5):
            print("=====================")
    

def checkRow(rowNum):
    #Loop through the row, adding each cell to a list. Before adding check to see if it is already in the list
    compare = []
    
    for x in range(9):
        for i in compare:
            if i == board[rowNum][x]:
                return False
            
        compare.append(board[rowNum][x])
    return True

def checkColumn(colNum):
    compare = []
    
    for y in range(9):
        for i in compare:
            if i == board[y][colNum]:
                return False
            
        compare.append(board[y][colNum])

    return True



def checkSquare():
    pass



renderBoard()

if checkColumn(0):
    print("the column is fine")
else:
    print("the column is not fine")

    
if checkRow(0):
    print("the line is fine")
else:
    print("the line is not fine")
