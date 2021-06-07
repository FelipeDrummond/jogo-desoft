import pygame
import os

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
 


BG1 = 'bg_img1'
BG2 = 'bg_img2'
BG3 = 'bg_img3'
BG4 = 'bg_img4'
BG5 = 'bg_img5'
BG6 = 'bg_img6'
BG7 = 'bg_img7'
BG8 = 'bg_img8'
BG9 = 'bg_img9'
TILES = 'tl'
GAME_OVER = 'game_over'
NAVE = 'nave'

def load_assets():
    assets = {}
    assets[BG1] = pygame.image.load("Image/City5.jpg")
    assets[BG1] = pygame.transform.scale(BG1, (LA_BG, ALT_TELA))

    assets[BG2] = pygame.image.load("Image/City2_1.jpg")
    assets[BG2] = pygame.transform.scale(BG2, (LA_BG, ALT_TELA))

    assets[BG3] = pygame.image.load("Image/City3.jpg")
    assets[BG3] = pygame.transform.scale(BG3, (LA_BG, ALT_TELA))

    assets[BG4] = pygame.image.load("Image/City4.jpg")
    assets[BG4] = pygame.transform.scale(BG4, (LA_BG, ALT_TELA))

    assets[BG5] = pygame.image.load("Image/City4.jpg")
    assets[BG5] = pygame.transform.scale(BG5, (LA_BG, ALT_TELA))

    assets[BG6] = pygame.image.load("Image/City4.jpg")
    assets[BG6] = pygame.transform.scale(BG6, (LA_BG, ALT_TELA))

    assets[BG7] = pygame.image.load("Image/City4.jpg")
    assets[BG7] = pygame.transform.scale(BG7, (LA_BG, ALT_TELA))

    assets[BG8] = pygame.image.load("Image/City4.jpg")
    assets[BG8] = pygame.transform.scale(BG8, (LA_BG, ALT_TELA))

    assets[BG9] = pygame.image.load("Image/City4.jpg")
    assets[BG9] = pygame.transform.scale(BG9, (LA_BG, ALT_TELA))

    assets[TILES] = pygame.image.load("Image/FullTiles.jpg")
    assets[TILES] = pygame.transform.scale(BG9, (LARG_TILES, ALT_TILES))

    assets[GAME_OVER] = pygame.image.load("Image/GameOver.jpg")
    assets[GAME_OVER] = pygame.transform.scale(BG9, (LARG_TELA, ALT_TELA))



    return assets