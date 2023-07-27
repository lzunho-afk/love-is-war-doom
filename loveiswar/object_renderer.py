#!/usr/bin/env python3
# Copyright (c) MIT
# Lucas Zunho <lucaszunho17@gmail.com>

import pygame
import settings 

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wallTextures = self.loadWallTextures()
        self.skyImage = self.getTexture('assets/textures/sky.png',
                                         (settings.WIDTH, settings.HALF_HEIGHT))
        self.skyOffset = 0
        
    def draw(self):
        self.drawBackground()
        self.renderGameObjects()
        
    def drawBackground(self):
        self.skyOffset = (self.skyOffset + 4.5 * self.game.player.rel) % settings.WIDTH
        self.screen.blit(self.skyImage, (-self.skyOffset, 0))
        self.screen.blit(self.skyImage, (-self.skyOffset + settings.WIDTH, 0))
    
        # Floor
        pygame.draw.rect(self.screen, settings.FLOOR_COLOR, 
                         (0, settings.HALF_HEIGHT, settings.WIDTH, settings.HEIGHT))
        
    def renderGameObjects(self):
        objectsList = sorted(self.game.raycasting.objectsToRender, key=lambda t: t[0], reverse=True)
        for depth, img, position in objectsList:
            self.screen.blit(img, position)
        
    @staticmethod 
    def getTexture(path, res=settings.TEXTURE_TUPLE):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)
        
    def loadWallTextures(self):
        return {
            1: self.getTexture('assets/textures/1.png'),
            2: self.getTexture('assets/textures/2.png'),
            3: self.getTexture('assets/textures/3.png'),
            4: self.getTexture('assets/textures/4.png'),
            5: self.getTexture('assets/textures/5.png')
        }
