# My First PyGame, Camren Johnson, 11/29/21 1:59pm, v0.0

import pygame, sys
from pygame.locals import * 

# Start PyGame 
pygame.init()

# Setup our window. 1 
windowSurface = pygame.set_mode((500,400), 0, 32)
pygame.display.set_caption('Hello, world!')

# Setup Colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (225, 0, 0)
GREEN = (0, 255, 0
BLUE = (0, 0, 255)