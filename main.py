import pygame

width = 500
height = 700
screen = pygame.display.set_mode((width, height))

title = "Sudoku"

running = True

pygame.display.set_caption(title)


board = [[0, 0, 0, 0, 0, 7, 0, 0, 0],
         [0, 0, 0, 8, 9, 0, 5, 0, 0],
         [0, 4, 0, 0, 0, 3, 0, 0, 0],
         [0, 0, 0, 0, 3, 0, 0, 6, 0],
         [7, 0, 3, 2, 0, 9, 0, 0, 0],
         [9, 0, 0, 6, 0, 1, 0, 0, 4],
         [0, 5, 0, 0, 0, 2, 4, 0, 0],
         [0, 0, 6, 4, 0, 0, 2, 0, 8],
         [0, 0, 0, 0, 0, 0, 7, 0, 3]]

boardEasy = [[0, 0, 3, 5, 6, 0, 4, 7, 0],
         [0, 0, 0, 3, 4, 2, 0, 0, 1],
         [0, 2, 0, 1, 9, 7, 0, 0, 0],
         [4, 3, 0, 0, 0, 6, 8, 1, 0],
         [2, 0, 6, 8, 0, 0, 0, 9, 0],
         [9, 0, 0, 0, 0, 3, 0, 6, 0],
         [0, 0, 0, 6, 0, 5, 1, 2, 3],
         [0, 5, 8, 0, 0, 9, 7, 0, 0],
         [0, 0, 2, 0, 3, 4, 5, 0, 0]]



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
    

def possibleRow(rowNum, n):
    for x in range(9):
        if board[rowNum][x] == n:
            return False

    return True
        

def possibleColumn(colNum, n):
    for y in range(9):
        if board[y][colNum] == n:
            return False

    return True



def possibleBox(colNum, rowNum, n):
    boxX = (colNum // 3) * 3
    boxY = (rowNum // 3) * 3
    
    
    for y in range(boxY, boxY + 3):
        for x in range(boxX, boxX + 3):
            if board[y][x] == n:
                return False
    return True


def possible(x, y, n):
    if possibleColumn(x, n) and possibleRow(y, n) and possibleBox(x, y, n):
        return True
    return False

def solve():
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0: 
                for i in range(1, 10):
                    if possible(x, y, i):
                        board[y][x] = i
                        solve()
                        board[y][x] = 0
                return
    renderBoard()

renderBoard()
print("Now solved:")
solve()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

