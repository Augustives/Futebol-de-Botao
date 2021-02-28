import pygame
import math

class Bola():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__raio = 20
        self.__angulo = 0.0174533
        self.__velocidade = 0.5
        self.__atrito = 0.050
        self.__imagem = pygame.transform.scale(pygame.image.load('imagens/bola.png'), [40, 40])

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def raio(self):
        return self.__raio

    @property
    def angulo(self):
        return self.__angulo

    @angulo.setter
    def angulo(self, angulo):
        self.__angulo = angulo

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    def move(self):
        self.__velocidade -= self.__atrito
        if self.__velocidade <= 0:
            self.__velocidade = 0
        self.__x += math.sin(self.__angulo) * self.__velocidade
        self.__y -= math.cos(self.__angulo) * self.__velocidade


    def desenha_bola(self, janela):
        janela.blit(self.__imagem, (self.__x, self.__y))



