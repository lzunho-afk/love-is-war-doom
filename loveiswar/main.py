#!/usr/bin/env python3
# Copyright (c) MIT
# Lucas Zunho <lucaszunho17@gmail.com>
"""Inicialização e representação do contexto do jogo.

Esse módulo apresenta a classe :py:class:`loveiswar.main.Game` e a sua inicialização
no caso de execução.

	.. todo:: Opção de linha de comando para alterar a visibilidade para modo 2D.
"""

import pygame
import sys
from pygame.locals import *

from loveiswar import settings
from loveiswar import map
from loveiswar import player
from loveiswar import raycasting
from loveiswar import object_renderer
from loveiswar import sprite_object

class Game:
    """Representação da montagem e atualização de todo o contexto do jogo.

    A classe carrega os elementos fundamentais da janela em seu construtor,
    redefinindo quaisquer elementos anteriores por acaso definidos no contexto
    do pygame e cria (`new_game`) o contexto específico do jogo dentro do
    pygame (o jogo em si).

    Attributes:
    	screen (pygame.Surface): Estrutura de controle do `display` do pygame.
        clock (pygame.time.Clock): Objeto utilizado para controle de tempo.
        dt (int): delta-time.
        map (loveiswar.map.Map): Controle e desenho do mapa.
        player (loveiswar.player.Player): Objeto de controle do `player`.
        raycasting (loveiswar.raycasting.RayCasting): Objeto de controle
        	do sistema de raycasting.
        static_sprite (loveiswar.sprite_object.SpriteObject): Objeto de
        	controle e desenho de sprites.
        
    """
    def __init__(self):
        """Inicialização do pygame e configurações básicas do contexto da janela.

        As definições de display feitas no construtor são orientadas pelo módulo
        :py:mod:`loveiswar.settings` - configurações :py:data:`loveiswar.settings.RES`
        e :py:data:`loveiswar.settings.FULLSCREEN`. Todos os outros objetos
        utilizados pela classe para controlar o contexto do jogo também utilizam
        esse mesmo módulo para orientar suas definições.
        """
        pygame.init()
        pygame.mouse.set_visible(False)

        self.screen = pygame.display.set_mode(settings.RES, pygame.FULLSCREEN)
        """pygame.display: Inicialização do display pygame, destruindo quaisquer
        	outros que possivelmente existam (importante para isolar o contexto
        	pygame do jogo de outras instâncias do pygame - é o procedimento
        	padrão)."""
        
        self.clock = pygame.time.Clock()
        self.dt = 1
        self.new_game()
        
    def new_game(self):
        """Atribuição dos objetos auxiliares do jogo à classe.

        Os objetos com maior importância para o contexto do jogo são inicializados
        aqui (perspectiva macro). Tais objetos se referem a todas as tecnologias ou
        representações que estarão presentes constantemente no loop de atualização
        do jogo.
        """
        self.map = map.Map(self)
        self.player = player.Player(self)
        self.object_renderer = object_renderer.ObjectRenderer(self)
        self.raycasting = raycasting.RayCasting(self)
        self.static_sprite = sprite_object.SpriteObject(self)
    
    def update(self):
        """Realiza a atualização plana de todos os objetos fundamentais.

        Esse método chama os métodos `update` dos objetos construidos na inicialização
        do jogo e realiza as operações de atualização de display e tempo do pygame.
        """
        self.player.update()
        self.raycasting.update()
        self.static_sprite.update()
        pygame.display.flip()
        
        self.dt = self.clock.tick(settings.FPS)
        """int: Definição do `delta-time` (milissegundos) através do framerate
        	anteriormente definido (limitação do tempo de execução).
        """
        
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
    def draw(self):
        """Renderiza definições básicas do display e as que serão sobrepostas. """
        # self.screen.fill('black')
        self.object_renderer.draw()
        #self.map.draw()
        #self.player.draw()
        
    def check_events(self):
        """Verifica os eventos gerais do `display` e chama os métodos necessários. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
    
    def run(self):
        """Loop principal do jogo. Roda as ações de atualização e renderização do
        	jogo até o evento de saída."""
        while True:
            self.check_events()
            self.update()
            self.draw()
