#!/usr/bin/env python3
# Copyright (c) MIT 
# Lucas Zunho <lucaszunho17@gmail.com>

from loveiswar import sprite_object
import sys
import pygame

# Adicionando system path
sys.path.insert(0, '../loveiswar')

# obj.
spritesheet = sprite_object.SpriteSheet('./assets/', (64, 64))
spritesheet.load_sprites()

# pygame context
white = (255, 64, 64)
screen = pygame.display.set_mode((spritesheet.sprites_res))

c = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == pygame.K_BACKSPACE or event.type == pygame.K_RIGHT:
            c += 1
        elif event.type == pygame.K_RETURN or event.type == pygame.K_LEFT:
            c -= 1
    screen.fill((white))
    screen.blit(spritesheet.images[c], (0, 0))
    pygame.display.flip()