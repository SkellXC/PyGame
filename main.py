
import pygame
pygame.init()

winWidth, winHeight = 500, 480
window = pygame.display.set_mode((winWidth,winHeight))# Creates the window
pygame.display.set_caption('Main Window')# Window name

x, y = 50,400# Place where the character is created
width,height = 64,64# Character size
velo = 5# Character velocity

run:bool = True
jump:bool = False
jumpHeight:int = 10
left:bool = False
right:bool = False
walkCount = 0
clock = pygame.time.Clock()


walkRight:list = [pygame.image.load('sprites/R1.png'), pygame.image.load('sprites/R2.png'), pygame.image.load('sprites/R3.png'), pygame.image.load('sprites/R4.png'), pygame.image.load('sprites/R5.png'), pygame.image.load('sprites/R6.png'), pygame.image.load('sprites/R7.png'), pygame.image.load('sprites/R8.png'), pygame.image.load('sprites/R9.png')]
walkLeft:list = [pygame.image.load('sprites/L1.png'), pygame.image.load('sprites/L2.png'), pygame.image.load('sprites/L3.png'), pygame.image.load('sprites/L4.png'), pygame.image.load('sprites/L5.png'), pygame.image.load('sprites/L6.png'), pygame.image.load('sprites/L7.png'), pygame.image.load('sprites/L8.png'), pygame.image.load('sprites/L9.png')]
bg = pygame.image.load('sprites/bg.jpg')
char = pygame.image.load('sprites/standing.png')


def redrawGameWindow():
    global walkCount
    window.blit(bg, (0,0))# Draws the background

    if walkCount + 1 >= 27:
        walkCount = 0
    
    if left:
        window.blit(walkLeft[walkCount//3],(x,y))
        walkCount += 1
    elif right:
        window.blit(walkRight[walkCount//3],(x,y))
        walkCount += 1
    else:
        window.blit(char, (x,y))

    pygame.display.update()



while run:# Mainloop
    #pygame.time.delay(37)# Equivilent of a tick in mc. In MS.
    clock.tick(27)# 27 fps
    # Events = Keyboard/mouse etc

    for event in pygame.event.get(): # Keyboard/mouse movements that have occured in this tick
        if event.type == pygame.QUIT:
            run = False# Lets the game get closed

    keys = pygame.key.get_pressed() # Find out what key has been pressed

    if keys[pygame.K_LEFT] and x > velo:# Ensure player can't exit the boundry
        x -= velo# Moves it by 5. same as c#
        left,right = True, False
    
    elif keys[pygame.K_RIGHT] and x < winWidth - width - velo:
        # Character would otherwise be just 1 character outside the width
        x += velo
        right,left = True, False
    else:
        right,left = False, False
        walkCount = 0
    if (not jump):
        if keys[pygame.K_SPACE]:
            jump = True
        '''Uses a quadratic equation, f(k), to move the character in an arc
        jump is 20 iterations long. for each iteration N, move f(N) positions in the y
        direction. For the first half, move it upwards and in the second half move it back
        down (hence why neg becomes negative)
        '''

    else:
        if jumpHeight >= -10:
            #neg = 1 if jumpHeight >= -20 else -1
            neg = 1
            if jumpHeight < 0:
                neg = -1
            y -= (jumpHeight **2) * 0.25 * neg
            jumpHeight -=1
        else:
            jump = False
            jumpHeight = 10
            
    redrawGameWindow()

pygame.quit()
