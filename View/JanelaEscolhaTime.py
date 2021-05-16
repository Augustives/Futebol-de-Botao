import pygame
import sys
from View.BotaoMenu import BotaoMenu


class JanelaEscolhaTime:
    def __init__(self, janela):
        self.__janela = janela
        self.__bg = pygame.image.load("./imagens/bg.png")
        self.__botaoTime1 = BotaoMenu(600, 450, 250, 100, "Fig", 30)
        self.__botaoTime2 = BotaoMenu(600, 575, 250, 100, "Ava", 30)
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
        self.__janela.blit((pygame.transform.scale(pygame.image.load("./imagens/titulo2.png").convert(), [625, 200])),
                           (400, 100))

    def check_events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            self.__botaoTime1.botao_hover(pos)
            self.__botaoTime2.botao_hover(pos)

        if self.__escolha2 is not None:
            event = pygame.event.Event(pygame.USEREVENT, UI='TURNO')
            pygame.event.post(event)
