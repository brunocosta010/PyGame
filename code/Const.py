# C
C_RED = (100, 0, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
import pygame

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0':1,
    'Level1Bg1': 1,
    'Level1Bg2': 1,
    'Level1Bg3': 1,
    'Level1Bg4': 1,
    'Level2Bg0': 1,
    'Level2Bg1': 1,
    'Level2Bg2': 1,
    'Level2Bg3': 1,
    'Level2Bg4': 1,
    'Player1': 3,
    'Player1Shot': 5,
    'Player2': 3,
    'Player2Shot': 1,
    'Enemy1': 1,
    'Enemy1Shot' : 3,
    'Enemy2': 1,
    'Enemy2Shot': 2
}

# H
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

# D

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1'  : 1,
    'Player1Shot': 25,
    'Player2'  : 1,
    'Player2Shot': 20,
    'Enemy1'   : 1,
    'Enemy1Shot' : 1,
    'Enemy2'   : 1,
    'Enemy2Shot' : 1
}

ENTITY_SCORE = {

    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1' : 0,
    'Player1Shot': 0,
    'Player2' : 0,
    'Player2Shot': 0,
    'Enemy1'  : 100,
    'Enemy1Shot' : 0,
    'Enemy2'  : 125,
    'Enemy2Shot' : 0
}

# E
ENTITY_SHOT_DELAY = {
    'Player1' : 20,
    'Player2' : 15,
    'Enemy1': 100,
    'Enemy2': 200
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITION',
               'SCORE',
               'EXIT')

# P
import pygame

PLAYER_KEY_UP = {
    'Player1': pygame.K_UP,
    'Player2': pygame.K_w
}

PLAYER_KEY_DOWN = {
    'Player1': pygame.K_DOWN,
    'Player2': pygame.K_s
}

PLAYER_KEY_LEFT = {
    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a
}

PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d
}

PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_LCTRL,
    'Player2': pygame.K_RCTRL
}

# S
SPAWN_TIME = 4000

#ST

TIMEOUT_STEP = 100

# T

TIMEOUT_LEVEL = 10000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
