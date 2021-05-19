import pygame

pygame.init()


window = pygame.display.set_mode((300, 600))
pygame.display.set_caption('Subway surfers 2.0')


game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            game = False

    window.fill((255, 255, 255))


    pygame.display.update()


pygame.quit()

