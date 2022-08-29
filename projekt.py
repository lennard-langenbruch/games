import pygame
import random
import os

## Globals
FPS = 7
DIMENSION = 500
SIZE = DIMENSION/25
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
EARTH = "#c4b7a6"

## Functions
def drawButton(file, resizew, resizeh, placex, placey):
    i = pygame.image.load(file)
    i = pygame.transform.scale(i, (resizew, resizeh))
    screen.blit(i, (placex - resizew / 2, placey - resizeh / 2))







## Initialize
pygame.init()

## Create Window
screen = pygame.display.set_mode((DIMENSION,DIMENSION))
pygame.display.set_caption("2d snake variation")

## Game loop condition
running = True
playing = True
pause = False
gameover = False

## last input
lastkeyevent = ""

## to keep track of length
tail = 0

## keep track of past location for tail
history = []

## to keep track of x- and y-coordinate of snake
xhead = yhead = 0

## x-coordinate of apple
## random integer between 0 and DIMENSION
xapple = random.randint(0,DIMENSION-SIZE)

## while its not a multiple of SIZE assign again
while xapple % SIZE != 0:
    xapple = random.randint(0, DIMENSION-SIZE)

## y-coordinate of apple
## random integer between 0 and DIMENSION
yapple = random.randint(0,DIMENSION-SIZE)

## while its not a multiple of SIZE assign again
while yapple % SIZE != 0:
    yapple = random.randint(0,DIMENSION-SIZE)

## width and height of snake/rectangle, xvelocity and yvelocity matches width and height
xvelocity = w = h = SIZE
yvelocity = 0

#get recent highcore
if not os.path.exists("save/highscore.txt"):
    writefile = open("save/highscore.txt", "w")
    writefile.write("0")
    writefile.close()
readfile = open("save/highscore.txt", "r")
highscore = readfile.readline()
readfile.close()







## actual game/while loop
while running:

    if playing:
        ## set ticks
        fps = pygame.time.Clock()
        ## case events/input
        for event in pygame.event.get():
            ## quit
            if event.type == pygame.QUIT:
                running = False
            ## controls
            if event.type == pygame.KEYDOWN:
                #
                if event.key == pygame.K_ESCAPE:
                    playing = False
                    pause = True

                #
                if event.key == pygame.K_LEFT and lastkeyevent != "right":
                    #
                    lastkeyevent = "left"
                    #
                    yvelocity = 0
                    xvelocity = SIZE
                    #
                    xvelocity=xvelocity*-1
                ##
                if event.key == pygame.K_RIGHT and lastkeyevent != "left":
                    #
                    lastkeyevent = "right"
                    #
                    yvelocity = 0
                    xvelocity = SIZE
                    #
                    xvelocity=xvelocity*1
                ##
                if event.key == pygame.K_UP and lastkeyevent != "down":
                    #
                    lastkeyevent = "up"
                    #
                    yvelocity = SIZE
                    xvelocity = 0
                    #
                    yvelocity=yvelocity*-1
                ##
                if event.key == pygame.K_DOWN and lastkeyevent != "up":
                    #
                    lastkeyevent = "down"
                    #
                    yvelocity = SIZE
                    xvelocity = 0
                    #
                    yvelocity=yvelocity*1
        ## draw
        screen.fill(BLACK)
        #draw score
        fontx = pygame.font.SysFont(None, 24)
        tx = fontx.render('score:  '+str(tail), True, EARTH)
        screen.blit(tx, (2, 2))
        #draw highscore
        fonty = pygame.font.SysFont(None, 24)
        ty = fonty.render('highscore:  '+str(highscore), True, EARTH)
        screen.blit(ty, (2, 25))


        ## case apple eats snake
        if(xhead == xapple and yhead == yapple):
            ##length/tail increases
            pygame.mixer.music.load('sound/schleck.wav')
            pygame.mixer.music.play()

            #pygame.mixer.music.pause()
            tail=tail+1

            ## remove apple by overdrawing
            pygame.draw.rect(screen, WHITE, pygame.Rect(xapple, yapple, w, h))

            ## xapple random multiple of SIZE
            xapple = random.randint(0, DIMENSION-SIZE)
            while xapple % SIZE != 0:
                xapple = random.randint(0, DIMENSION-SIZE)

            # yapple random multiple of SIZE
            yapple = random.randint(0, DIMENSION-SIZE)
            while yapple % SIZE != 0:
                yapple = random.randint(0, DIMENSION-SIZE)

        ## draw head
        if(xhead > DIMENSION or xhead < 0):
            playing = False
            gameover = True
        if(yhead > DIMENSION or yhead < 0):
            playing = False
            gameover = True

        ##
        pygame.draw.rect(screen, WHITE, pygame.Rect(xhead, yhead, w, h))

        ## draw tail
        for l in range(tail):
            pygame.draw.rect(screen, WHITE, pygame.Rect(history[l][0], history[l][1], w, h))

        ## draw apple
        pygame.draw.rect(screen, RED, pygame.Rect(xapple, yapple, w, h))

        ## track head past location for tail
        history.insert(0,(xhead,yhead))

        ## change/update snake position
        xhead= xhead + xvelocity
        yhead= yhead + yvelocity

        # case head hits tail
        if((xhead,yhead) in history[:tail]):
            pygame.mixer.music.load('sound/die.wav')
            pygame.mixer.music.play()
            playing = False
            gameover = True

        ## update
        pygame.display.update()
        fps.tick(FPS)

    if not playing:
        if pause:
            for event in pygame.event.get():
                ## quit
                if event.type == pygame.QUIT:
                    running = False
                ## controls
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (DIMENSION/2-150 < pygame.mouse.get_pos()[0] < (DIMENSION/2+150)) and (DIMENSION/2-50 < pygame.mouse.get_pos()[1] < (DIMENSION/2)+50):
                        pause = False
                        playing = True

            #Call Button Function
            drawButton("images/resume.png",300,100,DIMENSION/2,DIMENSION/2)
            #Display Update()
            pygame.display.update()

        if gameover:
            ## case events/input
            for event in pygame.event.get():
                ## quit
                if event.type == pygame.QUIT:
                    running = False
                ## controls
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (DIMENSION/2-150 < pygame.mouse.get_pos()[0] < (DIMENSION/2+150)) and (DIMENSION/2-50 < pygame.mouse.get_pos()[1] < (DIMENSION/2)+50):
                        ## Program
                        ## game/while loop condition
                        running = True
                        playing = True
                        gameover = False
                        ## last input
                        lastkeyevent = ""
                        ## to keep track of length
                        tail = 0
                        ## keep track of past location for tail
                        history = []
                        ## to keep track of x- and y-coordinate of snake
                        xhead = yhead = 0
                        ## x-coordinate of apple
                        ## random integer between 0 and DIMENSION
                        xapple = random.randint(0, DIMENSION - SIZE)
                        ## while its not a multiple of SIZE assign again
                        while xapple % SIZE != 0:
                            xapple = random.randint(0, DIMENSION - SIZE)
                        ## y-coordinate of apple
                        ## random integer between 0 and DIMENSION
                        yapple = random.randint(0, DIMENSION - SIZE)
                        ## while its not a multiple of SIZE assign again
                        while yapple % SIZE != 0:
                            yapple = random.randint(0, DIMENSION - SIZE)
                        ## width and height of snake/rectangle, xvelocity and yvelocity matches width and height
                        xvelocity = w = h = SIZE
                        yvelocity = 0

            #Call Button Function
            drawButton("images/restart.png",300,100,DIMENSION/2,DIMENSION/2)

            readfile = open("save/highscore.txt", "r")
            highscore = readfile.readline()
            if(tail > int(highscore)):
                writefile = open("save/highscore.txt","w")
                writefile.write(str(tail))
                writefile.close()
            readfile.close()

            #Display Update()
            pygame.display.update()
