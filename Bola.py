import pygame

class Bola():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__sprit = pygame.sprite.Sprite()
        self.__sprit.image = pygame.image.load('imagens/bola.png')
        self.__sprit.image = pygame.transform.scale(self.__sprit.image, [30, 30])
        self.__sprit.rect = pygame.Rect(self.__x, self.__y , 30, 30)

    def desenha_bola(self, janela):
        grupo = pygame.sprite.Group()
        grupo.add(self.__sprit)
        grupo.draw(janela)



