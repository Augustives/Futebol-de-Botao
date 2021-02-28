import pygame
from math import *

class Palheta:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__comprimento = 100
        self.__tangente = 0

    def aplica_forca(self, alvo, forca):
        alvo.angulo = self.__tangente
        alvo.velocidade = forca

    def desenha_palheta(self, alvo,  janela):
        self.__x, self.__y = pygame.mouse.get_pos()
        self.__tangente = atan2((alvo.y+20 - self.__y), (alvo.x+20 - self.__x)) + 1.5708
        pygame.draw.line(janela,(0,0,255), (self.__x, self.__y), (alvo.x+20, alvo.y+20), 3)


