#!/usr/bin/env python3
# Copyright (c) MIT
# Lucas Zunho <lucaszunho17@gmail.com>

import math
import pygame

from loveiswar import settings

class SpriteObject:
    """Manuseio de sprites, suas projeções e demais efeitos.

    Attributes:
    	game (loveiswar.main.Game): Objeto `Game` do contexto em execução.
        player (loveiswar.player.Player): Objeto de representação do player.
        x (int): Posição horizontal de coordenada do sprite.
        y (int): Posição vertical de coordenada do sprite.
        image (pygame.Surface): Imagem do sprite carregada com `per pixel alpha`.
        IMAGE_WIDTH (int): Largura em pixels da imagem carregada como sprite.
        IMAGE_HALF_WIDTH (int): Meio valor da largura da imagem carregada como sprite.
        IMAGE_RATIO (float): Proporção da imagem carregada como sprite.
        dx (int): Valor variável de X em relação ao player.
        dy (int): Valor variável de Y em relação ao player.
        theta (float): Valor da op. de arcotangente para mensuração do ângulo entre
        	os valores de váriação dx e dy.
        screen_x (int): Posição X do sprite na projeção da tela.
        distance (int): Distância entre o player e o sprite.
        normal_distance (int): Distância entre o player e o sprite com ajuste para
        	efeito olho de peixe.
        SPRITE_SCALE (float): Valor de escala de exibição do sprite.
        SPRITE_HEIGHT_SHIFT (float): Valor de deslocamento do sprite na vertical.
    """
    def __init__(self, game, path='assets/sprites/static/real_heart.png', pos=(10.5, 3.5), scale=0.5, shift=0.0):
        """Inicializa os atributos e define o contexto inicial do sprite.

        Esse construtor, além de definir os valor padrões através dos argumentos
        passados, também ajusta o encoding dos pixels da imagem do sprite,
        convertendo-os para um formato mais otimizado (próprio do pygame).

        Args:
        	game (loveiswar.main.Game): Obj. `Game` em execução.
            path (str): Caminho do arquivo de imagem do sprite.
            pos (float tuple): Posição de exibição do sprite no mapa.
            scale (float): Escala de exibição do sprite.
            shift (float): Valor de deslocamento do sprite na linha vertical.
        """
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
        """Calcula e coloca o sprite na lista de renderização.

        A imagem de sprite é escalonada conforme as definições de tela e a
        escala pré definida no construtor. Define-se o devido item de renderização
        do sprite e sua adição à lista de renderização é feita.
        """
        projection = settings.SCREEN_DIST / self.normal_distance * self.SPRITE_SCALE
        projection_width = projection * self.IMAGE_RATIO
        projection_height = projection 
        
        image = pygame.transform.scale(self.image, (projection_width, projection_height))
        
        self.sprite_half_width = projection_width // 2
        height_shift = projection_height * self.SPRITE_HEIGHT_SHIFT
        pos = self.screen_x - self.sprite_half_width, settings.HALF_HEIGHT - projection_height // 2 + height_shift
        
        self.game.raycasting.objects_to_render.append((self.normal_distance, image, pos))

    def get_sprite(self):
        """Cálculo das normativas de distância e perspectiva do sprite.

        Aqui é feita a definição das variáveis relativas dx, dy conforme a
        posição do player em relação ao obj. sprite e os cálculos necessários
        de perspectiva em relação ao mesmo. Observa-se nesse segmento a verificação
        da necessidade de ocorrência ou não da projeção do sprite.
        """
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
        """Método de atualização do obj. sprite.

        Esse método é utilizado no loop principal do jogo (Ver :py:mod:`loveiswar.main`)
        para a verificação continua do objeto de sprite. Ele realiza a chamada, portanto,
        do método :py:meth:`loveiswar.sprite_object.SpriteObject.get_sprite` para obter a
        atualização dos atributos.
        """
        self.get_sprite()
