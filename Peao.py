import pygame

class Peao():
    def __init__(self, imagem, posicao):
        self.imagem = imagem
        self.posicao = posicao
        self.peao = pygame.sprite.Sprite()
        self.peao.image = pygame.image.load(imagem)
        self.peao.image = pygame.transform.scale(self.peao.image, [80, 80])
        self.peao.rect = pygame.Rect(posicao[0], posicao[1], 80, 80)

class Goleiro():
    def __init__(self, imagem, posicao):
        self.imagem = imagem
        self.posicao = posicao
        self.goleiro = pygame.sprite.Sprite()
        self.goleiro.image = pygame.image.load(imagem)
        self.goleiro.image = pygame.transform.scale(self.goleiro.image, [30, 90])
        self.goleiro.rect = pygame.Rect(posicao[0], posicao[1], 30, 90)