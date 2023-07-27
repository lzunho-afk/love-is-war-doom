#!/usr/bin/env python3
# Copyright (c) MIT
# Lucas Zunho <lucaszunho17@gmail.com>

import pygame
import sys
from pygame.locals import *

import settings
import map
import player
import raycasting
import object_renderer
import sprite_object

class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(settings.RES, pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.dt = 1
        self.newGame()
        
    def newGame(self):
        self.map = map.Map(self)
        self.player = player.Player(self)
        self.object_renderer = object_renderer.ObjectRenderer(self)
        self.raycasting = raycasting.RayCasting(self)
        self.static_sprite = sprite_object.SpriteObject(self)
    
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.static_sprite.update()
        pygame.display.flip()
        self.dt = self.clock.tick(settings.FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
    def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()
        #self.map.draw()
        #self.player.draw()
        
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
    
    def run(self):
        while True:
            self.checkEvents()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
