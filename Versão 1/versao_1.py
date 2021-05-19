# === JOGO SUBWAY SURFERS 2.0 ===
# ---- Importando bibliotecas necessárias
import pygame

pygame.init()

# ---- Definindo a tela
ALT_TELA = 500
LARG_TELA = 1000
window = pygame.display.set_mode((LARG_TELA, ALT_TELA))
pygame.display.set_caption('Subway surfers 2.0')

# ---- ASSETS
BG = pygame.image.load('assets/background.jpeg').convert()
BG = pygame.transform.scale(BG, (LARG_TELA, ALT_TELA))

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(BG, (0, 0))
    pygame.display.update()  # Mostra o novo frame para o jogador

pygame.quit()

