import pygame

class Goleiro():
    def __init__(self, x, y, imagem):
        self.__x = x
        self.__y = y
        self.__limites = [self.__y+85, self.__y-75]
        self.__imagem = pygame.transform.scale(imagem, [30, 90])

    def desenha_goleiro(self, janela):
        janela.blit(self.__imagem, (self.__x, self.__y))

    def move(self, valor):
        if valor > 0 and (self.__y + valor) < (self.__limites[0]):
            self.__y += valor
        elif valor < 0 and (self.__y + valor) > (self.__limites[1]):
            self.__y += valor