import pygame
import pymunk
from Model.Lado_campo import Lado_do_campo
from Model.Time import Time
from Model.Bola import Bola
from Model.Gol import Gol

class Campo():

    def __init__(self):
        self.__space = pymunk.Space()
        self.__bola = Bola(860, 380, self.__space)
        self.__gol = Gol()
        self.__laterais = pygame.sprite.Group()
        self.__esquerdo = [(530, 200), (530, 575), (790, 200), (790, 575), (700, 375), (455, 400)]
        self.__direito = [(1175, 200), (1175, 575), (930, 200), (930, 575), (1010, 375), (1255, 400)]

        self.__time1 = None
        self.__time2 = None
        self.__gols1 = 0
        self.__gols2 = 0

        self.__turno_atual = 1
        self.__turno_max = 99

        self.__vez, self.__primeira_rodada = 1, True
        self.__nao_moveu = True
        self.__gol_mov = 0

    @property
    def gols1(self):
        return self.__gols1

    @gols1.setter
    def gols1(self, value):
        self.__gols1 = value

    @property
    def gols2(self):
        return self.__gols2

    @gols2.setter
    def gols2(self, value):
        self.__gols2 = value

    @property
    def vez(self):
        return self.__vez

    @vez.setter
    def vez(self, value):
        self.__vez = value

    @property
    def primeira_rodade(self):
        return self.__primeira_rodada

    @primeira_rodade.setter
    def primeira_rodade(self, value):
        self.__primeira_rodada = value

    @property
    def nao_moveu(self):
        return self.__nao_moveu

    @nao_moveu.setter
    def nao_moveu(self, value):
        self.__nao_moveu = value

    @property
    def gol_mov(self):
        return self.__gol_mov

    @gol_mov.setter
    def gol_mov(self, value):
        self.__gol_mov = value

    @property
    def turno_atual(self):
        return self.__turno_atual

    @turno_atual.setter
    def turno_atual(self, turnos):
        self.__turno_atual = turnos

    @property
    def turno_max(self):
        return self.__turno_max

    @turno_max.setter
    def turno_max(self, turnos):
        self.__turno_max = turnos

    @property
    def space(self):
        return self.__space

    @property
    def time1(self):
        return self.__time1

    @property
    def time2(self):
        return self.__time2

    @property
    def bola(self):
        return self.__bola

    @property
    def gol(self):
        return self.__gol

    def colisao_campo(self):
        Lado_do_campo([420, 100], [420, 655], self.__space, 2)
        Lado_do_campo([1290, 100], [1290, 655], self.__space, 2)
        Lado_do_campo([420, 100], [1290, 100], self.__space, 2)
        Lado_do_campo([420, 655], [1290, 655], self.__space, 2)

    def atrito(self):
        self.__bola.atrito()
        for i in (self.__time1.lista_peao + self.__time2.lista_peao):
            i.atrito()

    def desenha_campo(self, janela):
        grupo = pygame.sprite.Group()
        gramado = pygame.sprite.Sprite(grupo)
        gramado.image = pygame.image.load('./imagens/grama.png')
        gramado.image = pygame.transform.scale(gramado.image, [900, 600])
        gramado.rect = pygame.Rect(430, 100, 900, 600, )
        grupo.draw(janela)
        self.__laterais.add()
        transparente = pygame.Color(255, 255, 255, 255)
        pygame.draw.rect(janela, transparente, (450, 125, 850, 545), width=6)
        pygame.draw.rect(janela, transparente, (450, 270, 100, 260), width=6)
        pygame.draw.rect(janela, transparente, (1200, 270, 100, 260), width=6)
        pygame.draw.circle(janela, transparente, (880, 400), 120, width=6)
        pygame.draw.line(janela, transparente, (880, 125), (880, 670), width=6)
        pygame.draw.circle(janela, (255, 255, 255), (880, 400), 10, )
        self.__time1.desenha_time(janela)
        self.__time2.desenha_time(janela)
        self.__bola.desenha_bola(janela)


    def cria_time(self, escolha1, escolha2):
        if escolha1 == "Ava":
            self.__time1 = Time('Avai', 'imagens/brasao_avai.png', 'imagens/brasao_avai_goleiro.png'
                                , self.__esquerdo, self.__space)
        elif escolha2 =="Ava":
            self.__time2 = Time('Avai', 'imagens/brasao_avai.png', 'imagens/brasao_avai_goleiro.png'
                                , self.__direito, self.__space)
        if escolha1 == "Fig":
            self.__time1 = Time('Figueirence', 'imagens/brasao_figueirence.png', 'imagens/brasao_figueirence_goleiro.png'
                             , self.__esquerdo, self.__space)
        elif escolha2 =="Fig":
            self.__time2 = Time('Figueirence', 'imagens/brasao_figueirence.png', 'imagens/brasao_figueirence_goleiro.png'
                             , self.__direito, self.__space)

    def parado(self):
        if self.__time1.parado() and self.time2.parado() and self.__bola.parado():
            return True
        else:
            return False