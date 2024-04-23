import pygame
import math
import copy
import random
def place(image, pos, player):
    print(pos)
    board[pos[0]][pos[1]] = player
    pos = pos = (pos[1] * 170 + 45, pos[0] * 170 + 45)
    screen.blit(image, pos)
    pygame.display.flip()
def won(board):
    if math.fabs(board[0][0] + board[1][1] + board[2][2]) == 3 or math.fabs(board[0][2] + board[1][1] + board[2][0]) == 3:
        return board[1][1]
    for i in range(3):
        if math.fabs(board[i][0] + board[i][1] + board[i][2]) == 3 or math.fabs(board[0][i] + board[1][i] + board[2][i]) == 3:
            return board[i][i]
    return 0
def reset():
    screen.blit(background, (0,0))
    pygame.display.flip()
    for i in range(3):
        for j in range(3):
            board[i][j] = 0    
def minimax(board, switch = True):
    l = copy.deepcopy(board)
    print(l)
    temp = val = 0
    pos = (None, None)
    for i in range(3):
        for j in range(3):
            if l[i][j] == 0:
                if switch:
                    l[i][j] = 1
                else:
                    l[i][j] = -1
                temp = won(l)
                if temp != 0:
                    return (i,j), temp
                else:
                    try:
                        temp = minimax(l[:], not switch)[1]
                    except RecursionError:
                        return pos, val
                    if switch:
                        if val < temp:
                            val = temp
                            pos = (i,j)
                    else:
                        if val > temp:
                            val = temp
                            pos = (i,j)
                l[i][j] = 0
    return pos, val
board = list()
for i in range(3):
    board.append([0]*3)
pygame.init()
random.seed()
screen = pygame.display.set_mode(size = (512, 512), flags = pygame.NOFRAME, vsync = 1)
pygame.display.set_caption('Tic-Tac-Toe')
background = pygame.image.load('Tic.bmp').convert()
screen.blit(background,(0,0))
cross = pygame.image.load('Cross.bmp').convert()
cross.set_colorkey((255,255,255))
circle = pygame.image.load('Circle.bmp').convert()
circle.set_colorkey((255,255,255))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            place(cross, (pos[1]//170, pos[0]//170), -1)
            if won(board):
                reset()
                break
            pos = minimax(board)[0]
            if pos == (None, None):
                choices = list()
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 0:
                            choices.append((i,j))
                if choices == list():
                    reset()
                    break
                pos = random.choice(choices)   
            place(circle, pos, 1)
            if won(board):
                reset()
                break