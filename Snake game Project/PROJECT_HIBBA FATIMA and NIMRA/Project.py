import pygame
import random, sys
from pygame.locals import *
import time

red = (255,0,0)
black = (0,0,0)
darkGray = (169,169,169) 
gray = (128,128,128)
green = (0,255,0)
green01 = (0,150,0)
red01 =(200,0,0)

screenX = 600
screenY = 600



pygame.init()
pygame.mixer.music.load("snake.wav")
sound01 = pygame.mixer.Sound("snake_music.wav")
imageH=pygame.image.load("nibbles1.jpg")
imageH = pygame.transform.scale(imageH,(600,600))
text = pygame.image.load("snake2.jpg")
text = pygame.transform.scale(text,(600,600))
s = pygame.display.set_mode((600,600))

def screen(screenX,screenY):
    s=pygame.display.set_mode((screenX, screenY))
    pygame.display.set_caption('SNAKE')
    pygame.display.update()
    return s


        
def message(msg,color,x,y,textSize,textFont):  
    font = pygame.font.SysFont(textFont,textSize)
    sText = font.render(msg,True,color)
    s.blit(sText,[x,y])

def button(msg,x,y,w,h,x1,y1,ic,ac,action=None):
    mouseP = pygame.mouse.get_pos()
    cliks = pygame.mouse.get_pressed()
    if x+w > mouseP[0] > x and y+h > mouseP[1] > y:
        play = pygame.draw.rect(s,ac,(x,y,w,h))
        if cliks[0] ==1 and action != None:
            if action == "play":
                level01()
            elif action == "instruct":
                instruct()
            elif action == "easy":
                gameeasy()
            elif action == "medium":
                gamemedium()
            elif action == "hard":
                gamehard()
            elif action == "back":
                start()
            elif action == "play01":
                level01()
            elif action == "quit":
                quit01()
    else:
        play = pygame.draw.rect(s,ic,(x,y,w,h))
    diplay01 = message(msg,black,x1,y1,30,"Arial")

def quit01():
    sys.exit(0)

def pause():
	pause = False
	while not pause:
		for e in pygame.event.get():
			if e.type == QUIT:
				quit()
			if e.type == KEYDOWN:
				if e.key == K_c:
					pause = True
		s.fill((255,255,255))
		s.blit(text,(0,0))
		message("Paused!",black,150,100,70,"Broadway")
		message("Press \"C\" to continue!",black,10,300,30,"Arial")
		button10 = button("Select Level",40,400,150,50,50,405,(255,165,0),(240,230,140),"pause")
		button11 = button("Quit",40,500,150,50,90,505,red01,red,"quit")
		pygame.display.update()
def snakeDraw(snake,snakeList): 

    snake.fill((255, 0, 0))
    for i in snakeList:
        s.blit(snake,(i[0],i[1]))



def gameeasy():

    pygame.mixer.Sound.stop(sound01)  
    pygame.mixer.music.play(-1)
    snakeList=[] #stores all the coordinates of the snake
    dirs = 'right' 
    score = 0
    snakeLength = 2 
    lives = 3
    blueApples = 0    
    FPS = 10  #changes to increase the speed of the snake
    apple1posX = round(random.randrange(0, 590)/10.0)*10.0
    apple1posY = round(random.randrange(40, 590)/10.0)*10.0
    apple1image = pygame.Surface((10, 10))
    apple1image.fill((0, 0, 255))  #colour fill to the apple

    snake = pygame.Surface((13, 15))
    snake.fill((0, 0, 43))
    x = 300
    y = 300
    s.blit(snake,(x,y))
    f = pygame.font.SysFont('Arial', 20)
    clock = pygame.time.Clock()
    over = False
    while True:
        clock.tick(FPS)
        appleList = [] #stores the coordinates of apple and the compares them with coordinates of snake

        while over != False: #executes when snake crashes
            s.fill((0,0,0))
            s.blit(text,(0,0))
            message('Game Over!',black,110,50,60,"Broadway")
            message('Your Score:'+str(score),black,50,300,40,"Arial")
            button07 = button("Play Again",85,400,140,50,95,405,green01,green,"play01")
            button08 = button("Quit",85,500,140,50,130,505,red01,red,"quit")
            pygame.display.update()

            for e in pygame.event.get(): #quit function for gameover screen
                if e.type == QUIT:
                    sys.exit(0)
                    over = False
                

        

        for e in pygame.event.get():
            if e.type == QUIT: #quit function for game screen
                sys.exit(0)
                over = False

            elif e.type == KEYDOWN: #basic key controls of snake
                if e.key == K_UP and dirs != "downwards" :
                    
                    dirs = "upwards"
                elif e.key == K_DOWN and dirs != "upwards" :
                    
                    dirs = "downwards"
                elif e.key == K_LEFT  and dirs != "right" :
                    
                    dirs = "left"
                elif e.key == K_RIGHT and dirs !="left":
                    
                    dirs = "right"
                elif e.key == K_p:
                	pause()
        
        if dirs == "right":
            x+=10
            
        if dirs == "left":
            x-=10
            
        if dirs == "upwards" :
            y-=10
            
        if dirs == "downwards" :
            y+=10
        
        snakeHead = []  
        s.fill((230,220,255))       
        s.blit(apple1image,(apple1posX,apple1posY))

        snakeHead.append(x)
        snakeHead.append(y)       
        snakeList.append(snakeHead)
        if len(snakeList)>snakeLength:
            del(snakeList[0])

        for j in snakeList[:-1]:
            if j == snakeHead:
                lives -=1
        
        if lives==0:
            over = True     


        snakeDraw(snake,snakeList)
#In easy mode, boudaries don't crash the snake
        #snake appears from the other end
        if x>600:   
            x=0
            s.blit(snake,(x,y))
        elif x<0:
            x=600
            s.blit(snake,(x,y))
        elif y>600:
            y=0
            s.blit(snake,(x,y))
        elif y<0:
            y = 600
            s.blit(snake,(x,y))
            
#if snake coordinates are same as apple coordinates new apple appears
        if apple1posY >= y and apple1posY <= y+15:
            if apple1posX >= x and apple1posX <= x+13:
                
                apple1posX = round(random.randrange(0, 590)/10.0)*10.0
                apple1posY = round(random.randrange(40, 590)/10.0)*10.0
                appleList.append(apple1posX)
                appleList.append(apple1posY)
#if the new apple coordinates are similar to those of the present coordinates then new coordinates are chosen
                coord = True
                while coord:
                    for j in snakeList[:-1]:
                        if j == appleList:
                            apple1posX = round(random.randrange(0, 590)/10.0)*10.0
                            apple1posY = round(random.randrange(40, 590)/10.0)*10.0
                        else:
                            coord = False



                s.blit(apple1image,(apple1posX,apple1posY))
                score+=1
                snakeLength += 2
                blueApples +=1
            if blueApples % 3 == 0 and blueApples != 0:
                #speed of snake increases for every 3 apples eaten
                FPS += 2
                clock.tick(FPS)
                blueApples += 1
                
#top of screen displays number of lives, score and level name
        message("EASY",(255,165,0),250,0,40,"Arial")
        if lives == 3:
            message('lives:'+str(lives),(0,165,0),500,0,40,"Arial")
        if lives == 2:
            message('lives:'+str(lives),(255,165,0),500,0,40,"Arial")
        if lives == 1:
            message('lives:'+str(lives),(165,0,0),500,0,40,"Arial")
        message('Your Score:'+str(score),(255,165,0),0,0,40,"Arial")
        pygame.display.update()


    pygame.quit()
    quit()

#medium level
def gamemedium():
    pygame.mixer.Sound.stop(sound01)   #background music
    pygame.mixer.music.play(-1)
    snakeList=[]  #list to append snake coordinates
    dirs = 'right'
    score = 0
    snakeLength = 2 # a variable to control snake length
    lives = 2
    blueApples = 0  #a variable to control snake speed
    FPS = 10    

    apple1posX = round(random.randrange(0, 590)/10.0)*10.0
    apple1posY = round(random.randrange(40, 590)/10.0)*10.0
    apple1image = pygame.Surface((10, 10))
    apple1image.fill((0, 0, 255))


    snake = pygame.Surface((13, 15))
    snake.fill((0, 0, 43))
    x = 300
    y = 300
    s.blit(snake,(x,y))
    f = pygame.font.SysFont('Arial', 20)
    clock = pygame.time.Clock()
    over = False
    while True:
        clock.tick(FPS)
    
        appleList = []
        #code for game over screen
        while over != False:
            s.fill((0,0,0))
            s.blit(text,(0,0))
            message('Game Over!',black,110,50,60,"Broadway")
            message('Your Score:'+str(score),black,50,300,40,"Arial") #prints the final score
            button07 = button("Play Again",85,400,140,50,95,405,green01,green,"play01") #button that calls level select screen again
            button08 = button("Quit",85,500,140,50,130,505,red01,red,"quit")
    
            pygame.display.update()
#keyboard keys "q" and "p" can be used for quiting and playing again
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit(0)
                    over = False
                elif e.type == KEYDOWN:
                    if e.key == K_q: 
                        sys.exit(0)
                        over = False
                    elif e.key == K_p:
                        pygame.mixer.music.stop()
                        level01()

        
#close button of the window closes the game 
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
                over = False
#basic directional controls of snake
            elif e.type == KEYDOWN:
                if e.key == K_UP and dirs != "downwards" :
                    
                    dirs = "upwards"
                elif e.key == K_DOWN and dirs != "upwards" :
                    
                    dirs = "downwards"
                elif e.key == K_LEFT  and dirs != "right" :
                    
                    dirs = "left"
                elif e.key == K_RIGHT and dirs !="left":
                    
                    dirs = "right"
                elif e.key == K_p:
                	pause()

        #depending on direction the coordinates change and help the snake move forward
        if dirs == "right":
            x+=10
            
        if dirs == "left":
            x-=10
            
        if dirs == "upwards" :
            y-=10
            
        if dirs == "downwards" :
            y+=10

        snakeHead = [] #list to store the coordinates of the snake head  
        s.fill((230,220,255))       
        s.blit(apple1image,(apple1posX,apple1posY))


        snakeHead.append(x) 
        snakeHead.append(y)       
        snakeList.append(snakeHead)
        if len(snakeList)>snakeLength:
            del(snakeList[0])

        for j in snakeList[:-1]:    #checks if the snake has bitten itself
            if j == snakeHead:
                lives -= 1

        if lives == 0: 
            over = True  #if number of lives is 0 then game over code executes

        snakeDraw(snake,snakeList)
            
        if x>=600 or x<0 or y>=600 or x<0:
            over = True     #if snake crashes with the boundary game overs
#checks if snake collides with apple
        if apple1posY >= y and apple1posY <= y+15:
            if apple1posX >= x and apple1posX <= x+13:
                #new random coordinates of apple
                apple1posX = round(random.randrange(0, 590)/10.0)*10.0  #"/10.0)*10.0" this is done in order that apple coordinates are always a multiple of 10  
                apple1posY = round(random.randrange(40, 590)/10.0)*10.0
                appleList.append(apple1posX)
                appleList.append(apple1posY)
#checks if apple coordinates are similar to current coordinates of snake
                coord = True
                while coord:
                    for j in snakeList[:-1]:
                        if j == appleList:
                            apple1posX = round(random.randrange(0, 590)/10.0)*10.0
                            apple1posY = round(random.randrange(40, 590)/10.0)*10.0
                        else:
                            coord = False
                s.blit(apple1image,(apple1posX,apple1posY))
                score+=1
                snakeLength += 2
                blueApples +=1
#speed increases for every three apples
            if blueApples % 3 == 0 and blueApples != 0:
                    FPS += 2
                    clock.tick(FPS)
                    blueApples += 1
#top of screen displays number of lives, score and level name
                
        message("MEDIUM",(255,165,0),250,0,40,"Arial")
        if lives == 2:                  
            message('lives:'+str(lives),(0,165,0),500,0,40,"Arial") 
        if lives == 1:
            message('lives:'+str(lives),(165,0,0),500,0,40,"Arial") 

        message('Your Score:'+str(score),(255,165,0),0,0,40,"Arial")
        pygame.display.update()
        

    pygame.quit()
    quit()



#hard level
def gamehard():
    pygame.mixer.Sound.stop(sound01)  #backgroud music
    pygame.mixer.music.play(-1)
    snakeList=[]
    dirs = 'right'
    score = 0
    snakeLength = 2

    screenX = 600
    screenY = 600

    screen=pygame.display.set_mode((screenX, screenY))
    pygame.display.set_caption('SNAKE')
    appleList01 = []
    appleList02 = []
    appleList03 = []

#three apples generated at randim coordinates
    apple1posX = round(random.randrange(0, screenX-10)/10.0)*10.0
    apple1posY = round(random.randrange(40, screenY-10)/10.0)*10.0
    apple1image = pygame.Surface((10, 10))
    apple1image.fill((0, 0, 255))


    apple2posX = round(random.randrange(0, screenX-10)/10.0)*10.0
    apple2posY = round(random.randrange(40, screenY-10)/10.0)*10.0
    apple2image = pygame.Surface((10, 10))
    apple2image.fill((0, 255, 0))
    

    apple3posX = round(random.randrange(0, screenX-10)/10.0)*10.0
    apple3posY = round(random.randrange(40, screenY-10)/10.0)*10.0
    apple3image = pygame.Surface((10, 10))
    apple3image.fill((255, 0, 255))


    snake = pygame.Surface((13, 15))
    snake.fill((0, 0, 43))
    x = 300
    y = 300
    screen.blit(snake,(x,y))
    f = pygame.font.SysFont('Arial', 20)
    clock = pygame.time.Clock()
    over = False
    blueApples = 0

    FPS = 10
    while True:
        clock.tick(FPS)
#screen size changes each time a wrong apple is eaten
        screen=pygame.display.set_mode((screenX, screenY))
        pygame.display.set_caption('SNAKE')

#game over code
        while over != False:
            s = pygame.display.set_mode((600,600))
            s.fill((255,255,255))
            s.blit(text,(0,0))
            message("Game Over!",black,150,150,60,'Broadway')
            message("Press \"P\" to Play and \"Q\" to Quit!",black,10,250,40,'Arial')
            pygame.display.update()
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit(0)
#game quits with "q" and plays again with "p" keys on keyboard
                if e.type == KEYDOWN:
                    if e.key == K_p:
                        level01()
                    elif e.key == K_q:
                        sys.exit(0)

        
#game quits with close button of screen
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
                over = False
#basic directional controls of snake
            elif e.type == KEYDOWN:
                if e.key == K_UP and dirs != "downwards" :
                    
                    dirs = "upwards"
                elif e.key == K_DOWN and dirs != "upwards" :
                    
                    dirs = "downwards"
                elif e.key == K_LEFT  and dirs != "right" :
                    
                    dirs = "left"
                elif e.key == K_RIGHT and dirs !="left":
                    
                    dirs = "right"
                elif e.key == K_p:
                	pause()

#snake moves forward according to value of dirs (direction variable)
        if dirs == "right":
            x+=10
            
        if dirs == "left":
            x-=10
            
        if dirs == "upwards" :
            y-=10
            
        if dirs == "downwards" :
            y+=10
        
        snakeHead = []  
        screen.fill((230,220,255))
#three apples blit at random places
        screen.blit(apple1image,(apple1posX,apple1posY))
        screen.blit(apple2image,(apple2posX,apple2posY))
        screen.blit(apple3image,(apple3posX,apple3posY))

        snakeHead.append(x)
        snakeHead.append(y)       
        snakeList.append(snakeHead)
#controls length of snake
        if len(snakeList)>snakeLength:
            del(snakeList[0])

        for j in snakeList[:-1]:
            if j == snakeHead:
                over = True


        snakeDraw(snake,snakeList)
#snake crashes with boundary game overs            
        if x>=screenX or x<0 or y>=screenY or x<0:
            over = True


#snakes collision with apples detected
        if apple1posY >= y and apple1posY <= y+15:
            if apple1posX >= x and apple1posX <= x+13:
                if screenX < 600 and screenY < 600:
                    screenX += 20
                    screenY += 20
                
                apple1posX = round(random.randrange(0, screenX-10)/10.0)*10.0
                apple1posY = round(random.randrange(40, screenY-10)/10.0)*10.0
                appleList01.append(apple1posX)
                appleList01.append(apple1posY)
                coord = True
                while coord:
                    for j in snakeList[:-1]:
                        if j == appleList01:
                            apple1posX = round(random.randrange(0, 590)/10.0)*10.0
                            apple1posY = round(random.randrange(40, 590)/10.0)*10.0
                        else:
                            coord = False
                screen.blit(apple1image,(apple1posX,apple1posY))
                score+=1
                snakeLength += 2
                                
                apple2posX = round(random.randrange(0, screenX-10)/10.0)*10.0
                apple2posY = round(random.randrange(40, screenY-10)/10.0)*10.0
                appleList02.append(apple2posX)
                appleList02.append(apple2posY)
                coord = True
                while coord:
                    for j in snakeList[:-1]:
                        if j == appleList02:
                            apple1posX = round(random.randrange(0, 590)/10.0)*10.0
                            apple1posY = round(random.randrange(40, 590)/10.0)*10.0
                        else:
                            coord = False
                screen.blit(apple2image,(apple2posX,apple2posY))

                apple3posX = round(random.randrange(0, screenX-10)/10.0)*10.0
                apple3posY = round(random.randrange(40, screenY-10)/10.0)*10.0
                appleList03.append(apple3posX)
                appleList03.append(apple3posY)
                coord = True
                while coord:
                    for j in snakeList[:-1]:
                        if j == appleList03:
                            apple1posX = round(random.randrange(0, 590)/10.0)*10.0
                            apple1posY = round(random.randrange(40, 590)/10.0)*10.0
                        else:
                            coord = False
                screen.blit(apple3image,(apple3posX,apple3posY))

                blueApples += 1

                if blueApples % 3 == 0 and blueApples != 0:
                    FPS += 3
                    clock.tick(FPS)
                    blueApples += 1
                    
            

        
        if apple2posY >= y and apple2posY <= y+15:
            if apple2posX >= x and apple2posX <= x+13:
                #screen size variables
                screenX -= 20
                screenY -= 20
                apple1posX = round(random.randrange(0, screenX-10)/10.0)*10.0
                apple1posY = round(random.randrange(40, screenY-10)/10.0)*10.0
                appleList01.append(apple1posX)
                appleList01.append(apple1posY)
                coord = True
                while coord:
                    for j in snakeList[:-1]:
                        if j == appleList01:
                            apple1posX = round(random.randrange(0, 590)/10.0)*10.0
                            apple1posY = round(random.randrange(40, 590)/10.0)*10.0
                        else:
                            coord = False
                screen.blit(apple1image,(apple1posX,apple1posY))

                                
                apple2posX = round(random.randrange(0, screenX-10)/10.0)*10.0
                apple2posY = round(random.randrange(40, screenY-10)/10.0)*10.0
                appleList02.append(apple2posX)
                appleList02.append(apple2posY)
                coord = True
                while coord:
                    for j in snakeList[:-1]:
                        if j == appleList02:
                            apple1posX = round(random.randrange(0, 590)/10.0)*10.0
                            apple1posY = round(random.randrange(40, 590)/10.0)*10.0
                        else:
                            coord = False
                screen.blit(apple2image,(apple2posX,apple2posY))

                apple3posX = round(random.randrange(0, screenX-10)/10.0)*10.0
                apple3posY = round(random.randrange(40, screenY-10)/10.0)*10.0
                appleList03.append(apple3posX)
                appleList03.append(apple3posY)
                coord = True
                while coord:
                    for j in snakeList[:-1]:
                        if j == appleList03:
                            apple1posX = round(random.randrange(0, 590)/10.0)*10.0
                            apple1posY = round(random.randrange(40, 590)/10.0)*10.0
                        else:
                            coord = False
                screen.blit(apple3image,(apple3posX,apple3posY))
                del(snakeList[0])
                snakeLength -=1
                score -= 1
                
            
                

                


        if apple3posY >= y and apple3posY <= y+15:
            if apple3posX >= x and apple3posX <= x+13:
                #screen size variables
                screenX -= 20
                screenY -= 20
                apple1posX = round(random.randrange(0, screenX-10)/10.0)*10.0
                apple1posY = round(random.randrange(40, screenY-10)/10.0)*10.0
                appleList01.append(apple1posX)
                appleList01.append(apple1posY)
                coord = True
                while coord:
                    for j in snakeList[:-1]:
                        if j == appleList01:
                            apple1posX = round(random.randrange(0, 590)/10.0)*10.0
                            apple1posY = round(random.randrange(40, 590)/10.0)*10.0
                        else:
                            coord = False
                screen.blit(apple1image,(apple1posX,apple1posY))

                                
                apple2posX = round(random.randrange(0, screenX-10)/10.0)*10.0
                apple2posY = round(random.randrange(40, screenY-10)/10.0)*10.0
                appleList02.append(apple2posX)
                appleList02.append(apple2posY)
                coord = True
                while coord:
                    for j in snakeList[:-1]:
                        if j == appleList02:
                            apple1posX = round(random.randrange(0, 590)/10.0)*10.0
                            apple1posY = round(random.randrange(40, 590)/10.0)*10.0
                        else:
                            coord = False
                screen.blit(apple2image,(apple2posX,apple2posY))

                apple3posX = round(random.randrange(0, screenX-10)/10.0)*10.0
                apple3posY = round(random.randrange(40, screenY-10)/10.0)*10.0
                appleList03.append(apple3posX)
                appleList03.append(apple3posY)
                coord = True
                while coord:
                    for j in snakeList[:-1]:
                        if j == appleList03:
                            apple1posX = round(random.randrange(0, 590)/10.0)*10.0
                            apple1posY = round(random.randrange(40, 590)/10.0)*10.0
                        else:
                            coord = False
                screen.blit(apple3image,(apple3posX,apple3posY))
                del(snakeList[0])
                snakeLength -= 1
                score -= 1
                

        if score<0 or len(snakeList)==0:
            over=True

        message("EAT BLUE APPLE!",(0,0,200),380,10,30,"Arial")  
        message("HARD",(255,165,0),250,0,40,"Arial")
        if score == -1:
            score = 0       
        message('Your Score:'+str(score),(255,165,0),0,0,40,"Arial")

        pygame.display.update()


    pygame.quit()
    
    quit()


def level01():
    s = screen(screenX,screenY)
    level = True
    clock = pygame.time.Clock()
    timer = 170
    while level:
        pygame.mixer.Sound.play(sound01)
        s.fill((0,0,0))
        s.blit(text,(0,0))
        for m in pygame.event.get():
            if m.type == QUIT:
                sys.exit(0)
    
        mText = message("Select Level",black,80,100,70,"Broadway")
        mouseP = pygame.mouse.get_pos()
        button03 = button("Easy",50,200,100,50,70,212,(255,165,0),(240,230,140),"easy")
        button04 = button("Medium",50,300,100,50,55,312,(255,165,0),(240,230,140),"medium")
        button05 = button("Hard",50,400,100,50,70,412,(255,165,0),(240,230,140),"hard")
        
        
        pygame.display.update()
        clock.tick(15)

def instruct():
    s=pygame.display.set_mode((600, 600))
    pygame.display.set_caption('SNAKE')
    inst = True
    clock = pygame.time.Clock()
    while inst:
        pygame.mixer.Sound.play(sound01)
        s.fill((255,255,255))
        s.blit(text,(0,0))
        for m in pygame.event.get():
            if m.type == QUIT:
                sys.exit(0)
        message("INSTRUCTIONS",black,120,20,40,"Arial Black")
        message("1. Be careful for boundaries in \"MEDIUM and HARD\" levels",black,30,80,25,"Arial")
        message("2. Look for \"BLUE APPLES\" in hard level.",black,30,120,25,"Arial")
        message("3. In hard level,\"EATING WRONG APPLE DECREASES",black,30,155,25,"Arial")
        message("    MAZE SIZE\"",black,30,190,25,"Arial")
        button05 = button("Back",20,500,100,50,40,510,(255,165,0),(240,230,140),"back")
        pygame.display.update()
        clock.tick(15)

def start():
    s = screen(screenX,screenY)
    pygame.mixer.Sound.play(sound01)
    game = True
    clock = pygame.time.Clock()
    while game:
        pygame.mixer.Sound.play(sound01)
        s.fill((0,0,0))
        s.blit(imageH,(0,0))
        for l in pygame.event.get():
                if l.type == QUIT:
                        sys.exit(0)

        mouseP = pygame.mouse.get_pos()
        button01= button("Play",85,350,140,50,130,360,green01,green,"play")
        button02= button("Instructions",85,450,140,50,90,465,red01,red,"instruct")


        pygame.display.update()
    
start()
