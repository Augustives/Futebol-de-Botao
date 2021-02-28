import pygame
import sys
from BotaoMenu import Botao
from Campo import Campo
from Lado_campo import Lado_do_campo
from Placar import Placar
from BarraForca import BarraForca
from Time import Time
from Bola import Bola
from Palheta import Palheta
from Fisica import Fisica

class Tabuleiro:
    def __init__(self, janela):
        self.__janela = janela
        self.__clock = pygame.time.Clock()
        self.__botaoVoltar = Botao(90, 575, 250, 100, "Voltar")
        self.__placar = Placar(50, 50, 350, 60)
        self.__barraForca = BarraForca(65, 500, 300, 30)
        self.__campo = Campo()
        self.__time_1 = Time('Figueirence', 'imagens/brasao_figueirence.png', 'imagens/brasao_figueirence_goleiro.png', Lado_do_campo().esquerdo)
        self.__time_2 = Time('Avai', 'imagens/brasao_avai.png', 'imagens/brasao_avai_goleiro.png', Lado_do_campo().direito)
        self.__bola = Bola(870, 340)
        self.__palheta = Palheta()
        self.__fisica = Fisica()

    def desenha_tabuleiro(self):
        self.__janela.fill((200, 200, 200))
        self.__placar.desenha_placar(self.__janela)
        self.__barraForca.desenha_barra(self.__janela)
        self.__botaoVoltar.desenha_botao(self.__janela)
        self.__campo.desenha_campo(self.__janela)
        self.__time_1.desenha_time(self.__janela)
        self.__time_2.desenha_time(self.__janela)
        self.__bola.desenha_bola(self.__janela)

    def vez_de_quem(self):
        pass

    def loop(self):
        jogo_aberto = True
        barra_mov = 0
        gol_mov = 0
        alvo = self.__time_1.lista_peao[0]
        while jogo_aberto:
            self.desenha_tabuleiro()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        jogo_aberto = False
                    if event.key == pygame.K_w:
                        barra_mov = 3.5
                    if event.key == pygame.K_q:
                        barra_mov = -3.5
                    if event.key == pygame.K_s:
                        gol_mov = 3.5
                    if event.key == pygame.K_a:
                        gol_mov = -3.5
                    if event.key == pygame.K_SPACE and alvo is not None:
                        self.__palheta.aplica_forca(alvo, 5)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_q:
                        barra_mov = 0
                    if event.key == pygame.K_s or event.key == pygame.K_a:
                        gol_mov = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__botaoVoltar.mouse_sobre(pos):
                        jogo_aberto = False
                    for i in (self.__time_1.lista_peao+self.__time_2.lista_peao):
                        if i.mouse_sobre(pos):
                            alvo = i
                self.__botaoVoltar.botao_hover(event, pos)

            self.__palheta.desenha_palheta(alvo, self.__janela)

            self.__time_1.goleiro.move(gol_mov)
            self.__barraForca.incrementa(barra_mov)

            self.__bola.move()
            self.__fisica.colisao_campo(self.__bola)

            for i, peao1 in enumerate(self.__time_1.lista_peao+self.__time_2.lista_peao):
                peao1.move()
                self.__fisica.colisao_bola(peao1, self.__bola)
                self.__fisica.colisao_campo(peao1)
                for peao2 in  (self.__time_1.lista_peao+self.__time_2.lista_peao)[i + 1:]:
                    self.__fisica.colisao_peoes(peao1, peao2)


            self.__clock.tick(60)
            pygame.display.update()