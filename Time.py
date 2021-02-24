
import pygame
from Peao import Peao, Goleiro
from Campo import Lado_do_campo

class Time:
    def __init__(self, nome, brasao_jogador, brasao_goleiro, lado_do_campo=Lado_do_campo().esquerdo):
        self.nome = nome
        self.lado_do_campo = lado_do_campo
        self.jogador_1 = Peao(brasao_jogador, self.lado_do_campo[0]).peao
        self.jogador_2 = Peao(brasao_jogador, self.lado_do_campo[1]).peao
        self.jogador_3 = Peao(brasao_jogador, self.lado_do_campo[2]).peao
        self.jogador_4 = Peao(brasao_jogador, self.lado_do_campo[3]).peao
        self.jogador_5 = Peao(brasao_jogador, self.lado_do_campo[4]).peao
        self.goleiro = Goleiro(brasao_goleiro, self.lado_do_campo[5]).goleiro


    def desenhar(self, janela):
        grupo = pygame.sprite.Group()
        grupo.add(self.jogador_1)
        grupo.add(self.jogador_2)
        grupo.add(self.jogador_3)
        grupo.add(self.jogador_4)
        grupo.add(self.jogador_5)
        grupo.add(self.goleiro)
        grupo.draw(janela)
