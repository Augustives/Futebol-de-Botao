
import pygame
from Model.Peao import Peao
from Model.Goleiro import Goleiro


class Time:
    def __init__(self, nome, brasao_peao, brasao_goleiro, posicoes, space):
        self.__nome = nome
        self.__brasao_peao = pygame.image.load(brasao_peao)
        self.__brasao_goleiro = pygame.image.load(brasao_goleiro)
        self.__posicoes = posicoes
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

    @property
    def nome(self):
        return self.__nome

    def desenha_time(self, janela):
        for i in self.__lista_peao:
            i.desenha_peao(janela)
        self.__goleiro.desenha_goleiro(janela)

    def reset(self):
        for i in range(len(self.__lista_peao)):
            self.__lista_peao[i].body.position = self.__posicoes[i][0], self.__posicoes[i][1]
            self.__lista_peao[i].body.velocity = 0, 0
            self.__goleiro.reset()

    def on_move(self):
        for i in self.__lista_peao:
            if i.body.velocity != (0, 0):
                return True

