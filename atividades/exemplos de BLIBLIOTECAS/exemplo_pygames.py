import pygame
from pygame.locals import *
from sys import exit


pygame.init()

largura = 800
altura = 500
Tela = pygame.display.set_mode((largura,altura))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
