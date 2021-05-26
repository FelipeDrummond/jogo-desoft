class Obstaculo:

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = 1000

    def update(self):
        self.rect.x -= velocidade
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, win):
        win.blit(self.image[self.type], self.rect)


class SmallCactus(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstaculo):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstaculo):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, win):
        if self.index >= 9:
            self.index = 0
        win.blit(self.image[self.index//5], self.rect)
        self.index += 1