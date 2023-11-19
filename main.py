import pygame
pygame.init()

winWidth, winHeight = 500, 500

window = pygame.display.set_mode((winWidth,winHeight))# Creates the window

pygame.display.set_caption('Main Window')# Window name

x, y = 50,50# Place where the character is created
width,height = 40,60# Character size
velo = 5# Character velocity

run = True
jump = False
jumpHeight = 10

while run:# Mainloop
    pygame.time.delay(50)# Equivilent of a tick in mc. In MS.
    # Events = Keyboard/mouse etc

    for event in pygame.event.get(): # Keyboard/mouse movements that have occured in this tick
        if event.type == pygame.QUIT:
            run = False# Lets the game get closed

    keys = pygame.key.get_pressed() # Find out what key has been pressed

    if keys[pygame.K_LEFT] and x > velo:# Ensure player can't exit the boundry
        x -= velo# Moves it by 5. same as c#
    if keys[pygame.K_RIGHT] and x < winWidth - width - velo:
        # Character would otherwise be just 1 character outside the width
        x += velo
    if (not jump):
            
        if keys[pygame.K_UP] and y > velo:
            y -= velo
        if keys[pygame.K_DOWN] and y < 500 - height - velo:
            y += velo
        if keys[pygame.K_SPACE]:
            jump = True
        '''Uses a quadratic equation, f(k), to move the character in an arc
        jump is 20 iterations long. for each iteration N, move f(N) positions in the y
        direction. For the first half, move it upwards and in the second half move it back
        down (hence why nec becomes negative)
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
            
    window.fill((0,0,0)) #Gets rid of the old stuff?
    pygame.draw.rect(window, (255,0,0), (x,y,width,height))# Creates a rectangle. More in website
    pygame.display.update()# Refresh screen. Same as C#

pygame.quit()
