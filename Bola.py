import pygame

class Bola():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__bola = pygame.sprite.Sprite()
        self.__bola.image = pygame.image.load('imagens/bola.png')
        self.__bola.image = pygame.transform.scale(self.__bola.image, [30, 30])
        self.__bola.rect = pygame.Rect(self.__x, self.__y , 30, 30)

    def desenha_bola(self, janela):
        grupo = pygame.sprite.Group()
        grupo.add(self.__bola)
        grupo.draw(janela)



