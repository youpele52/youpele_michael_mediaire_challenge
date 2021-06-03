
import pygame, sys
import numpy as np
import random

pygame.init()


WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 5

CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15

BOARD_ROWS = 6
BOARD_COLS = 6

red =  (255,0, 0 )
orange= (255,165,0)
blue =  (0, 255, 255)
line_color = 	(0,0,0)
BG = (255,255,255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('COLOR GAME')
screen.fill(BG)

# board 
board = np.zeros((BOARD_ROWS, BOARD_COLS) )
# print(board)

# lines
def draw_lines():
    for num in range(00,700,100):
        #horizontal
        pygame.draw.line(screen,line_color, (0,num), (600,num), LINE_WIDTH)
        # vertital
        pygame.draw.line(screen,line_color, (num,0), (num,600), LINE_WIDTH)

def draw_figure(color, x, y):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                pygame.draw.rect(screen, color,pygame.Rect(x, y, 100, 100))
                # pygame.display.flip()
                
    
    
def mark_square(row, col, color):
    board[row][col] = color

def available_square (row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]== 0:
                return False
    return True
            



draw_lines()

color_0 = 0
color_1= 1
color_2 = 2

# mainloop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # linking console board and screen GUI board
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y
            
            clicked_row = int(mouseY // 100)
            clicked_col = int(mouseX // 100)
            
            
            print(mouseX, mouseY)
            print(clicked_col,clicked_row) 
            color = random.randint(0, 2)
            
            if available_square(clicked_row, clicked_col) :
                if color==color_0:
                    mark_square(clicked_row, clicked_col, color_0 )
                    draw_figure(blue, mouseX, mouseY)
                    color = color_1
                elif color==color_1:
                    mark_square(clicked_row, clicked_col, color_1)
                    draw_figure(orange,  mouseX, mouseY)
                    color = color_2
                elif color==color_2:
                    mark_square(clicked_row,clicked_col, color_2)
                    draw_figure(red,  mouseX, mouseY)
                    color = color_0
                    
                
                
        
    pygame.display.update()
    
