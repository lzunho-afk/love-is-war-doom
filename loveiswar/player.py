#!/usr/bin/env python3
# Copyright (c) MIT
# Lucas Zunho <lucaszunho17@gmail.com>

import pygame
import math
from loveiswar import settings

class Player:
    """Controle de informações e eventos relacionados ao jogador.

    Attributes:
    	game (loveiswar.main.Game): Objeto `Game` do contexto em execução.
        x (int): Valor horizontal ('X') da coordenada do player.
        y (int): Valor vertical ('Y') da coordenada do player.
        angle (int): Armazena o valor de :py:data:`loveiswar.settings.PLAYER_ANGLE`.
        	Se referindo ao ângulo de visão do player (utilizado pelo raycasting).
        rel (tuple): Tupla com o valor de movimento do mouse no formato '(x, y)'.
    """
    def __init__(self, game):
        """Atribuição das variáveis do contexto atual do jogo e do player.

        As coordenadas (x, y) do player têm o valor inicial de acordo com as
        configurações setadas no :py:mod:`loveiswar.settings` - valores da tupla 
        :py:data:`loveiswar.settings.PLAYER_POS`.
        
        Args:
        	game (loveiswar.game.Game): Obj. `Game` em execução.
        """
        self.game = game
        self.x, self.y = settings.PLAYER_POS[0], settings.PLAYER_POS[1]
        self.angle = settings.PLAYER_ANGLE
        
    def movement(self):
        """Verifica eventos relacionados ao movimento do player.

        Aqui são armazenados alguns valores relacionados à alteração espacial
        do player e também ocorre a verificação dos eventos do teclado (WASD)
        que têm a ver com o movimento.
        """
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
            
        self.check_wall_collision(dx, dy)
        """Verificação de colisão com base no movimento prestes a ocorrer
        	sobre as escalas do jogo (:py:mod:`loveiswar.settings`)."""
        
        # if keys[pygame.K_LEFT]:
            # self.angle -= settings.PLAYER_ROT_SPEED * self.game.dt
        # if keys[pygame.K_RIGHT]:
            # self.angle += settings.PLAYER_ROT_SPEED * self.game.dt
        self.angle %= math.tau
        
    def check_wall(self, x, y):
        """Verifica as coordenadas em relação ao mapa de renderização do jogo.

        Args:
        	x (int): Valor 'X' (horizontal) da coordenada a ser verificada.
            y (int): Valor 'Y' (vertical) da coordenada a ser verificada.

        Returns:
        	bool: 'True' caso a coordenada esteja no mapa (colidindo) e 'False'
            	caso contrário.
        """
        return (x, y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        """Verifica a colisão nas duas dimensões, considerando a escala e a posição
        	atual do player.

        Args:
        	dx (int): Valor de variação da posição do player na linha 'X' - horizontal.
            dy (int): Valor de variação da posição do player na linha 'Y' - vertical.
        """
        scale = settings.PLAYER_SIZE_SCALE / self.game.dt
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy
        
    def draw(self):
        """Renderiza um círculo para visualização e controle da distância de colisão
        	do player e, caso ativo, uma linha para visualização do ponteiro do mouse.

        .. todo:: Criar alternância de visibilidade da linha do cursor através de eventos
        	do teclado.
        """
        #pygame.draw.line(self.game.screen, 'yellow', 
        #                 (self.x * math.floor(settings.WIDTH / 16), 
        #                  self.y * math.floor(settings.HEIGHT / 9)),
        #                 (self.x * math.floor(settings.WIDTH / 16) + settings.WIDTH * math.cos(self.angle), 
        #                  self.y * math.floor(settings.HEIGHT / 9) + settings.HEIGHT * math.sin(self.angle)), 2)
        pygame.draw.circle(self.game.screen, 'green', 
                           (self.x * 100,
                            self.y * 100), 15)
    
    def mouse_control(self):
        """Altera o angulo de acordo com a atual movimentação do mouse."""
        mx, my = pygame.mouse.get_pos()
        if mx < settings.MOUSE_BORDER_LEFT or mx > settings.MOUSE_BORDER_RIGHT:
            pygame.mouse.set_pos([settings.HALF_WIDTH, settings.HALF_HEIGHT])
        self.rel = pygame.mouse.get_rel()[0]
        self.rel = max(-settings.MOUSE_MAX_REL, min(settings.MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * settings.MOUSE_SENSITIVITY * self.game.dt
    
    def update(self):
        """Chama os métodos de verificação e alteração do movimento e da perspectiva do player."""
        self.movement()
        self.mouse_control()
        
    @property 
    def pos(self):
        """list (int): Coordenadas da atual posição do player."""
        return self.x, self.y
    
    @property 
    def map_pos(self):
        """list (int): Coordenadas da atual posição do player no contexto do mapa."""
        return int(self.x), int(self.y)
