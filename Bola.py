import pygame

class Bola():
    def __init__(self, posicao):
        self.imagem = 'imagens/bola.png'
        self.posicao = posicao
        self.bola = pygame.sprite.Sprite()

        self.bola.image = pygame.image.load(self.imagem)
        self.bola.image = pygame.transform.scale(self.bola.image, [30, 30])

        self.bola.rect = pygame.Rect(posicao[0], posicao[1], 30, 30)

    def desenhar(self, janela):
        grupo = pygame.sprite.Group()
        grupo.add(self.bola)
        grupo.draw(janela)