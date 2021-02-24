
import pygame
from Peao import Peao

class Time:
    def __init__(self, nome, brasao):
        self.nome = nome
        self.brasao = brasao
        self.jogador_1 = Peao(brasao, (500, 100)).peao
        self.jogador_2 = Peao(brasao, (500, 500)).peao
        self.jogador_3 = Peao(brasao, (800, 100)).peao
        self.jogador_4 = Peao(brasao, (800, 500)).peao
        self.jogador_5 = Peao(brasao, (650, 300)).peao


    def desenhar(self, janela):
        cor = pygame.Surface
        grupo = pygame.sprite.Group()
        grupo.add(self.jogador_1)
        grupo.add(self.jogador_2)
        grupo.add(self.jogador_3)
        grupo.add(self.jogador_4)
        grupo.add(self.jogador_5)


        grupo.draw(janela)
