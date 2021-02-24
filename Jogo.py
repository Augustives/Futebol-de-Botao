import pygame
import sys
from BotaoMenu import Botao
from Placar import Placar
from BarraForca import BarraForca
from Campo import Campo, Lado_do_campo



class Jogo():
    def __init__(self):
        pygame.init()
        self.janela = pygame.display.set_mode((1400, 700))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Futebol de Chernobyl")
        icon = pygame.image.load('./imagens/nuclear.png')
        pygame.display.set_icon(icon)


    def jogo_loop(self):
        jogo_aberto = True
        botao_voltar = Botao(50, 575, 250, 100, "Voltar")
        placar = Placar(50, 10, 300, 60)
        barra_forca = BarraForca(50, 600, 300, 30)
        pygame.key.set_repeat(5)

        while jogo_aberto:
            self.janela.fill((255, 255, 255))

            placar.desenha_placar(self.janela)
            barra_forca.desenha_barra(self.janela)
            botao_voltar.desenha_botao(self.janela)

            Campo().desenhar(self.janela)



            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        jogo_aberto = False
                    if event.key == pygame.K_w:
                        barra_forca.aumenta_forca()
                    if event.key == pygame.K_q:
                        barra_forca.diminui_forca()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_voltar.mouse_sobre(pos):
                        jogo_aberto = False
                botao_voltar.botao_hover(event, pos)

            self.clock.tick(60)
            pygame.display.update()




    def menuPrincipal_loop(self):
        botao_start = Botao(575, 300, 250, 100, "Start")
        botao_creditos = Botao(575, 425, 250, 100, "Credits")
        bg = pygame.image.load("./imagens/bg.png")

        while True:
            self.janela.fill((255, 255, 255))
            self.janela.blit(bg, (0,0))
            botao_start.desenha_botao(self.janela)
            botao_creditos.desenha_botao(self.janela)



            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_start.mouse_sobre(pos):
                        self.jogo_loop()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_creditos.mouse_sobre(pos):
                        self.creditos_loop()

                botao_start.botao_hover(event, pos)
                botao_creditos.botao_hover(event, pos)


            self.clock.tick(60)
            pygame.display.update()


    def creditos_loop(self):
        botao_voltar = Botao(600, 575, 250, 100, "Voltar")
        credito_aberto = True
        while credito_aberto:
            self.janela.fill((255, 255, 255))
            botao_voltar.desenha_botao(self.janela)


            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        credito_aberto = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_voltar.mouse_sobre(pos):
                        credito_aberto = False
                botao_voltar.botao_hover(event, pos)

            self.clock.tick(60)
            pygame.display.update()
