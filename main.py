import pygame
pygame.init()


width = 600
height = 800

title = "Sudoku"

running = True

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

font = pygame.font.SysFont("comicsans", 50)
clock = pygame.time.Clock()

#x0, y0 is top left
    
gridx0 = 75
gridx1 = 525
gridy0 = 0
gridy1 = 450

xScale = 50
yScale = 50





boardHard = [[0, 0, 0, 0, 0, 7, 0, 0, 0],
         [0, 0, 0, 8, 9, 0, 5, 0, 0],
         [0, 4, 0, 0, 0, 3, 0, 0, 0],
         [0, 0, 0, 0, 3, 0, 0, 6, 0],
         [7, 0, 3, 2, 0, 9, 0, 0, 0],
         [9, 0, 0, 6, 0, 1, 0, 0, 4],
         [0, 5, 0, 0, 0, 2, 4, 0, 0],
         [0, 0, 6, 4, 0, 0, 2, 0, 8],
         [0, 0, 0, 0, 0, 0, 7, 0, 3]]

board = [[0, 0, 3, 5, 6, 0, 4, 7, 0],
         [0, 0, 0, 3, 4, 2, 0, 0, 1],
         [0, 2, 0, 1, 9, 7, 0, 0, 0],
         [4, 3, 0, 0, 0, 6, 8, 1, 0],
         [2, 0, 6, 8, 0, 0, 0, 9, 0],
         [9, 0, 0, 0, 0, 3, 0, 6, 0],
         [0, 0, 0, 6, 0, 5, 1, 2, 3],
         [0, 5, 8, 0, 0, 9, 7, 0, 0],
         [0, 0, 2, 0, 3, 4, 5, 0, 0]]



def renderConsoleBoard():
    for y in range(9):
        for x in range(9):
            print(board[y][x], end = '')

            if (x == 2) or (x == 5):
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


def findEmpty():
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                return (y, x)
    return False

def solve():
    empty = findEmpty() 

    if not empty:
        return True
    else:
        y, x = empty
        
        
    for i in range(1, 10):
        if possible(x, y, i):
            board[y][x] = i
            if solve():
                return True
                        
            board[y][x] = 0

    return False
    renderConsoleBoard()
    





def renderGrid():
    #Grid Border
    pygame.draw.lines(screen, [0,0,0], True, [(gridx0, gridy0), (gridx1, gridy0)], 3)
    pygame.draw.lines(screen, [0,0,0], True, [(gridx0, gridy1), (gridx1, gridy1)], 3)

    pygame.draw.lines(screen, [0,0,0], True, [(gridx0, gridy0), (gridx0, gridy1)], 3)
    pygame.draw.lines(screen, [0,0,0], True, [(gridx1, gridy0), (gridx1, gridy1)], 3)
    
    #Render Boxes
    pygame.draw.lines(screen, [0,0,0], True, [(gridx0,150), (gridx1, 150)], 3)
    pygame.draw.lines(screen, [0,0,0], True, [(gridx0,300), (gridx1, 300)], 3)
    
    pygame.draw.lines(screen, [0,0,0], True, [(225,gridy0), (225, gridy1)], 3)
    pygame.draw.lines(screen, [0,0,0], True, [(375,gridy0), (375, gridy1)], 3)

    #RenderColumns
    for x in range(1, 9):
        xOffset = (x * 50) + 75
        pygame.draw.lines(screen, [0, 0, 0], True,[(xOffset, gridy0), (xOffset, gridy1)], 1)

    #RenderRows
    for y in range(1, 9):
        yOffset = (y * 50)
        pygame.draw.lines(screen, [0, 0, 0], True,[(gridx0, yOffset), (gridx1, yOffset)], 1)


def renderBoard():
    for y in range(9):
        for x in range(9):
            temp = 0
            temp = temp + board[y][x]
            text = font.render(str(temp), 0, (0,0,0))
            screen.blit(text, ((gridx0 + 15)+ (x * xScale), (gridy0 + 10) + (y *yScale)))
        

while running:
    screen.fill((220, 221, 225))    
    renderGrid()
    renderBoard()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                solve()
            if event.key == pygame.K_2:
                #board[0][0]= 9
                renderConsoleBoard()

    pygame.display.update()
    clock.tick(1)
    
