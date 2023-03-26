#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:29:26 2023

@author: lzunho-afk
"""

import math
import pygame 
import settings

class SpriteObject:
    def __init__(self, game, path='assets/sprites/static/real_heart.png', pos=(10.5, 3.5), scale=0.5, shift=0.0):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pygame.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx = 0
        self.dy = 0
        self.theta = 0
        self.screen_x = 0
        self.distance = 1
        self.normalDistance = 1
        self.spriteHalfWidth = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift
        
    def getSpriteProjection(self):
        projection = settings.SCREEN_DIST / self.normalDistance * self.SPRITE_SCALE
        projectionWidth = projection * self.IMAGE_RATIO
        projectionHeight = projection 
        
        image = pygame.transform.scale(self.image, (projectionWidth, projectionHeight))
        
        self.spriteHalfWidth = projectionWidth // 2
        heightShift = projectionHeight * self.SPRITE_HEIGHT_SHIFT
        pos = self.screen_x - self.spriteHalfWidth, settings.HALF_HEIGHT - projectionHeight // 2 + heightShift
        
        self.game.raycasting.objectsToRender.append((self.normalDistance, image, pos))

    def getSprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)
        
        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau
            
        delta_rays = delta / settings.DELTA_ANGLE
        self.screen_x = (settings.HALF_NUM_RAYS + delta_rays) * settings.SCALE
        
        self.distance = math.hypot(dx, dy)
        self.normalDistance = self.distance * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (settings.WIDTH + self.IMAGE_HALF_WIDTH) and self.normalDistance > 0.5:
            self.getSpriteProjection()
            
    def update(self):
        self.getSprite()