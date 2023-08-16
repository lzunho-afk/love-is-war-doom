#!/usr/bin/env python3
# Copyright (c) MIT
# Lucas Zunho <lucaszunho17@gmail.com>

import pygame
import settings

class ObjectRenderer:
    """Renderiza filas de renderização e importa texturas necessárias.

    A classe carrega os objetos já em execução da classe
    :py:class:`loveiswar.main.Game` e carrega as textura básicas para
    a renderização do jogo, disponibilizando um método estático para o
    carregamento de texturas e chamadas para renderização do raycasting
    (:py:mod:`loveiswar.raycasting`) e, se for o caso, outros objetos
    considerados "dinâmicos".

    Attributes:
    	game (loveiswar.game.Game): Objeto `Game` do contexto em execução.
        screen (pygame.Surface): Surface base do jogo, usada como estrutura
        	de controle do `display`.
        wallTextures (pygame.Surface list): Lista de texturas pré-carregas das paredes.
        skyImage (pygame.Surface): textura de imagem do background (céu) do jogo.
    """
    def __init__(self, game):
        """Atribuição das variáveis do contexto atual do jogo e carregamento
        	das texturas base.

        Args:
        	game (:obj:`loveiswar.game.Game`): Obj. `Game` em execução.
        """
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

        self.sky_image = self.get_texture('assets/textures/sky.png',
            (settings.WIDTH, settings.HALF_HEIGHT))
        """Surface: Escalonagem da textura de céu para uso útil (1/2 da altura)."""
        
        self.sky_offset = 0
        
    def draw(self):
        """Chama os métodos de renderização do plano de fundo e os de objetos com
        	renderização específica. """
        self.draw_background()
        self.render_game_objects()
        
    def draw_background(self):
        """Renderiza o plano de fundo (céu) e o chão. """
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % settings.WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + settings.WIDTH, 0))
    
        # Floor
        pygame.draw.rect(self.screen, settings.FLOOR_COLOR, 
                         (0, settings.HALF_HEIGHT, settings.WIDTH, settings.HEIGHT))
        """:obj:`pygame.Rect`: renderização do chão do jogo com uma cor plana
        	(:py:data:`loveiswar.settings.FLOOR_COLOR`). """
        
    def render_game_objects(self):
        """Renderiza os objetos específicos da lista de renderização do jogo.

        Nesse método que ocorre a renderização das rays através da lista de objetos
        do objeto de raycasting (:py:class:`loveiswar.raycasting.RayCasting`) da classe Game.
        """
        objects_list = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, img, position in objects_list:
            self.screen.blit(img, position)
        
    @staticmethod 
    def get_texture(path, res=settings.TEXTURE_TUPLE):
        """Carrega uma imagem em alpha de um arquivo e o escalona sobre a resolução usada.

        Args:
        	path (str): Caminho para a imagem da textura a ser carregada.
            res (int tuple): Tupla com a resolução 2d da textura (Default:
            	:py:data:``loveiswar.settings.TEXTURA_TUPLE``).

        Returns:
        	pygame.Surface: textura ajustada com a resolução correta.
        """
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)
        
    def load_wall_textures(self):
        """Utiliza o módulo estático de carregamento de texturas para carregar as texturas
        	padrão de renderização do mapa.

        Returns:
        	`pygame.Surface` list: Lista com os objetos carregados com index iniciado em '1'.
        """
        return {
            1: self.get_texture('assets/textures/1.png'),
            2: self.get_texture('assets/textures/2.png'),
            3: self.get_texture('assets/textures/3.png'),
            4: self.get_texture('assets/textures/4.png'),
            5: self.get_texture('assets/textures/5.png')
        }
