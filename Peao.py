import pygame
import math
from math import *

class Peao():
    def __init__(self, x, y, imagem):
        self.__x = x
        self.__y = y
        self.__raio = 20
        self.__angulo = radians(0)
        self.__velocidade = 0
        self.__atrito = 0.075
        self.__imagem = pygame.transform.scale(imagem, [40, 40])

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

    def desenha_peao(self, janela):
        janela.blit(self.__imagem, (self.__x, self.__y))

    def move(self):
        self.__velocidade -= self.__atrito
        if self.__velocidade <= 0:
            self.__velocidade = 0
        self.__x += math.sin(self.__angulo) * self.__velocidade
        self.__y -= math.cos(self.__angulo) * self.__velocidade


    def mouse_sobre(self, pos):
        if pos[0] > self.__x and pos[0] < self.__x + 40 :
            if pos[1] > self.__y and pos[1] < self.__y + 40:
                return True

        return False