# My First PyGame, Camren Johnson, 11/29/21 2:02pm, v0.9

import pygame, sys
from pygame.locals import * 

# Start PyGame 
pygame.init()


# Setup our window. 1 
windowSurface = pygame.display.set_mode((500,400),0, 32)
pygame.display.set_caption('Hello, world!')

# Setup Colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (225, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FLAMINGOPINK = (168, 50, 117)


# Setup font.
basicFont = pygame.font.SysFont(None, 48)

# Setup text
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect= text.get_rect()
textRect.centery + windowSurface.get_rect().centery

# Fill background color 
windowSurface.fill(FLAMINGOPINK)

# Draw a polygon onto the screen.
pygame.draw.polygon(windowSurface, GREEN,((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

#Draw lines on the screen.
pygame.draw.line(windowSurface,BLUE, (0,150), (150,0), 1)
pygame.draw.line(windowSurface,RED, (60,0), (120,0), 4)
pygame.draw.line(windowSurface,WHITE, (75,60), (60,75), 2)

# Draw a circle.
pygame.draw.circle(windowSurface,BLACK, (300, 50), 20, 0)

# Draw an ellipse 
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80),1)

# Draw a rectangle
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# Create Pixel Array
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLUE 
del pixArray

# Draw the text onto the surface.
windowSurface.blit(text, textRect)

#Update Pygame Display
pygame.display.update()

# Run game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            sys.exit()



