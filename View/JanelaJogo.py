import pygame
import sys
from View.BotaoMenu import BotaoMenu
from View.Placar import Placar
from View.BarraForca import BarraForca
from Model.Palheta import Palheta


class JanelaJogo:
    def __init__(self, janela, campo):
        self.__janela = janela
        self.__clock = pygame.time.Clock()
        self.__botaoVoltar = BotaoMenu(90, 600, 250, 100, "Voltar")
        self.__barraForca = BarraForca(65, 500, 300, 30)
        self.__campo = campo
        self.__placar = Placar(40, 100, 350, 60, self.__campo.time1.nome, self.__campo.time2.nome)
        self.__palheta = Palheta()

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

    def reset(self):
        self.__campo.bola.reset()
        self.__campo.time1.reset()
        self.__campo.time2.reset()

    def vez_de_quem(self):
        pass

    def loop(self):
        aberto = True
        self.__campo.colisao_campo()
        gol_mov = 0
        while aberto:
            if self.__campo.gol.verifica_gol(self.__campo.bola) == 1:
                self.reset()
                self.__placar.incrementa(2)
            elif self.__campo.gol.verifica_gol(self.__campo.bola) == 2:
                self.reset()
                self.__placar.incrementa(1)
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
                self.__botaoVoltar.botao_hover(pos)

            self.desenha_tabuleiro()
            self.__palheta.desenha_palheta(pos, self.__janela)
            self.__campo.time1.goleiro.move(gol_mov)

            self.atrito()
            self.__clock.tick(60)
            self.__campo.space.step(2 / 60)
            pygame.display.update()
