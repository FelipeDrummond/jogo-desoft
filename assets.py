import pygame
import os

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