
def possibleRow(board, rowNum, n):
    for x in range(9):
        if board[rowNum][x] == n:
            return False

    return True
        

def possibleColumn(board, colNum, n):
    for y in range(9):
        if board[y][colNum] == n:
            return False

    return True



def possibleBox(board, colNum, rowNum, n):
    boxX = (colNum // 3) * 3
    boxY = (rowNum // 3) * 3
    
    
    for y in range(boxY, boxY + 3):
        for x in range(boxX, boxX + 3):
            if board[y][x] == n:
                return False
    return True


def possible(board, x, y, n):
    if possibleColumn(board, x, n) and possibleRow(board, y, n) and possibleBox(board, x, y, n):
        return True
    return False

def findEmpty(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                return (y, x)
    return False

def solve(board):
    empty = findEmpty(board) 

    if not empty:
        return True
    else:
        y, x = empty
        
    for i in range(1, 10):
        if possible(board, x, y, i):
            board[y][x] = i
            if solve(board):
                return True
                        
            board[y][x] = 0

    return False


