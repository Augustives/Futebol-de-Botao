import pygame
import sys
from BotaoMenu import Botao
from Campo import Campo
from Placar import Placar
from BarraForca import BarraForca
from Palheta import Palheta


class JanelaJogo:
    def __init__(self, janela, campo):
        self.__janela = janela
        self.__clock = pygame.time.Clock()
        self.__botaoVoltar = Botao(90, 600, 250, 100, "Voltar")
        self.__placar = Placar(40, 100, 350, 60)
        self.__barraForca = BarraForca(65, 500, 300, 30)
        self.__campo = campo

        self.__palheta = Palheta()

        self.__escolha1 = None
        self.__escolha2 = None


    def desenha_tabuleiro(self):
        self.__janela.fill((200, 200, 200))
        self.__placar.desenha_placar(self.__janela)
        self.__botaoVoltar.desenha_botao(self.__janela)
        self.__campo.desenha_campo(self.__janela)
        self.__campo.time1.desenha_time(self.__janela)
        self.__campo.time2.desenha_time(self.__janela)
        self.__campo.bola.desenha_bola(self.__janela)



    def atrito(self):
        self.__campo.bola.atrito()
        for i in (self.__campo.time1.lista_peao + self.__campo.time2.lista_peao):
            i.atrito()

    def vez_de_quem(self):
        pass

    def loop(self):
        aberto = True
        self.__campo.colisao_campo()
        gol_mov = 0
        while aberto:
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        aberto = False
                    if event.key == pygame.K_s:
                        gol_mov = 3.5
                    if event.key == pygame.K_a:
                        gol_mov = -3.5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s or event.key == pygame.K_a:
                        gol_mov = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__botaoVoltar.mouse_sobre(pos):
                        aberto = False

                self.__palheta.aplica_impulso(event, self.__campo.time1.lista_peao, self.__campo.time2.lista_peao, pos, self.__janela)
                self.__botaoVoltar.botao_hover(event, pos)

            self.desenha_tabuleiro()
            self.__palheta.desenha_palheta(pos, self.__janela)
            self.__campo.time1.goleiro.move(gol_mov)

            self.atrito()
            self.__clock.tick(60)
            self.__campo.space.step(2 / 60)
            pygame.display.update()
