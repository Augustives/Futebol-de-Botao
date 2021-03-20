
import pygame
from Peao import Peao
from Goleiro import Goleiro
from Lado_campo import Lado_do_campo

class Time:
    def __init__(self, nome, brasao_peao, brasao_goleiro, lado_do_campo, space):
        self.__nome = nome
        self.__lado_do_campo = lado_do_campo
        self.__brasao_peao = pygame.image.load(brasao_peao)
        self.__brasao_goleiro = pygame.image.load(brasao_goleiro)
        self.__posicoes = lado_do_campo
        self.__space = space

        self.__peao_1 = Peao(self.__posicoes[0][0],self.__posicoes[0][1], self.__brasao_peao, self.__space)
        self.__peao_2 = Peao(self.__posicoes[1][0], self.__posicoes[1][1], self.__brasao_peao, self.__space)
        self.__peao_3 = Peao(self.__posicoes[2][0], self.__posicoes[2][1], self.__brasao_peao, self.__space)
        self.__peao_4 = Peao(self.__posicoes[3][0], self.__posicoes[3][1], self.__brasao_peao, self.__space)
        self.__peao_5 = Peao(self.__posicoes[4][0], self.__posicoes[4][1], self.__brasao_peao, self.__space)
        self.__goleiro = Goleiro(self.__posicoes[5][0], self.__posicoes[5][1], self.__brasao_goleiro, self.__space)

        self.__lista_peao = [self.__peao_1, self.__peao_2, self.__peao_3, self.__peao_4, self.__peao_5]


    @property
    def lista_peao(self):
        return self.__lista_peao

    @property
    def goleiro(self):
        return self.__goleiro

    def desenha_time(self, janela):
        for i in self.__lista_peao:
            i.desenha_peao(janela)
        self.__goleiro.desenha_goleiro(janela)
