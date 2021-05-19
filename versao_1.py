# === JOGO SUBWAY SURFERS 2.0 ===
# ---- Importando bibliotecas necessárias
import pygame

pygame.init()

# ---- Definindo a tela
window = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Subway surfers 2.0')

# ---- ASSETS
BG = pygame.image.load('lm_jogo.jpeg').convert()


game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            game = False

    window.fill((255, 255, 255))


    pygame.display.update()


pygame.quit()

