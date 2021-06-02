from os import path

# Estabelece a pasta que contém as figuras e sons
IMG_DIR = path.join(path.dirname(__file__), 'Assets', 'Image')
PLAYER_DIR = path.join(path.dirname(__file__), 'Assets', 'Player')
OTHER_DIR = path.join(path.dirname(__file__), 'Assets', 'Other')
SND_DIR = path.join(path.dirname(__file__), 'Assets', 'snd')

# Parâmetros Universais do jogo
ALT_TELA = 500 # Altura da tela
LARG_TELA = 950 # Largura da tela
LA_BG = 1000 # Largura do Background
FPS = 28 # Frames por segundo

# Parâmetros de tamanho de obstáculos
# AERONAVE
ALT_NAVE = 70
LARG_NAVE = 140
# STOP
ALT_STOP = 125
LARG_STOP = 85
# BARREIRA
ALT_CONE = 95
LARG_CONE = 75 
# CHÃO
ALT_TILES = 100
LARG_TILES = 1000
 




