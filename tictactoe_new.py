import pygame as pg,sys
from pygame.locals import *
import time

XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255,255,255)
line_color = (69, 144, 255)


TTT = [[None]*3,[None]*3,[None]*3]


#initializing py game window
pg.init()
fps = 40
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width,height+100),0,32)
pg.display.set_caption("Tic Tac Toe")


#loading the images
opening = pg.image.load('tictactoe.jpg')
x_img = pg.image.load('xblue.png')
o_img = pg.image.load('oblue.png')

#Resizing the loaded images
x_img = pg.transform.scale(x_img,(80,80))
o_img = pg.transform.scale(o_img,(80,80))
opening = pg.transform.scale(opening,(width,height+100))


#game inititalisation

def game_open():
    screen.blit(opening,(0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

    #Vertical Lines
    pg.draw.line(screen,line_color,(width/3,0),(width/3,height),7)
    pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2,height),7)

    #Horizontal Lines
    pg.draw.line(screen,line_color,(0,height/3),(width,height/3),7)
    pg.draw.line(screen,line_color,(0,height/3*2),(width,height/3*2),7)
    draw_status()


def draw_status():
    global draw

    if winner is None:
        message = XO.upper()+"'s Turn"
    else:
        message = winner.upper()+" won!"
    if draw:
        message = 'Game Draw!'

    font = pg.font.Font(None,30)
    text= font.render(message,1,(255,255,255))

    #copying the rendered message onto the board
    
    screen.fill((69, 144, 255),(0,400,500,100))
    text_rect = text.get_rect(center=(width/2,500-50))
    screen.blit(text,text_rect)
    pg.display.update()


def check_win():
    global TTT,winner,draw


    #check for rows

    for row in range (3):
        if(TTT[row][0]==TTT[row][1]==TTT[row][2]) and (TTT[row][0] is not None):
            winner = TTT[row][0]
            print("Winner",winner)
            pg.draw.line(screen,(250,0,0),(0,(row+1)*height/3-height/6),(width,(row+1)*height/3-height/6),4)
            break


    #check for columns

    for col in range(3):
        if(TTT[0][col]==TTT[1][col]==TTT[2][col]) and (TTT[0][col] is not None):
            winner = TTT[0][col]
            pg.draw.line(screen,(250,0,0),((col+1)*width/3-width/6,0),((col+1)*width/3-width/6,height),4)
            break


    #check for diagonal left to right

    if (TTT[0][0]==TTT[1][1]==TTT[2][2]) and (TTT[0][0] is not None):
        winner = TTT[0][0]
        pg.draw.line(screen,(250,0,0),(0,0),(width,height),4)
       

    if(TTT[0][2]==TTT[1][1]==TTT[2][0]) and (TTT[0][2] is not None):
        winner = TTT[0][2]
        pg.draw.line(screen,(250,0,0),(width,0),(0,height),4)
        

    if(all([all(row) for row in TTT]) and winner is None):
        draw = True
    draw_status()


    
        
def drawXO(row,col):
    global TTT,XO

    if row == 1:
        posy = 30

    if row == 2:
        posy = width/3 +30

    if row == 3:
        posy = width/3*2 + 30

    if col == 1:
        posx = 30

    if col == 2:
        posx = height/3 + 30

    if col == 3:
        posx = height/3*2 + 30

    TTT[row-1][col-1]=XO

    print("Value of posx and posy",posx,posy)

    if(XO=='x'):
        screen.blit(x_img,(posx,posy))
        XO='o'

    else:
        screen.blit(o_img,(posx,posy))
        XO = 'x'
    pg.display.update()


def userClick():
    #coordinates of mouse
    x,y = pg.mouse.get_pos()

    if(x<width/3):
        col = 1
    elif (x<width/3*2):
        col =2
    elif (x<width):
        col = 3
    else:
        col = None

    if(y<height/3):
        row = 1
    elif(y<height/3*2):
        row = 2

    elif(y<height):
        row = 3

    else:
        row = None

    print("Value of x and y",x,y)
    print("Value of row and column",row,col)

    if (row and col and TTT[row-1][col-1] is None):
        global XO

        drawXO(row,col)
        check_win()


def reset_game():
    global TTT,winner,XO,draw
    time.sleep(3)
    XO='x'
    draw = False
    game_open()
    winner = None
    TTT = [[None]*3,[None]*3,[None]*3]





    




game_open()

while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        elif event.type is MOUSEBUTTONDOWN:
            userClick()

            if (winner or draw ):
                reset_game()


    pg.display.update()


