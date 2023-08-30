#!/usr/bin/env python3
# Copyright (c) MIT
# Lucas Zunho <lucaszunho17@gmail.com>
""" Configurações de inicialização e manutenção do jogo/engine.

Todas as variáveis globais desse arquivo representam configurações
que serão utilizadas no contexto da engine. Elas podem ser alteradas
por via externa (arquivos de configuração yaml) ou através de 
alterações devidas pelo próprio contexto da engine (via interna).

    .. todo:: Classe de manipulação da configuração por yaml.
"""

import math

RAYCASTING_DEBUG = False
"""bool: Define a visibilidade das linhas de debug do raycasting."""

WIDTH = 1366
HEIGHT = 768
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

RES = (WIDTH, HEIGHT)
"""tuple: Tupla de dois valores -> largura e altura, representando a resolução em uso."""

FPS = 60
"""int: Frames por segundo utilizados pelo clock do pygame.

Esse valor de framerate será utilizado pelo método `tick` do
Clock do pygame para atualizá-lo com o tempo certo de delay de
cada chamada.
"""

PLAYER_POS = (1.5, 5)
"""tuple: Representação do local de \"nascimento\" do jogador dentro do mapa do jogo.

Esses dois valores em tupla devem levar em consideração os limites
de mapa impostos pela variável :py:data:`loveiswar.map.mini_map`.
"""

PLAYER_ANGLE = 0
"""int: Valor de representação do ângulo de visão do player.

Esse valor é utilizado pela classe :py:class:`loveiswar.raycasting.RayCasting`
para cálculo de renderização das rays e, também, pelo módulo
:py:mod:`loveiswar.player` para cálculos relacionados ao
movimento do player.
"""

PLAYER_SPEED = 0.004
"""float: Valor de representação da velocidade do player.

O float de velocidade será utilizado em conjunto com o deltatime
:py:data:`loveiswar.main.Game.dt` da instância do jogo para cálculo
correto da velocidade de movimento e a previsão de colisão do player.
"""

PLAYER_ROT_SPEED = 0.002
"""float: Valor de representação da velocidade de rotação do mouse na
	representação 2D do raycasting.

Esse valor deverá ser utilizado junto da opção de representação 2D do
jogo. Essa opção deve ser ativada por linha de comando (ver :py:mod:`loveiswar.main`).
"""

PLAYER_SIZE_SCALE = 60
"""int: Valor referência para a `hitbox` do player.

Essa variável é utilizada pelo :py:mod:`loveiswar.player` para
verificação de colisão.
"""

MOUSE_SENSITIVITY = 0.0003
"""float: Valor de sensibilidade do mouse.

Essa variável é utilizada como base para o cálculo de alteração
da rotação do player conforme o movimento do mouse.
"""

MOUSE_MAX_REL = 40
"""int: Quantidade de movimento máximo para registro do mouse.

Utilizada pelo método :py:meth:`loveiswar.player.Player.mouse_control` para controle
da quantidade de movimento do mouse para cada frame do jogo.
"""

MOUSE_BORDER_LEFT = 100
"""int: Menor valor do limite do ponteiro do mouse.

Esse valor é utilizada em conjunto com :py:data:`loveiswar.settings.MOUSE_BORDER_RIGHT`
para manter o cursor sempre em movimento, permitindo seu uso
indiscriminado pelo usuário (sem atender aos limites do monitor).
"""

MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT
"""int: Maior valor do limite do ponteiro do mouse.

Ver :py:data:`loveiswar.settings.MOUSE_BORDER_LEFT`.
"""

FLOOR_COLOR = (30, 30, 30)

FOV = math.pi / 3
HALF_FOV = FOV / 2

NUM_RAYS = WIDTH // 2
"""int: Número de rays a serem consideradas pelo raycasting.

Esse valor será utilizado pelo módulo :py:mod:`loveiswar.raycasting`
para definir a renderização da quantidade ideal de rays conforme a
resolução do jogo.
"""

HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
"""float: Valor do ângulo de cada ray.

Esse valor em graus é utilizado pelo método :py:meth:`loveiswar.raycasting.RayCasting.ray_cast`
para andar pelas rays dentro do atual ângulo de visão do player (:py:data:`loveiswar.player.Player.angle`).
"""

MAX_DEPTH = 20
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS
"""int: Valor base de escala do jogo.

Esse valor é utilizado para verificar colisão e realizar a renderização
das paredes e suas texturas, conforme :py:meth:`loveiswar.raycasting.RayCasting.get_objects_to_render`
e :py:meth:`loveiswar.player.Player.check_wall_collision`.
"""

TEXTURE_SIZE = 1024
"""int: Tamanho em pixels das texturas carregadas pelo jogo.

Esse valor é utilizado para padronizar a resolução de carregamento
das texturas, escalonando-as conforme necessário. Ver
:py:meth:`loveiswar.object_renderer.ObjectRenderer.get_texture`.
"""

TEXTURE_TUPLE = (TEXTURE_SIZE, TEXTURE_SIZE)
"""int: Tupla (x, y) de tamanho das texturas.

Ver :py:data:`loveiswar.settings.TEXTURE_SIZE`.
"""

HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2
