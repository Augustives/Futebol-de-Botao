import pygame


class Peao:
    def __init__(self, imagem, posicao):
        self.imagem = imagem
        self.posicao = posicao
        self.peao = pygame.sprite.Sprite()

        imagem = 'imagens/brasao_figueirence.png'

        self.peao.image = pygame.image.load(imagem)
        self.peao.image = pygame.transform.scale(self.peao.image, [80, 80])

        self.peao.rect = pygame.Rect(posicao[0], posicao[1], 80, 80)

