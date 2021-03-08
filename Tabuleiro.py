import pygame

import pymunk

import sys
from BotaoMenu import Botao
from Campo import Campo
from Lado_campo import Lado_do_campo
from Placar import Placar
from BarraForca import BarraForca
from Time import Time
from Bola import Bola
from Palheta import Palheta


class Tabuleiro:
    def __init__(self, janela):
        self.__janela = janela
        self.__space = pymunk.Space()
        self.__clock = pygame.time.Clock()
        self.__botaoVoltar = Botao(90, 600, 250, 100, "Voltar")
        self.__placar = Placar(40, 100, 350, 60)
        self.__barraForca = BarraForca(65, 500, 300, 30)
        self.__campo = Campo()
        self.__time_1 = Time('Figueirence', 'imagens/brasao_figueirence.png', 'imagens/brasao_figueirence_goleiro.png'
                             , self.__campo.esquerdo, self.__space )
        self.__time_2 = Time('Avai', 'imagens/brasao_avai.png', 'imagens/brasao_avai_goleiro.png'
                             , self.__campo.direito, self.__space)
        self.__bola = Bola(860, 380, self.__space)
        self.__palheta = Palheta()


    def desenha_tabuleiro(self):
        self.__janela.fill((200, 200, 200))
        self.__placar.desenha_placar(self.__janela)
        self.__botaoVoltar.desenha_botao(self.__janela)
        self.__campo.desenha_campo(self.__janela)
        self.__time_1.desenha_time(self.__janela)
        self.__time_2.desenha_time(self.__janela)
        self.__bola.desenha_bola(self.__janela)

    def colisao_campo(self):
        Lado_do_campo([420, 100], [420, 655], self.__space, 2)
        Lado_do_campo([1290, 100], [1290, 655], self.__space, 2)
        Lado_do_campo([420, 100], [1290, 100], self.__space, 2)
        Lado_do_campo([420, 655], [1290, 655], self.__space, 2)

    def atrito(self):
        self.__bola.atrito()
        for i in (self.__time_1.lista_peao + self.__time_2.lista_peao):
            i.atrito()

    def vez_de_quem(self):
        pass

    def loop(self):
        jogo_aberto = True
        self.colisao_campo()
        barra_mov = 0
        gol_mov = 0
        while jogo_aberto:
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        jogo_aberto = False
                    if event.key == pygame.K_s:
                        gol_mov = 3.5
                    if event.key == pygame.K_a:
                        gol_mov = -3.5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s or event.key == pygame.K_a:
                        gol_mov = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__botaoVoltar.mouse_sobre(pos):
                        jogo_aberto = False

                self.__palheta.aplica_impulso(event, self.__time_1.lista_peao, self.__time_2.lista_peao, pos, self.__janela)
                self.__botaoVoltar.botao_hover(event, pos)

            self.desenha_tabuleiro()
            self.__palheta.desenha_palheta(pos, self.__janela)
            self.__time_1.goleiro.move(gol_mov)

            self.atrito()




            self.__clock.tick(60)
            self.__space.step(2 / 60)
            pygame.display.update()
