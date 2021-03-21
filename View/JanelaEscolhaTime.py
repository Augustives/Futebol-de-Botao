import pygame
import sys
from View.BotaoMenu import Botao


class JanelaEscolhaTime:
    def __init__(self, janela):
        self.__janela = janela
        self.__bg = pygame.image.load("./imagens/bg.png")
        self.__clock = pygame.time.Clock()
        self.__botaoTime1 = Botao(600, 450, 250, 100, "Fig")
        self.__botaoTime2 = Botao(600, 575, 250, 100, "Ava")
        self.__num_escolhas = 0
        self.__escolha1 = None
        self.__escolha2 = None

    @property
    def escolha1(self):
        return self.__escolha1

    @property
    def escolha2(self):
        return self.__escolha2

    def desenha_escolha(self):
        self.__janela.fill((255, 255, 255))
        self.__janela.blit(self.__bg, (0, 0))
        self.__botaoTime1.desenha_botao(self.__janela)
        self.__botaoTime2.desenha_botao(self.__janela)

    def loop(self):
        aberto = True
        while aberto:
            self.desenha_escolha()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        aberto = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__botaoTime1.mouse_sobre(pos):
                        if self.__num_escolhas == 0:
                            self.__escolha1 = 'Fig'
                            self.__num_escolhas += 1
                        elif self.__escolha1 != 'Fig':
                            self.__num_escolhas = 0
                            self.__escolha2 = 'Fig'
                    if self.__botaoTime2.mouse_sobre(pos):
                        if self.__num_escolhas == 0:
                            self.__escolha1 = 'Ava'
                            self.__num_escolhas += 1
                        elif self.__escolha1 != 'Ava':
                            self.__num_escolhas = 0
                            self.__escolha2 = 'Ava'

                self.__botaoTime1.botao_hover(event, pos)
                self.__botaoTime2.botao_hover(event, pos)

            if self.__escolha2 is not None:
                return True

            self.__clock.tick(60)
            pygame.display.update()
