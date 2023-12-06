import pygame
pygame.init()
class image: pass# For type hinting
winWidth, winHeight = 572, 250
window = pygame.display.set_mode((winWidth,winHeight))# Creates the window
pygame.display.set_caption('Dino Game')# Window name

clock = pygame.time.Clock()

bg = pygame.image.load('dynoGame/sprites/bg1.png')
run1 = pygame.image.load('dynoGame/sprites/run1.png')
run1:image = pygame.transform.scale(run1, (46,46))# Resizes the image
run2 = pygame.image.load('dynoGame/sprites/run2.png')
run2:image = pygame.transform.scale(run2, (46,46))

x, y = 10,80
dino:image = run1
swap:bool = False
run:bool = True
jump:bool = False
jumpCount:int = 10
def jump_func(is_jumping, jump_count,y):
    if is_jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10
    return is_jumping, jump_count, y

'''
for 10 iterations.
Each iteration. Increment y by f(y) in arc.
y\ =\ \left(-x-2\right)\left(x-2\right)
y = x^2 + 4x + 4


'''
def jumpUp(ypos):
    #y^2 + 0.25y
    pass

while run:
    clock.tick(30)# 27 fps
    # Events = Keyboard/mouse etc
    window.blit(bg, (0,0))# Draws the background
    swap = not swap
    dino = run1 if swap else run2
    window.blit(dino, (x,y))

    for event in pygame.event.get(): # Keyboard/mouse movements that have occured in this tick
        keys = pygame.key.get_pressed() 
        if event.type == pygame.QUIT:
            run = False# Lets the game get closed
        elif keys[pygame.K_SPACE]:
            jump = True
            jump, jumpCount, y = jump_func(jump, jumpCount,y)
            

    pygame.display.update()