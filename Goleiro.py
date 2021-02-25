import pygame

class Goleiro():
    def __init__(self, imagem, posicao):
        self.imagem = imagem
        self.posicao = posicao
        self.goleiro = pygame.sprite.Sprite()
        self.goleiro.image = pygame.image.load(imagem)
        self.goleiro.image = pygame.transform.scale(self.goleiro.image, [30, 90])
        self.goleiro.rect = pygame.Rect(posicao[0], posicao[1], 30, 90)