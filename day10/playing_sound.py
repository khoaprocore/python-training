import pygame
import sys
from pygame.locals import *
import time

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World")
soundObj = pygame.mixer.Sound("beeps.wav")
soundObj.play()
time.sleep(1)
soundObj.stop()
pygame.mixer.music.load("TLS.mp3")
pygame.mixer.music.play(-1, 0.0)
# pygame.mixer.music.stop()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
