import pygame
import sys
from pygame.locals import *

pygame.init()


DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
TRAN_BLUE = (0, 0, 255, 0)
AQUA = (0, 255, 255)
PINK = (255, 153, 255)

DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0),
                    (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, TRAN_BLUE, (120, 60), (60, 120), 1)
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (170, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.circle(DISPLAYSURF, AQUA, (380, 70), 40, 5)
pygame.draw.ellipse(DISPLAYSURF, BLUE, (300, 260, 40, 80), 1)
pygame.draw.ellipse(DISPLAYSURF, YELLOW, (380, 260, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 200, 100))
pygame.draw.line(DISPLAYSURF, AQUA, (360, 260), (360, 340), 1)
pygame.draw.rect(DISPLAYSURF, PINK, (50, 100, 100, 100), 0)

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
pixObj[380][70] = PINK
del pixObj


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
