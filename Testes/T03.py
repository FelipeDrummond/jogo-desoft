import pygame
import os
import random
pygame.init()


win = pygame.display.set_mode((1000, 500))

bg_img = pygame.image.load("Assets/Image/City5.jpg")
bg_img2 = pygame.image.load("Assets/Image/City3.jpg")
bg_img3 = pygame.image.load("Assets/Image/City4.jpg")
bg_img4 = pygame.image.load("Assets/Image/City6.jpg")
bg_img5 = pygame.image.load("Assets/Image/City7.jpg")
bg_img6 = pygame.image.load("Assets/Image/City8.jpg")
bg_img7 = pygame.image.load("Assets/Image/City9.jpg")
bg_img8 = pygame.image.load("Assets/Image/City.gif")
bg_img9 = pygame.image.load("Assets/Image/City2_1.jpg")
plat_img = pygame.image.load("Assets/Other/plataforma2.png").convert_alpha()

BG = pygame.transform.scale(bg_img, (1000, 500))
BG2 = pygame.transform.scale(bg_img2, (1000, 500))
BG3 = pygame.transform.scale(bg_img3, (1000, 500))
BG4 = pygame.transform.scale(bg_img4, (1000, 500))
BG5 = pygame.transform.scale(bg_img5, (1000, 500))
BG6 = pygame.transform.scale(bg_img6, (1000, 500))
BG7 = pygame.transform.scale(bg_img7, (1000, 500))
BG8 = pygame.transform.scale(bg_img8, (1000, 500))
BG9 = pygame.transform.scale(bg_img9, (1000, 500))
PLAT = pygame.transform.scale(plat_img, (200, 80))

CORRER = [pygame.image.load(os.path.join("Assets/Player", "p1_walk01.png")),
           pygame.image.load(os.path.join("Assets/Player", "p1_walk03.png"))]
PULAR = pygame.image.load(os.path.join("Assets/Player", "p1_jump.png"))
AGAIXAR = [pygame.image.load(os.path.join("Assets/Player", "p1_down7.png")), 
           pygame.image.load(os.path.join("Assets/Player", "p1_down8.png"))]

class Platform:
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = random.randint(25, 350)
        self.speedx = 20

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < 0:
            self.rect.x = 1000
            self.rect.y = random.randint(25, 350)

    def muda(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Alien:
    X_POS = 80
    Y_POS = 400
    Y_POS_AG = 420
    vel_pulo = 8.5

    def __init__(self):

        #Var
        self.agaixa_img = AGAIXAR
        self.corre_img = CORRER
        self.pula_img = PULAR

        # Começa correndo sem estar agaixado ou pulando:
        self.alien_agaixa = False
        self.alien_corre = True
        self.alien_pula = False

        # Iniciais
        self.passo_index = 0
        self.pulo_vel = self.vel_pulo
        self.image = self.corre_img[0]
        self.alien_rect = self.image.get_rect()
        self.alien_rect.x = self.X_POS
        self.alien_rect.y = self.Y_POS

    # Atualiza conforme o usuario interaje
    def att(self, usIn):
        if self.alien_agaixa:
            self.agaixa()
        if self.alien_corre:
            self.corre()
        if self.alien_pula:
            self.pula()

        if self.passo_index >= 10:
            self.passo_index = 0

        if usIn[pygame.K_UP] and not self.alien_pula:
            self.alien_agaixa = False
            self.alien_corre = False
            self.alien_pula = True
        elif usIn[pygame.K_DOWN] and not self.alien_pula:
            self.alien_agaixa = True
            self.alien_corre = False
            self.alien_pula = False
        elif not (self.alien_pula or usIn[pygame.K_DOWN]):
            self.alien_agaixa = False
            self.alien_corre = True
            self.alien_pula = False

    def agaixa(self):
        self.image = self.agaixa_img[self.passo_index // 5]
        self.alien_rect = self.image.get_rect()
        self.alien_rect.x = self.X_POS
        self.alien_rect.y = self.Y_POS_AG
        self.passo_index += 1

    def corre(self):
        self.image = self.corre_img[self.passo_index // 5]
        self.alien_rect = self.image.get_rect()
        self.alien_rect.x = self.X_POS
        self.alien_rect.y = self.Y_POS
        self.passo_index += 1

    def pula(self):
        self.image = self.pula_img
        if self.alien_pula:
            self.alien_rect.y -= self.pulo_vel * 4
            self.pulo_vel -= 0.8
        if self.pulo_vel < - self.vel_pulo:
            self.alien_pula = False
            self.pulo_vel = self.vel_pulo

    def muda(self, win):
        win.blit(self.image, (self.alien_rect.x, self.alien_rect.y))

# MAIN

def main():
    global velocidade, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()    
    velocidade = 20
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.SysFont(None, 30)
    obstacles = []
    death_count = 0
    plat1 = Platform(PLAT)
    player = Alien()

    def pontos():
        global points, velocidade
        points += 1
        if points % 100 == 0:
            velocidade += 1

        text = font.render("Pontuação: " + str(points), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (800, 40)
        win.blit(text, textRect)

    def background():

        global x_pos_bg, y_pos_bg

        if points <= 100:
            image_width = BG.get_width()
            win.blit(BG, (x_pos_bg, y_pos_bg))
            win.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            if x_pos_bg <= -image_width:
                win.blit(BG, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            x_pos_bg -= velocidade

        elif points <= 200 and points > 100:

            image_width2 = BG2.get_width()
            win.blit(BG2, (x_pos_bg, y_pos_bg))
            win.blit(BG2, (image_width2 + x_pos_bg, y_pos_bg))
            if x_pos_bg <= -image_width2:
                win.blit(BG2, (image_width2 + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            x_pos_bg -= velocidade

        elif points <= 300 and points > 200:

            image_width2 = BG3.get_width()
            win.blit(BG3, (x_pos_bg, y_pos_bg))
            win.blit(BG3, (image_width2 + x_pos_bg, y_pos_bg))
            if x_pos_bg <= -image_width2:
                win.blit(BG3, (image_width2 + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            x_pos_bg -= velocidade

        elif points <= 400 and points > 300:

            image_width2 = BG4.get_width()
            win.blit(BG4, (x_pos_bg, y_pos_bg))
            win.blit(BG4, (image_width2 + x_pos_bg, y_pos_bg))
            if x_pos_bg <= -image_width2:
                win.blit(BG4, (image_width2 + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            x_pos_bg -= velocidade

        elif points <= 500 and points > 400:

            image_width2 = BG5.get_width()
            win.blit(BG5, (x_pos_bg, y_pos_bg))
            win.blit(BG5, (image_width2 + x_pos_bg, y_pos_bg))
            if x_pos_bg <= -image_width2:
                win.blit(BG5, (image_width2 + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            x_pos_bg -= velocidade

        elif points <= 600 and points > 500:

            image_width2 = BG6.get_width()
            win.blit(BG6, (x_pos_bg, y_pos_bg))
            win.blit(BG6, (image_width2 + x_pos_bg, y_pos_bg))
            if x_pos_bg <= -image_width2:
                win.blit(BG6, (image_width2 + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            x_pos_bg -= velocidade

        elif points <= 700 and points > 600:

            image_width2 = BG7.get_width()
            win.blit(BG7, (x_pos_bg, y_pos_bg))
            win.blit(BG7, (image_width2 + x_pos_bg, y_pos_bg))
            if x_pos_bg <= -image_width2:
                win.blit(BG7, (image_width2 + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            x_pos_bg -= velocidade

        elif points <= 800 and points > 700:

            image_width2 = BG8.get_width()
            win.blit(BG8, (x_pos_bg, y_pos_bg))
            win.blit(BG8, (image_width2 + x_pos_bg, y_pos_bg))
            if x_pos_bg <= -image_width2:
                win.blit(BG8, (image_width2 + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            x_pos_bg -= velocidade

        elif points > 800:

            image_width2 = BG9.get_width()
            win.blit(BG9, (x_pos_bg, y_pos_bg))
            win.blit(BG9, (image_width2 + x_pos_bg, y_pos_bg))
            if x_pos_bg <= -image_width2:
                win.blit(BG9, (image_width2 + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            x_pos_bg -= velocidade

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        background()

        player.muda(win)

        plat1.muda(win)

        player.att(userInput)

        plat1.update()

        pontos()

        clock.tick(30)
        pygame.display.update()

def menu(death_count):

    global points

    run = True

    while run:
        win.fill((255, 255, 255))
        image_width = BG.get_width()
        image_height = BG.get_height()
        win.blit(BG, (image_width, image_height))
        font = pygame.font.SysFont(None, 30)

        if death_count == 0:
            text = font.render("Aperte as setas para começar", True, (0, 0, 0))
            text2 = font.render("Somente as setas serão usadas durante o jogo", True, (0, 0, 0))

        elif death_count > 0:
            text = font.render("Aperte as setas para começar", True, (0, 0, 0))
            text2 = font.render("Somente as setas serão usadas durante o jogo", True, (0, 0, 0))
            score = font.render("Sua Pontuação: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (500, 300)
            win.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (490, 250)

        textRect2 = text2.get_rect()
        textRect2.center = (490, 300)

        win.blit(text, textRect)
        win.blit(text2, textRect2)
        win.blit(CORRER[0], (440, 110))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)