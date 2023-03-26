#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:58:50 2023

@author: lzunho-afk
"""

import math

RAYCASTING_DEBUG = False

WIDTH = 1366
HEIGHT = 768
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
RES = (WIDTH, HEIGHT)
FPS = 60

PLAYER_POS = (1.5, 5)
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
PLAYER_SIZE_SCALE = 60

MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOR = (30, 30, 30)

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 1024
TEXTURE_TUPLE = (TEXTURE_SIZE, TEXTURE_SIZE)
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2
