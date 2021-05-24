# === JOGO SUBWAY SURFERS 2.0 ===
# ---- Importando bibliotecas necessárias
import pygame
import os

pygame.init()

# ---- Definindo a tela
ALT_TELA = 500
LARG_TELA = 1000
window = pygame.display.set_mode((LARG_TELA, ALT_TELA))
pygame.display.set_caption('Subway surfers 2.0')

# ---- ASSETS

pygame.init()
win = pygame.display.set_mode((1000, 500))
bg_img = pygame.image.load("Image/City5.jpg")
bg = pygame.transform.scale(bg_img, (1000, 500))
bg_img2 = pygame.image.load("Image/City2_1.jpg")
bg2 = pygame.transform.scale(bg_img2, (1000, 500))

width = 1000
i = 0

run = True

ig = 0

while run:
      
    if ig <= 100000:
        for event in pygame.event.get():
                
            if event.type == pygame.QUIT:
                run = False

        win.fill((0,0,0))

        #Create looping background
        win.blit(bg, (i, 0))
        win.blit(bg, (width + i, 0))
        if i == -width:
            i = 0
        i -= 0.5

        ig += 2
        pygame.display.update()
        

    elif ig > 100000 and ig < 125000:
        for event in pygame.event.get():
                
            if event.type == pygame.QUIT:
                run = False

        win.fill((0,0,0))

        #Create looping background
        win.blit(bg2, (i, 0))
        win.blit(bg2, (width + i, 0))
        if i == -width or i < -width:
            i = 0
        i -= 1.25

        pygame.display.update()
        ig += 2

    elif ig == 125000:
        for event in pygame.event.get():
                
            if event.type == pygame.QUIT:
                run = False

        win.fill((0,0,0))

        #Create looping background
        win.blit(bg, (i, 0))
        win.blit(bg, (width + i, 0))
        if i == -width or i < -width:
            i = 0
        i -= 1.25

        
        pygame.display.update()
        ig = 0       

