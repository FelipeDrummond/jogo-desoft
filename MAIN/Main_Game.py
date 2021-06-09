# === INICIALIZAÇÃO ===

# Importanto e iniciando bibliotecas  
import pygame
import os
import random

from pygame.constants import K_s

pygame.init()
pygame.mixer.init()

# Definindo parâmetros
ALT_TELA = 500
LARG_TELA = 950
LA_BG = 1000
FPS = 28
ALT_NAVE = 70
LARG_NAVE = 140
ALT_STOP = 125
LARG_STOP = 85
ALT_CONE = 95
LARG_CONE = 75 
ALT_TILES = 100
LARG_TILES = 1000

# Definindo tamanho da tela 
win = pygame.display.set_mode((LARG_TELA, ALT_TELA))

# Iniciando assets
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
rocket_img = pygame.image.load("Assets/Other/rocket.png").convert_alpha()
obs_img2 = pygame.image.load('Assets/Other/barreira2.png').convert_alpha()
gameover = pygame.image.load('Assets/Image/GameOver.jpg')
tiles = pygame.image.load('Assets\Image\FullTiles.png')
stop = pygame.image.load('Assets\Other\Stop.png').convert_alpha()

# Transformando assets para a escala correta
BG = pygame.transform.scale(bg_img, (LA_BG, ALT_TELA))
BG2 = pygame.transform.scale(bg_img2, (LA_BG, ALT_TELA))
BG3 = pygame.transform.scale(bg_img3, (LA_BG, ALT_TELA))
BG4 = pygame.transform.scale(bg_img4, (LA_BG, ALT_TELA))
BG5 = pygame.transform.scale(bg_img5, (LA_BG, ALT_TELA))
BG6 = pygame.transform.scale(bg_img6, (LA_BG, ALT_TELA))
BG7 = pygame.transform.scale(bg_img7, (LA_BG, ALT_TELA))
BG8 = pygame.transform.scale(bg_img8, (LA_BG, ALT_TELA))
BG9 = pygame.transform.scale(bg_img9, (LA_BG, ALT_TELA))
MN = pygame.transform.scale(mn, (LARG_TELA, ALT_TELA))
OBS1 = pygame.transform.scale(stop, (LARG_STOP, ALT_STOP))
OBS2 = pygame.transform.scale(obs_img2, (LARG_CONE, ALT_CONE))
GO = pygame.transform.scale(gameover, (LARG_TELA, ALT_TELA))
TL = pygame.transform.scale(tiles, (LARG_TILES, ALT_TILES))
ROCK = pygame.transform.scale(rocket_img, (LARG_NAVE, ALT_NAVE))

CORRER = [pygame.image.load(os.path.join("Assets/Player", "p1_walk01.png")),
           pygame.image.load(os.path.join("Assets/Player", "p1_walk03.png"))]

PULAR = pygame.image.load(os.path.join("Assets/Player", "p1_jump.png"))

AGAIXAR = [pygame.image.load(os.path.join("Assets/Player", "p1_down7.png")), 
           pygame.image.load(os.path.join("Assets/Player", "p1_down8.png"))]

DISP = pygame.image.load(os.path.join("Assets/Player", "p1_walk012.png"))

# Carregando arquivos de som
pygame.mixer.music.load("Assets/snd/DARUDE.mp3")
Gameover_snd = pygame.mixer.Sound("Assets/snd/gameover.mp3")
pygame.mixer.music.set_volume(0.4)    

# Iniciando estruturas de dados (classes)
class Alien:
    X_POS = 80
    Y_POS = 375
    Y_POS_AG = 397
    vel_pulo = 10

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

        if (usIn[pygame.K_UP] or usIn[pygame.K_SPACE] or usIn[pygame.K_w]) and not self.alien_pula:
            self.alien_agaixa = False
            self.alien_corre = False
            self.alien_pula = True
        elif (usIn[pygame.K_DOWN] or usIn[pygame.K_s]) and not self.alien_pula:
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
            self.pulo_vel -= 1
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
        self.rect.y = 360


class Cone(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 375


class Naves(Obstaculo):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(250, 370)
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


# Função com o loop principal do jogo
def main():
    global velocidade, x_pos_bg, y_pos_bg, points, obstacles, x_tiles
    run = True
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    player = Alien()    
    velocidade = 20
    x_pos_bg = 0
    x_tiles = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.SysFont(None, 30)
    obstacles = []
    

    # Função para a pontuação
    def pontos():
        global points, velocidade
        points += 1
        if points % 100 == 0:
            velocidade += 1

        # Faz a pontuação aparecer na tela
        text = font.render("Pontuação: " + str(points), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (800, 40)
        win.blit(text, textRect)

    # Função para o background
    def background():

        global x_pos_bg, y_pos_bg, x_tiles

        ytl = 460
        image_width = BG.get_width()
        image_width_t = TL.get_width()




        # Faz com que o background mude conforme a pontuação aumenta
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

    # Update do que irá aparecer na tela
    while run:

        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequência
            if event.type == pygame.QUIT:
                pygame.mixer.music.pause()
                run = False

        win.fill((255, 255, 255))

        usIn = pygame.key.get_pressed()
        


        background()

        # Faz com que a  probabilidade de aparecimento de obstáculos mude conforme o jogo avança
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

        # Analisa possíveis colisões (GAME OVER)
        for obstacle in obstacles:
            obstacle.draw(win)
            obstacle.update()
            if player.alien_rect.colliderect(obstacle.rect):

                pygame.time.delay(500)
                pygame.mixer.music.pause()
                pygame.time.delay(300)
                
                # Caso ocorra uma colisão, invoca a função Game Over
                GameOver()

        # Caso não ocorram colisões, atualiza os elementos do jogo
        player.muda(win)

        player.att(usIn)

        pontos()

        clock.tick(FPS)
        
        pygame.display.update()

# Função que mostra a tela de Game Over
def GameOver():
    perdeu = 1
    # Música de game over
    Gameover_snd.play()
    
    win.blit(GO, (0, 0))

    pygame.display.update()
    pygame.time.delay(4000)

    # Já retorna automaticamente para o menu principal
    menu(perdeu)

# Ultima função, que apresentará o "menu" principal do jogo, e apresenta algumas regras
def menu(perdeu):
    # Pausa música do jogo
    pygame.mixer.music.pause()

    global points

    run = True

    while run:
        
        # Faz o background do menu

        win.blit(MN, (0, 0))

        font = pygame.font.SysFont(None, 35)
        font2 = pygame.font.SysFont(None, 50)
 
        # Apresenta dicas e como iniciar o jogo
        if perdeu == 0:
            text = font2.render("Aperte qualquer tecla para começar", 50, (0, 255, 0))
            text2 = font2.render("Não encoste em nenhum obstáculo!!!", True, (255, 0, 10))

        # Apresenta novamente as dicas, porém, com a adição da pontuação
        elif perdeu > 0:
            
            text = font2.render("Aperte qualquer tecla para começar", True, (0, 255, 0))
            text2 = font2.render("Não encoste em nenhum obstáculo!!!", True, (255, 0, 10))
            score = font.render("Sua Pontuação: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (490, 370)
            win.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (490, 130)

        textRect2 = text2.get_rect()
        textRect2.center = (490, 435)

        win.blit(text, textRect)
        win.blit(text2, textRect2)
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