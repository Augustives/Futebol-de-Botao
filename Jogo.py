import pygame
import sys
from BotaoMenu import Botao


class Jogo():
    def __init__(self):
        pygame.init()
        self.janela = pygame.display.set_mode((1400, 700))
        self.clock = pygame.time.Clock()

    def jogo_loop(self):
        botao_voltar = Botao((155, 155, 0), 600, 575, 250, 100, "Voltar")
        jogo_aberto = True
        while jogo_aberto:
            self.janela.fill((255, 255, 255))
            botao_voltar.desenha_botao(self.janela, (0,0,0))




            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        jogo_aberto = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_voltar.mouse_sobre(pos):
                        jogo_aberto = False

            pygame.display.update()
            self.clock.tick(60)



    def menuPrincipal_loop(self):
        botao_start = Botao((155, 155, 0), 150, 225, 250, 100, "Start")
        botao_creditos = Botao((155, 155, 0), 150, 500, 250, 100, "Credits")
        while True:
            self.janela.fill((255, 0, 0))
            botao_start.desenha_botao(self.janela,(0,0,0))
            botao_creditos.desenha_botao(self.janela, (0, 0, 0))
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


            pygame.display.update()
            self.clock.tick(60)


    def creditos_loop(self):
        botao_voltar = Botao((155, 155, 0), 600, 575, 250, 100, "Voltar")
        credito_aberto = True
        while credito_aberto:
            self.janela.fill((255, 255, 255))
            botao_voltar.desenha_botao(self.janela, (0, 0, 0))


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

            pygame.display.update()
            self.clock.tick(60)