#!/usr/bin/env python3
# Copyright (c) MIT
# Lucas Zunho <lucaszunho17@gmail.com>

import pygame
import math
import settings

class RayCasting:
    """Implementação e projeção de raycasting no contexto do jogo.

    Attributes:
    	game (loveiswar.main.Game): Objeto `Game` do contexto em execução.
        rayCastingResult (list): Lista com os valores de escala e textura para renderização e
        	projeção das `rays`.
        objectsToRender (list): Lista de obj. descrevendo as `rays` já prontas para renderização.
        textures (pygame.Surface list): Lista das texturas de parede do jogo - refere-se à
        	:py:class:`loveiswar.main.Game`.
    """
    def __init__(self, game):
        """Atribuição das variáveis do atual contexto do jogo e inicialização das listas
        	para atribuição das `rays`.

        Args:
        	game (:obj:`loveiswar.game.Game`): Obj. `Game` em execução.
        """
        self.game = game
        self.rayCastingResult = []
        self.objectsToRender = []
        self.textures = self.game.object_renderer.wallTextures
        
    def getObjectsToRender(self):
        """Cria a lista de renderização de acordo com cada `ray` e sua respectiva textura.

        O método verifica cada valor resultante do raycasting (:py:meth:`loveiswar.raycasting.Raycasting.rayCast`)
        e ajusta a escala da textura sobre cada `ray` para definir a perspectiva correta
        na tela, alocando-a na lista de renderização.
        """
        self.objectsToRender = []
        for ray, values in enumerate(self.rayCastingResult):
            depth, projectionHeight, texture, offset = values
            
            if projectionHeight < settings.HEIGHT:
                wallColumn = self.textures[texture].subsurface(
                    offset * (settings.TEXTURE_SIZE - settings.SCALE), 0, settings.SCALE, settings.TEXTURE_SIZE
                )
                wallColumn = pygame.transform.scale(wallColumn, (settings.SCALE, projectionHeight))
                wallPosition = (ray * settings.SCALE, settings.HALF_HEIGHT - projectionHeight // 2)
            else:
                textureHeight = settings.TEXTURE_SIZE * settings.HEIGHT / projectionHeight
                wallColumn = self.textures[texture].subsurface(
                    offset * (settings.TEXTURE_SIZE - settings.SCALE),
                    settings.HALF_TEXTURE_SIZE - textureHeight // 2,
                    settings.SCALE, textureHeight
                )
                wallColumn = pygame.transform.scale(wallColumn, (settings.SCALE, settings.HEIGHT))
                wallPosition = (ray * settings.SCALE, 0)
                
            self.objectsToRender.append((depth, wallColumn, wallPosition))
        
    def rayCast(self):
        """Cálculo do `raycasting` para a projeção 3D."""
        self.rayCastingResult = []
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos
        
        verticalTexture, horizontalTexture = 1, 1
        
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
                    horizontalTexture = self.game.map.world_map[tile_hor]
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
                    verticalTexture = self.game.map.world_map[tile_vert]
                    break
                x_vert += dx
                y_vert += dy
                vertical_depth += delta_depth
            
            # Set Depth & Texture Offset
            if vertical_depth < horizontal_depth:
                depth = vertical_depth
                texture = verticalTexture
                y_vert %= 1
                
                if cos_a > 0:
                    offset = y_vert
                else:
                    offset = (1 - y_vert)
            else:
                depth = horizontal_depth
                texture = horizontalTexture
                x_hor %= 1
                
                if sin_a > 0:
                    offset = (1 - x_hor)
                else:
                    offset = x_hor
            
            depth *= math.cos(self.game.player.angle - ray_angle)
            
            # RayCasting debug lines
            if settings.RAYCASTING_DEBUG:
                pygame.draw.line(self.game.screen, 'yellow', 
                                 (100 * ox,
                                  100 * oy),
                                 (100 * ox + 100 * depth * cos_a,
                                  100 * oy + 100 * depth * sin_a), 2)
                
            # Projection
            projection_height = settings.SCREEN_DIST / (depth + 0.0001)
            
            # Defining RayCasting result
            self.rayCastingResult.append((depth, projection_height, texture, offset))
            
            ray_angle += settings.DELTA_ANGLE
    
    def update(self):
        """Cálcula e atualiza a lista de renderização do `raycasting`."""
        self.rayCast()
        self.getObjectsToRender()
