import pygame


class Peao:
    def __init__(imagem, cor=(0,0,0), raio=80, posicao=(100, 100)):
        self.
        self.cor = cor
        self.raio = raio
        self.posicao = posicao

        avai1 = pygame.sprite.Sprite(grupo)
        avai1.image = pygame.image.load('brasao_avai.png')
        avai1.image = pygame.transform.scale(avai1.image, [80, 80])
        pygame.sprite.collide_circle()
        avai1.rect = pygame.Rect(50, 50, 80, 80)


    def desenha_peao(self):

        peao = pygame.sprite.Sprite()
        peao.image =