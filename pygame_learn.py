import pygame

background_image_filename = '1000*1000.png'
mouse_image_filename = '100*100px.png'

from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Glovoice Control Panel")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background,(0,0))

    x,y = pygame.mouse.get_pos()

    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2

    screen.blit(mouse_cursor,(x,y))

    pygame.display.update()
