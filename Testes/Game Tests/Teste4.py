import pygame
import os
import random

pygame.init()
pygame.mixer.init()

win = pygame.display.set_mode((950, 500))

bg_img = pygame.image.load("Assets/Image/City5.jpg")
bg_img2 = pygame.image.load("Assets/Image/City3.jpg")
bg_img3 = pygame.image.load("Assets/Image/City4.jpg")
bg_img4 = pygame.image.load("Assets/Image/City6.jpg")
bg_img5 = pygame.image.load("Assets/Image/City7.jpg")
bg_img6 = pygame.image.load("Assets/Image/City8.jpg")
bg_img7 = pygame.image.load("Assets/Image/City9.jpg")
bg_img8 = pygame.image.load("Assets/Image/City.gif")
bg_img9 = pygame.image.load("Assets/Image/City2_1.jpg")
mn = pygame.image.load("Assets/Image/Nave.jpg")
nvz = pygame.image.load("Assets/Image/Navezinha.png")
rocket_img = pygame.image.load("Assets/Other/rocket.png").convert_alpha()
obs_img1 = pygame.image.load('Assets/Other/barreira1.jpg') 
obs_img2 = pygame.image.load('Assets/Other/barreira2.png')
obs_img3 = pygame.image.load('Assets/Other/parede.png')
gameover = pygame.image.load('Assets/Image/GameOver.jpg')
tiles = pygame.image.load('Assets\Image\FullTiles.png')
stop = pygame.image.load('Assets\Other\Stop.png').convert_alpha()


BG = pygame.transform.scale(bg_img, (1000, 500))
BG2 = pygame.transform.scale(bg_img2, (1000, 500))
BG3 = pygame.transform.scale(bg_img3, (1000, 500))
BG4 = pygame.transform.scale(bg_img4, (1000, 500))
BG5 = pygame.transform.scale(bg_img5, (1000, 500))
BG6 = pygame.transform.scale(bg_img6, (1000, 500))
BG7 = pygame.transform.scale(bg_img7, (1000, 500))
BG8 = pygame.transform.scale(bg_img8, (1000, 500))
BG9 = pygame.transform.scale(bg_img9, (1000, 500))
MN = pygame.transform.scale(mn, (1000, 500))
OBS1 = pygame.transform.scale(stop, (70, 110))
OBS2 = pygame.transform.scale(obs_img2, (150, 150))
OBS3 = pygame.transform.scale(obs_img3, (100, 100))
GO = pygame.transform.scale(bg_img, (1000, 500))
TL = pygame.transform.scale(tiles, (1000, 100))


CORRER = [pygame.image.load(os.path.join("Assets/Player", "p1_walk01.png")),
           pygame.image.load(os.path.join("Assets/Player", "p1_walk03.png"))]

PULAR = pygame.image.load(os.path.join("Assets/Player", "p1_jump.png"))

AGAIXAR = [pygame.image.load(os.path.join("Assets/Player", "p1_down7.png")), 
           pygame.image.load(os.path.join("Assets/Player", "p1_down8.png"))]

DISP = pygame.image.load(os.path.join("Assets/Player", "p1_walk012.png"))

ROCK = pygame.transform.scale(rocket_img, (140, 70))

NAVEZINHA = [pygame.image.load(os.path.join("Assets/Image", "Navezinha.png")), 
            pygame.image.load(os.path.join("Assets/Image", "Navezinha.png"))]
HIDRA = pygame.image.load(os.path.join("Assets/Image", "Hidrante.jpg"))
PLACA = pygame.image.load(os.path.join("Assets/Image", "Hidrante.jpg"))

pygame.mixer.music.load("Assets/snd/DARUDE.mp3")
pygame.mixer.music.set_volume(0.4)    

class Alien:
    X_POS = 80
    Y_POS = 375
    Y_POS_AG = 397
    vel_pulo = 8.5

    def __init__(self):

        #Var
        self.agaixa_img = AGAIXAR
        self.corre_img = CORRER
        self.pula_img = PULAR

        # Come??a correndo sem estar agaixado ou pulando:
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

    # Personagem agaixa
    def agaixa(self):
        self.image = self.agaixa_img[self.passo_index // 5]
        self.alien_rect = self.image.get_rect()
        self.alien_rect.x = self.X_POS
        self.alien_rect.y = self.Y_POS_AG
        self.passo_index += 1

    # Personagem corre
    def corre(self):
        self.image = self.corre_img[self.passo_index // 5]
        self.alien_rect = self.image.get_rect()
        self.alien_rect.x = self.X_POS
        self.alien_rect.y = self.Y_POS
        self.passo_index += 1
    
    # Personagem pula
    def pula(self):
        self.image = self.pula_img
        if self.alien_pula:
            self.alien_rect.y -= self.pulo_vel * 5
            self.pulo_vel -= 0.8
        if self.pulo_vel < - self.vel_pulo:
            self.alien_pula = False
            self.pulo_vel = self.vel_pulo

    # Personagem aparece
    def muda(self, win):
        win.blit(self.image, (self.alien_rect.x, self.alien_rect.y))


class Obstaculo:

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = 1000

    def update(self):
        self.rect.x -= velocidade
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, win):
        win.blit(self.image, self.rect)


class Barreira(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 370


class Cone(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 360


class Naves(Obstaculo):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(250, 450)
        self.index = 0

    def draw(self, win):
        if self.index >= 9:
            self.index = 0
        win.blit(self.image, self.rect)
        self.index += 1

class Zero(Obstaculo):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 1100
        self.index = 0

    def draw(self, win):
        if self.index >= 9:
            self.index = 0
        win.blit(self.image, self.rect)
        self.index += 1


# Fun????o principal do jojo
def main():
    global velocidade, x_pos_bg, y_pos_bg, points, obstacles, x_tiles
    run = True
    clock = pygame.time.Clock()
    player = Alien()    
    velocidade = 20
    x_pos_bg = 0
    x_tiles = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.SysFont(None, 30)
    obstacles = []
    perdeu = 0
    

    # Fun????o para a pontua????o
    def pontos():
        global points, velocidade
        points += 1
        if points % 100 == 0:
            velocidade += 1

        # Faz a pontua????o aparecer na tela
        text = font.render("Pontua????o: " + str(points), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (800, 40)
        win.blit(text, textRect)

    # Fun????o para o background
    def background():

        global x_pos_bg, y_pos_bg, x_tiles

        ytl = 460
        image_width = BG.get_width()
        image_width_t = TL.get_width()




        # Faz com que o background mude conforme a pontua????o aumenta
        if points <= 1000:

            win.blit(BG, (x_pos_bg, y_pos_bg))
            win.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            win.blit(TL, (x_tiles, ytl))
            win.blit(TL, (image_width_t + x_tiles, ytl))

            if x_pos_bg <= -image_width:
                win.blit(BG, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            if x_tiles <= -image_width_t:
                win.blit(TL, (image_width_t + x_tiles, ytl))
                x_tiles = 0

            x_pos_bg -= velocidade
            x_tiles -= velocidade

        elif points <= 2000 and points > 1000:

            win.blit(BG2, (x_pos_bg, y_pos_bg))
            win.blit(BG2, (image_width + x_pos_bg, y_pos_bg))
            win.blit(TL, (x_tiles, ytl))
            win.blit(TL, (image_width_t + x_tiles, ytl))

            if x_pos_bg <= -image_width:
                win.blit(BG2, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = 0

            if x_tiles <= -image_width_t:
                win.blit(TL, (image_width_t + x_tiles, ytl))
                x_tiles = 0

            x_pos_bg -= velocidade
            x_tiles -= velocidade

        elif points <= 3000 and points > 2000:

            win.blit(BG3, (x_pos_bg, y_pos_bg))
            win.blit(BG3, (image_width + x_pos_bg, y_pos_bg))
            win.blit(TL, (x_tiles, ytl))
            win.blit(TL, (image_width_t + x_tiles, ytl))

            if x_pos_bg <= -image_width:
                win.blit(BG3, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            if x_tiles <= -image_width_t:
                win.blit(TL, (image_width_t + x_tiles, ytl))
                x_tiles = 0

            x_pos_bg -= velocidade
            x_tiles -= velocidade

        elif points <= 4000 and points > 3000:

            win.blit(BG4, (x_pos_bg, y_pos_bg))
            win.blit(BG4, (image_width + x_pos_bg, y_pos_bg))
            win.blit(TL, (x_tiles, ytl))
            win.blit(TL, (image_width_t + x_tiles, ytl))

            if x_pos_bg <= -image_width:
                win.blit(BG4, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            if x_tiles <= -image_width_t:
                win.blit(TL, (image_width_t + x_tiles, ytl))
                x_tiles = 0

            x_pos_bg -= velocidade
            x_tiles -= velocidade

        elif points <= 5000 and points > 4000:

            win.blit(BG5, (x_pos_bg, y_pos_bg))
            win.blit(BG5, (image_width + x_pos_bg, y_pos_bg))
            win.blit(TL, (x_tiles, ytl))
            win.blit(TL, (image_width_t + x_tiles, ytl))

            if x_pos_bg <= -image_width:
                win.blit(BG5, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            if x_tiles <= -image_width_t:
                win.blit(TL, (image_width_t + x_tiles, ytl))
                x_tiles = 0

            x_pos_bg -= velocidade
            x_tiles -= velocidade

        elif points <= 6000 and points > 5000:

            win.blit(BG6, (x_pos_bg, y_pos_bg))
            win.blit(BG6, (image_width + x_pos_bg, y_pos_bg))
            win.blit(TL, (x_tiles, ytl))
            win.blit(TL, (image_width_t + x_tiles, ytl))

            if x_pos_bg <= -image_width:
                win.blit(BG6, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            if x_tiles <= -image_width_t:
                win.blit(TL, (image_width_t + x_tiles, ytl))
                x_tiles = 0

            x_pos_bg -= velocidade
            x_tiles -= velocidade

        elif points <= 7000 and points > 6000:

            win.blit(BG7, (x_pos_bg, y_pos_bg))
            win.blit(BG7, (image_width + x_pos_bg, y_pos_bg))
            win.blit(TL, (x_tiles, ytl))
            win.blit(TL, (image_width_t + x_tiles, ytl))
            
            if x_pos_bg <= -image_width:
                win.blit(BG7, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            if x_tiles <= -image_width_t:
                win.blit(TL, (image_width_t + x_tiles, ytl))
                x_tiles = 0

            x_pos_bg -= velocidade
            x_tiles -= velocidade

        elif points <= 8000 and points > 7000:

            win.blit(BG8, (x_pos_bg, y_pos_bg))
            win.blit(BG8, (image_width + x_pos_bg, y_pos_bg))
            win.blit(TL, (x_tiles, ytl))
            win.blit(TL, (image_width_t + x_tiles, ytl))

            if x_pos_bg <= -image_width:
                win.blit(BG8, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            if x_tiles <= -image_width_t:
                win.blit(TL, (image_width_t + x_tiles, ytl))
                x_tiles = 0

            x_pos_bg -= velocidade
            x_tiles -= velocidade

        elif points > 8000:

            win.blit(BG9, (x_pos_bg, y_pos_bg))
            win.blit(BG9, (image_width + x_pos_bg, y_pos_bg))
            win.blit(TL, (x_tiles, ytl))
            win.blit(TL, (image_width_t + x_tiles, ytl))

            if x_pos_bg <= -image_width:
                win.blit(BG9, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = 0

            if x_tiles <= -image_width_t:
                win.blit(TL, (image_width_t + x_tiles, ytl))
                x_tiles = 0

            x_pos_bg -= velocidade
            x_tiles -= velocidade

    # Update do que ir?? aparecer na tela
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill((255, 255, 255))

        userInput = pygame.key.get_pressed()
        


        background()

        if len(obstacles) == 0:
            if points < 1000:
                z = random.randint(0, 3)
                if z == 0:
                    obstacles.append(Cone(OBS2))
                elif z == 1:
                    obstacles.append(Barreira(OBS1))
                elif z == 2 or z == 3:
                    obstacles.append(Zero(ROCK))

            elif points >= 1000 and points < 2000:
                z2 = random.randint(0, 3)
                if z2 == 3:
                    obstacles.append(Naves(ROCK))
                elif z2 == 0:
                    obstacles.append(Cone(OBS2))
                elif z2 == 1:
                    obstacles.append(Barreira(OBS1))
                elif z2 == 2:
                    obstacles.append(Zero(ROCK))

            elif points >= 2000 and points < 3000:
                z3 = random.randint(0, 5)
                if z3 == 3:
                    obstacles.append(Naves(ROCK))
                elif z3 == 0:
                    obstacles.append(Cone(OBS2))
                elif z3 == 1:
                    obstacles.append(Barreira(OBS1))
                elif z3 == 5 or 2:
                    obstacles.append(Zero(ROCK))

            elif points >= 3000 and points < 4000:
                z4 = random.randint(0, 6)
                if z4 == 3:
                    obstacles.append(Naves(ROCK))
                elif z4 == 0 or 2:
                    obstacles.append(Cone(OBS2))
                elif z4 == 1:
                    obstacles.append(Barreira(OBS1))
                elif z4 == 5 or 6:
                    obstacles.append(Zero(ROCK))


            elif points >= 4000 and points < 5000:
                z5 = random.randint(0, 7)
                if z5 == 3:
                    obstacles.append(Naves(ROCK))
                elif z5 == 0 or 2:
                    obstacles.append(Cone(OBS2))
                elif z5 == 1 or 7:
                    obstacles.append(Barreira(OBS1))
                elif z5 == 5 or 6:
                    obstacles.append(Zero(ROCK))

            elif points >= 5000 and points < 6000:
                z6 = random.randint(0, 8)
                if z6 == 3:
                    obstacles.append(Naves(ROCK))
                elif z6 == 0 or 2:
                    obstacles.append(Cone(OBS2))
                elif z6 == 1 or 7:
                    obstacles.append(Barreira(OBS1))
                elif z6 == 5 or 6 or z6 == 8:
                    obstacles.append(Zero(ROCK))

            elif points >= 7000:
                z7 = random.randint(0, 9)
                if z7 == 3 or z7 == 7:
                    obstacles.append(Naves(ROCK))
                elif z7 == 0:
                    obstacles.append(Cone(OBS2))
                elif z7 == 1:
                    obstacles.append(Barreira(OBS1))
                elif z7 == 5 or z7 == 6:
                    obstacles.append(Zero(ROCK))


        for obstacle in obstacles:
            obstacle.draw(win)
            obstacle.update()
            if player.alien_rect.colliderect(obstacle.rect):
                win.blit(GO, (0, 0))
                pygame.time.delay(1000)
                perdeu += 1
                menu(perdeu)

        player.muda(win)

        player.att(userInput)

        pontos()

        clock.tick(30)
        
        pygame.display.update()


# Ultima fun????o, que apresentar?? o "menu" principal do jogo, e apresenta algumas regras
def menu(perdeu):

    pygame.mixer.music.pause()
    
    global points

    run = True

    while run:
        
        # Faz o background do menu

        win.fill((255, 255, 255))
        win.blit(MN, (0, 0))

        font = pygame.font.SysFont(None, 35)
        font2 = pygame.font.SysFont(None, 50)
 
        # Apresenta dicas e como iniciar o jogo
        if perdeu == 0:
            text = font2.render("Aperte as setas para come??ar", 50, (0, 255, 0))
            text2 = font.render("Somente as setas ser??o usadas durante o jogo", True, (255, 233, 0))
            text3 = font.render("N??o encoste em nenhum obst??culo!!!", True, (255, 0, 80))

        elif perdeu > 0:
            
            text = font2.render("Aperte as setas para come??ar", True, (0, 255, 0))
            text2 = font.render("Somente as setas ser??o usadas durante o jogo", True, (255, 233, 0))
            text3 = font.render("N??o encoste em nenhum obst??culo!!!", True, (255, 0, 80))
            score = font.render("Sua Pontua????o: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (490, 370)
            win.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (490, 130)

        textRect2 = text2.get_rect()
        textRect2.center = (490, 435)

        textRect3 = text3.get_rect()
        textRect3.center = (490, 470)

        win.blit(text, textRect)
        win.blit(text2, textRect2)
        win.blit(text3, textRect3)
        win.blit(DISP, (440, 200))

        pygame.display.update()
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                pygame.mixer.music.play(loops=-1)
                main()

menu(perdeu=0)