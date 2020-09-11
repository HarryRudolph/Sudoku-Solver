import pygame

#x0, y0 is top left
    
gridx0 = 75
gridx1 = 525
gridy0 = 0
gridy1 = 450

xScale = 50
yScale = 50

def renderConsoleBoard(board):
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

            
def renderGrid(screen):
    #Grid Border
    pygame.draw.lines(screen, [53, 59, 72], True, [(gridx0, gridy0), (gridx1, gridy0)], 3)
    pygame.draw.lines(screen, [53, 59, 72], True, [(gridx0, gridy1), (gridx1, gridy1)], 3)

    pygame.draw.lines(screen, [53, 59, 72], True, [(gridx0, gridy0), (gridx0, gridy1)], 3)
    pygame.draw.lines(screen, [53, 59, 72], True, [(gridx1, gridy0), (gridx1, gridy1)], 3)
    
    #Render Boxes
    pygame.draw.lines(screen, [53, 59, 72], True, [(gridx0,150), (gridx1, 150)], 3)
    pygame.draw.lines(screen, [53, 59, 72], True, [(gridx0,300), (gridx1, 300)], 3)
    
    pygame.draw.lines(screen, [53, 59, 72], True, [(225,gridy0), (225, gridy1)], 3)
    pygame.draw.lines(screen, [53, 59, 72], True, [(375,gridy0), (375, gridy1)], 3)

    #RenderColumns
    for x in range(1, 9):
        xOffset = (x * 50) + 75
        pygame.draw.lines(screen, [0, 0, 0], True,[(xOffset, gridy0), (xOffset, gridy1)], 1)

    #RenderRows
    for y in range(1, 9):
        yOffset = (y * 50)
        pygame.draw.lines(screen, [0, 0, 0], True,[(gridx0, yOffset), (gridx1, yOffset)], 1)


def renderBoard(board, screen, font):
    for y in range(9):
        for x in range(9):
            temp = 0
            temp = temp + board[y][x]
            if temp != 0: 
                text = font.render(str(temp), 0, (53, 59, 72))
                screen.blit(text, ((gridx0 + 15)+ (x * xScale), (gridy0 + 10) + (y *yScale)))
    
def renderChange(x, y, board, screen, works):
    if works:
        pygame.draw.rect(screen, (76, 209, 55), (gridx0 + (x*50), gridy0 + (y*50), 50, 50))
    else:
        pygame.draw.rect(screen, (232, 65, 24), (gridx0 + (x*50), gridy0 + (y*50), 50, 50))
        
def renderMainMenu(screen, font, items):
    text = font.render("Sudoku Solver!", 0, (53, 59, 72))
    screen.blit(text, (100, 100))

    for i in range(len(items)):
        text = font.render(str(i+1) + ") " + items[i], 0,(53, 59, 72))
        screen.blit(text, (50, 250 + (100*(i+1))))
        
def renderAboutMenu (screen, font):
    text = font.render("made my Harry Rudolph", 0, (53, 59, 72))
    screen.blit(text, (50, 250))
