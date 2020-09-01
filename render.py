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


def renderBoard(board, screen, font):
    for y in range(9):
        for x in range(9):
            temp = 0
            temp = temp + board[y][x]
            text = font.render(str(temp), 0, (0,0,0))
            screen.blit(text, ((gridx0 + 15)+ (x * xScale), (gridy0 + 10) + (y *yScale)))
