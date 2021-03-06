import pygame
import pymunk
from Lado_campo import Lado_do_campo
from Time import Time
from Bola import  Bola

class Campo():

    def __init__(self):
        self.__space = pymunk.Space()
        self.__bola = self.__bola = Bola(860, 380, self.__space)
        self.__gol = None
        self.__laterais = pygame.sprite.Group()
        self.__esquerdo = [(500, 200), (500, 575), (790, 200), (790, 575), (650, 375), (455, 400)]
        self.__direito = [(1175, 200), (1175, 575), (890, 200), (890, 575), (1010, 375), (1255, 400)]
        self.__time1 = None
        self.__time2 = None

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

    def colisao_campo(self):
        Lado_do_campo([420, 100], [420, 655], self.__space, 2)
        Lado_do_campo([1290, 100], [1290, 655], self.__space, 2)
        Lado_do_campo([420, 100], [1290, 100], self.__space, 2)
        Lado_do_campo([420, 655], [1290, 655], self.__space, 2)

    def reset(self):
        self.__space = pymunk.Space()

    def desenha_campo(self, janela):
        grupo = pygame.sprite.Group()
        gramado = pygame.sprite.Sprite(grupo)
        gramado.image = pygame.image.load('imagens/grama.png')
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