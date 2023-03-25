#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:58:26 2023

@author: lzunho-afk
"""

import pygame
import settings 

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wallTextures = self.loadWallTextures()
        
    def draw(self):
        self.renderGameObjects()
        
    def renderGameObjects(self):
        objectsList = self.game.raycasting.objectsToRender
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