
import pygame
from Peao import Peao

class Time:
    def __init__(self, nome, brasao):
        self.nome = nome
        self.brasao = brasao
        self.jogador_1 = Peao()
        self.jogador_2 = Peao()
        self.jogador_3 = Peao()
        self.jogador_4 = Peao()
        self.jogador_5 = Peao()
        self.goleiro = Peao()