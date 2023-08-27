#!/usr/bin/env python3
# Copyright (c) MIT
# Lucas Zunho <lucaszunho17@gmail.com>

import math
import pygame

from loveiswar import settings

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
        self.normal_distance = 1
        self.sprite_half_width = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift
        
    def get_sprite_projection(self):
        projection = settings.SCREEN_DIST / self.normal_distance * self.SPRITE_SCALE
        projection_width = projection * self.IMAGE_RATIO
        projection_height = projection 
        
        image = pygame.transform.scale(self.image, (projection_width, projection_height))
        
        self.sprite_half_width = projection_width // 2
        height_shift = projection_height * self.SPRITE_HEIGHT_SHIFT
        pos = self.screen_x - self.sprite_half_width, settings.HALF_HEIGHT - projection_height // 2 + height_shift
        
        self.game.raycasting.objects_to_render.append((self.normal_distance, image, pos))

    def get_sprite(self):
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
        self.normal_distance = self.distance * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (settings.WIDTH + self.IMAGE_HALF_WIDTH) and self.normal_distance > 0.5:
            self.get_sprite_projection()
            
    def update(self):
        self.get_sprite()
