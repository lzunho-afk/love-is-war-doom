#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:58:33 2023

@author: lzunho-afk
"""

import pygame
import math
import settings

class RayCasting:
    def __init__(self, game):
        self.game = game
        
    def rayCast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos
        
        ray_angle = self.game.player.angle - settings.HALF_FOV + 0.0001
        for ray in range(settings.NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            
            # Intersections with horizontals
            if sin_a > 0:
                y_hor = y_map + 1
                dy = 1
            else:
                y_hor = y_map - 1e-6
                dy = -1
                
            horizontal_depth = (y_hor - oy) / sin_a
            x_hor = ox + horizontal_depth * cos_a
            
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a
            
            for i in range(settings.MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy                
                horizontal_depth += delta_depth
            
            # Intersections with verticals
            if cos_a > 0:
                x_vert = x_map + 1
                dx = 1
            else:
                x_vert = x_map - 1e-6
                dx = -1
            
            vertical_depth = (x_vert - ox) / cos_a
            y_vert = oy + vertical_depth * sin_a
            
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a
            
            for i in range(settings.MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                vertical_depth += delta_depth
            
            # Set Depth
            if vertical_depth < horizontal_depth:
                depth = vertical_depth
            else:
                depth = horizontal_depth
            
            # RayCasting debug lines
            if settings.RAYCASTING_DEBUG:
                pygame.draw.line(self.game.screen, 'yellow', 
                                 (math.floor(settings.WIDTH / 16) * ox,
                                  math.floor(settings.HEIGHT / 9) * oy),
                                 (math.floor(settings.WIDTH / 16) * ox + math.floor(settings.WIDTH / 16) * depth * cos_a,
                                  math.floor(settings.HEIGHT / 9) * oy + math.floor(settings.HEIGHT / 9) * depth * sin_a), 2)
                
            # Projection
            projection_height = settings.SCREEN_DIST / (depth + 0.0001)
            
            # Walls
            color = [255 / (1 + depth ** 5 * 0.00002)] * 3 # Distance Shadow
            pygame.draw.rect(self.game.screen, color,
                             (ray * settings.SCALE,
                              settings.HALF_HEIGHT - projection_height // 2,
                              settings.SCALE,
                              projection_height))
            
            ray_angle += settings.DELTA_ANGLE
    
    def update(self):
        self.rayCast()