import pygame

import solve, render
pygame.init()

width = 600
height = 800

title = "Sudoku"

running = True

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 50)

gameStarted = False

mainMenuItems = ["start", "about", "exit"]

# pygame.time.set_timer(updateBoard, 500)

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

screen.fill((220, 221, 225))
render.renderMenu(screen, font, mainMenuItems)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if gameStarted:
                    solve.solve(board, screen, font)
                gameStarted = True
            if event.key == pygame.K_2:
                renderConsoleBoard()



    if gameStarted:
        screen.fill((220, 221, 225))
        render.renderBoard(board, screen, font)
        render.renderGrid(screen)

            
    pygame.display.update()
    clock.tick(30)
    
