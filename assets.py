import pygame
import os
from config import ALT_TELA, LARG_TELA, LA_BG, FPS, ALT_NAVE, LARG_NAVE, ALT_STOP, LARG_STOP, ALT_CONE, LARG_CONE, ALT_TILES, LARG_TILES

bg_img = pygame.image.load("Image/City5.jpg")
bg = pygame.transform.scale(bg_img, (1000, 500))
bg_img2 = pygame.image.load("Image/City2_1.jpg")
bg2 = pygame.transform.scale(bg_img2, (1000, 500))

BACKGROUND1 = 'background1'
BACKGROUND2 = 'background2'
def load_assets():
    assets = {}
    assets[BACKGROUND1] = pygame.image.load("Image/City5.jpg")
    assets[BACKGROUND1] = pygame.transform.scale(bg_img, (1000, 500))

    assets[BACKGROUND2] = pygame.image.load("Image/City2_1.jpg")
    assets[BACKGROUND2] = pygame.transform.scale(bg_img2, (1000, 500))
    return assets