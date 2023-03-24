#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:57:59 2023

@author: lzunho-afk
"""

import pygame
import sys
from pygame.locals import *

import settings
import map
import player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.RES, pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.dt = 1
        self.newGame()
        
    def newGame(self):
        self.map = map.Map(self)
        self.player = player.Player(self)
    
    def update(self):
        self.player.update()
        pygame.display.flip()
        self.dt = self.clock.tick(settings.FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()
        
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