
board = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
         [4, 5, 6, 5, 6, 7, 8, 9, 1],
         [7, 8, 9, 6, 7, 8, 9, 1, 2],
         [4, 5, 6, 7, 8, 9, 1, 2, 3],
         [5, 6, 7, 8, 9, 1, 2, 3, 4],
         [6, 7, 8, 9, 1, 2, 3, 4, 5],
         [7, 8, 9, 1, 2, 3, 4, 5, 6],
         [8, 9, 1, 2, 3, 4, 5, 6, 7],
         [9, 1, 2, 3, 4, 5, 6, 7, 8]]


def renderBoard():
    for y in range(9):
        for x in range(9):
            print(board[y][x], end = '')

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



def checkBox(boxNum):
    #Box numbers are 1-9
    compare = []

    # for box in range(9):
    #I'm sure there is a better way. Somehow I need to set y based on boxNum

    if boxNum == 1 or boxNum == 2 or boxNum == 3:
        yArray = [0, 1, 2]
    if boxNum == 4 or boxNum == 5 or boxNum == 6:
        yArray = [3, 4, 5]
    if boxNum == 7 or boxNum == 8 or boxNum == 9:
        yArray = [6, 7, 8]
    
    for y in yArray:
        for x in range(3):
            for i in compare:
                if i == board[y][x*(boxNum % 3)]:
                #    print("compare: ", compare, "| x = ", x, "| y = ", y)

                    print("the box is bad")
                    return False
            compare.append(board[y][x*boxNum% 3])

    print("the box is fine")
    return True


renderBoard()

if checkColumn(0):
    print("the column is fine")
else:
    print("the column is not fine")

    
if checkRow(0):
    print("the line is fine")
else:
    print("the line is not fine")



checkBox(1)
