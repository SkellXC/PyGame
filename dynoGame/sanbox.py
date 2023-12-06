import pygame
pygame.init()
class image: pass  # For type hinting

winWidth, winHeight = 572, 250
window = pygame.display.set_mode((winWidth, winHeight))  # Creates the window
pygame.display.set_caption('Dino Game')  # Window name

clock = pygame.time.Clock()

bg = pygame.image.load('dynoGame/sprites/bg1.png')
run1 = pygame.image.load('dynoGame/sprites/run1.png')
run1:image = pygame.transform.scale(run1, (46, 46))  # Resizes the image
run2 = pygame.image.load('dynoGame/sprites/run2.png')
run2:image = pygame.transform.scale(run2, (46, 46))

x, y = 10, 80
dino:image = run1
swap:bool = False
run:bool = True
jump:bool = False
jumpCount:int = 9

def jump_function():
    global y, jumpCount, jump
    if jumpCount >= -9:
        neg = 1
        if jumpCount < 0:
            neg = -1
        y -= (jumpCount ** 2) * 0.25 * neg
        #print(y)
        jumpCount -= 1
    else:
        jump = False
        jumpCount = 9
    

while run:
    clock.tick(30)  # 27 fps
    # Events = Keyboard/mouse, etc.
    window.blit(bg, (0, 0))  # Draws the background
    swap = not swap
    dino = run1 if swap else run2
    window.blit(dino, (x, y))

    for event in pygame.event.get():  # Keyboard/mouse movements that have occurred in this tick
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            run = False  # Lets the game get closed
        elif keys[pygame.K_SPACE] and not jump:
            jump = True

    if jump:
        jump_function()

    pygame.display.update()