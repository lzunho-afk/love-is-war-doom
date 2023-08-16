#!/usr/bin/env python3
# Copyright (c) MIT
# Lucas Zunho <lucaszunho17@gmail.com>

import pygame

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [1, _, _, 2, 2, 2, 2, _, _, _, 5, 5, 5, _, _, 3],
    [1, _, _, _, _, _, 2, _, _, _, _, _, 5, _, _, 3],
    [1, _, _, _, _, _, 2, _, _, _, _, _, 5, _, _, 3],
    [1, _, _, 2, 2, 2, 2, _, _, _, _, _, _, _, _, 3],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [1, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, 3],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
]
"""lista de inteiros: Define o tamanho do mapa e a localização das texturas. 

    :meta hide-value:
"""

class Map:
    """Representação de mapa do jogo com sua interface de renderização.

    Essa classe inicializa e renderiza os elementos de mapa, incluindo os
    arquivos de abstração de mapa e seus respectivos updates, que se referem
    a quaisquer eventuais atualizações que o usuário possa fazer em relação
    ao mapa do jogo pelo andamento da história do mesmo.

    Attributes:
    	game (:obj:`loveiswar.main.Game`): Objeto `Game` do contexto em execução.
        mini_map (int matrix):Representação do mapa e suas texturas.
        world_map (int list): Representação do mapa e suas texturas com um index
        	de tuplas para representar suas coordenadas.
    """
    def __init__(self, game):
        """Atribuição das variáveis do atual contexto do jogo e indexação do
        	mapa alvo.

        Args:
        	game (:obj:`loveiswar.game.Game`): Obj. `Game` em execução.
        """
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
        
    def get_map(self):
        """Indexação do arquivo de mapa.

        Transforma a lista de inteiros que representa o mapa e suas texturas em
        uma lista de inteiros com tuplas como chave, facilitando para o
        reconhecimento de suas coordenadas.
        """
        for j, row in enumerate(self.mini_map):
            for i, val in enumerate(row):
                if val:
                    self.world_map[(i, j)] = val
                    
    def draw(self):
        [pygame.draw.rect(self.game.screen, 'darkgray', (
            pos[0] * 100,
            pos[1] * 100, 
            100, 
            100
        ), 2)
         for pos in self.world_map]
        
