import pygame
import sys
from BotaoMenu import Botao

class Creditos:
    def __init__(self, janela):
        self.__janela = janela
        self.__clock = pygame.time.Clock()
        self.__botaoVoltar = Botao(600, 575, 250, 100, "Voltar")

    def desenha_creditos(self):
        self.__janela.fill((255, 255, 255))
        self.__botaoVoltar.desenha_botao(self.__janela)

    def loop(self):
        credito_aberto = True
        while credito_aberto:
            self.desenha_creditos()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        credito_aberto = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__botaoVoltar.mouse_sobre(pos):
                        credito_aberto = False
                self.__botaoVoltar.botao_hover(event, pos)

            self.__clock.tick(60)
            pygame.display.update()
