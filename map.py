#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:58:37 2023

@author: lzunho-afk
"""

import pygame
import settings
from math import floor

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
        
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, val in enumerate(row):
                if val:
                    self.world_map[(i, j)] = val
                    
    def draw(self):
        [pygame.draw.rect(self.game.screen, 'darkgray', (
            pos[0] * floor(settings.WIDTH / 16),
            pos[1] * floor(settings.HEIGHT / 9), 
            floor(settings.WIDTH / 16), 
            floor(settings.HEIGHT / 9)
        ), 2)
         for pos in self.world_map]
        