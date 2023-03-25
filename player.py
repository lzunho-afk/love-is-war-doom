#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:58:10 2023

@author: lzunho-afk
"""

import settings
import pygame
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = settings.PLAYER_POS[0], settings.PLAYER_POS[1]
        self.angle = settings.PLAYER_ANGLE
        
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = settings.PLAYER_SPEED * self.game.dt
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pygame.K_d]:
            dx += -speed_sin
            dy += speed_cos
            
        self.checkWallCollision(dx, dy)
        
        if keys[pygame.K_LEFT]:
            self.angle -= settings.PLAYER_ROT_SPEED * self.game.dt
        if keys[pygame.K_RIGHT]:
            self.angle += settings.PLAYER_ROT_SPEED * self.game.dt
        self.angle %= math.tau
        
    def checkWall(self, x, y):
        return (x, y) not in self.game.map.world_map
    
    def checkWallCollision(self, dx, dy):
        scale = settings.PLAYER_SIZE_SCALE / self.game.dt
        if self.checkWall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.checkWall(int(self.x), int(self.y + dy * scale)):
            self.y += dy
        
    def draw(self):
        #pygame.draw.line(self.game.screen, 'yellow', 
        #                 (self.x * math.floor(settings.WIDTH / 16), 
        #                  self.y * math.floor(settings.HEIGHT / 9)),
        #                 (self.x * math.floor(settings.WIDTH / 16) + settings.WIDTH * math.cos(self.angle), 
        #                  self.y * math.floor(settings.HEIGHT / 9) + settings.HEIGHT * math.sin(self.angle)), 2)
        pygame.draw.circle(self.game.screen, 'green', 
                           (self.x * math.floor(settings.WIDTH / 16),
                            self.y * math.floor(settings.HEIGHT / 9)), 15)
    
    def update(self):
        self.movement()
        
    @property 
    def pos(self):
        return self.x, self.y 
    
    @property 
    def map_pos(self):
        return int(self.x), int (self.y)