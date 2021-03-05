import pygame
from pygame.locals import *
import pymunk
from pymunk.pygame_util import *
from pymunk.vec2d import Vec2d
import sys
from BotaoMenu import Botao
from Campo import Campo
from Lado_campo import Lado_do_campo, CordenadasCampo
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
        self.__botaoVoltar = Botao(90, 575, 250, 100, "Voltar")
        self.__placar = Placar(50, 50, 350, 60)
        self.__barraForca = BarraForca(65, 500, 300, 30)
        self.__campo = Campo()
        self.__lado_campo = CordenadasCampo()
        self.__time_1 = Time('Figueirence', 'imagens/brasao_figueirence.png', 'imagens/brasao_figueirence_goleiro.png'
                             , self.__lado_campo.esquerdo, self.__space )
        self.__time_2 = Time('Avai', 'imagens/brasao_avai.png', 'imagens/brasao_avai_goleiro.png'
                             , self.__lado_campo.direito, self.__space)
        self.__bola = Bola(860, 330, self.__space)
        self.__palheta = Palheta()


    def desenha_tabuleiro(self):
        self.__janela.fill((200, 200, 200))
        self.__placar.desenha_placar(self.__janela)
        self.__barraForca.desenha_barra(self.__janela)
        self.__botaoVoltar.desenha_botao(self.__janela)
        self.__campo.desenha_campo(self.__janela)
        self.__time_1.desenha_time(self.__janela)
        self.__time_2.desenha_time(self.__janela)
        self.__bola.desenha_bola(self.__janela)

    def colisao_campo(self):
        Lado_do_campo([420, 50], [420, 605], self.__space, 2)
        Lado_do_campo([1290, 50], [1290, 605], self.__space, 2)
        Lado_do_campo([420, 50], [1290, 50], self.__space, 2)
        Lado_do_campo([420, 605], [1290, 605], self.__space, 2)

    def vez_de_quem(self):
        pass

    def loop(self):
        jogo_aberto = True
        self.colisao_campo()
        barra_mov = 0
        gol_mov = 0
        alvo = None
        pulling = None
        while jogo_aberto:
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
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
                            i.body.angle = (pos - i.body.position).angle
                            dist = i.shape.point_query(pos).distance
                            if dist - 20 < 0:
                                alvo = i
                                pulling = True
                if event.type == MOUSEBUTTONUP:
                    if pulling:
                        pulling = False
                        b = alvo.shape.body
                        alvo = None
                        x, y = b.position
                        p1x, p1y = Vec2d(x, y)
                        p2x, p2y = from_pygame(event.pos, self.__janela)
                        impulsex, impulsey = 2 * Vec2d(p1x - p2x, p1y - p2y).rotated(-b.angle)
                        if impulsex > 300:
                            impulsex = 300
                        elif impulsex < -300:
                            impulsex = -300
                        if impulsey > 300:
                            impulsey = 300
                        elif impulsey < -300:
                            impulsey = -300
                        b.apply_impulse_at_local_point((impulsex, impulsey))

                self.__botaoVoltar.botao_hover(event, pos)

            self.desenha_tabuleiro()

            self.__bola.atrito()
            for i in (self.__time_1.lista_peao + self.__time_2.lista_peao):
                i.atrito()

            self.__time_1.goleiro.move(gol_mov)
            self.__barraForca.incrementa(barra_mov)

            if alvo is not None:
                b = alvo.shape.body
                p0 = to_pygame(b.position, self.__janela)
                x, y = p0
                if pulling:
                    pygame.draw.line(self.__janela, (0, 0, 255), (x + 20, y + 20), pos, 3)

            if alvo is not None:
                s = alvo.shape
                r = int(alvo.shape.radius)
                p = to_pygame(s.body.position, self.__janela)
                x, y = p
                pygame.draw.circle(self.__janela, (0, 0, 255), (x + 20, y + 20), r + 5, 3)

            self.__clock.tick(60)
            self.__space.step(2 / 60)
            pygame.display.update()
