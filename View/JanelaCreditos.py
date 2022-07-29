import pygame
import sys
from View.BotaoMenu import BotaoMenu
from View.LanguageConfig import LANGUAGE_TEXTS
from View.Texto import Texto


class JanelaCreditos:
    def __init__(self, janela, controlador):
        self.__janela = janela
        self.__bg = pygame.image.load("./imagens/bg.png")
        self.__clock = pygame.time.Clock()
        self.__controlador = controlador

        # Texto aqui
        self.__botaoVoltar = BotaoMenu(600, 575, 250, 100, LANGUAGE_TEXTS[self.__controlador.language]["go_back_button"], 30, controlador)

    def desenha_creditos(self):
        self.__janela.fill((255, 255, 255))
        self.__janela.blit(self.__bg, (0, 0))
        self.__botaoVoltar.desenha_botao(self.__janela, LANGUAGE_TEXTS[self.__controlador.language]["go_back_button"])

        # Texto aqui
        titulo = Texto(LANGUAGE_TEXTS[self.__controlador.language]["credits_button"], 64, 700, 200, self.__janela, self.__controlador)
        autor = Texto('AUGUSTO S DE O', 64, 700, 300, self.__janela, self.__controlador)
        autor2 = Texto('GABRIEL M NEVES', 64, 700, 400, self.__janela, self.__controlador)
        titulo.desenha_texto()
        autor.desenha_texto()
        autor2.desenha_texto()

    def check_events(self):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__botaoVoltar.mouse_sobre(pos):
                    event = pygame.event.Event(pygame.USEREVENT, UI='MP')
                    pygame.event.post(event)
            self.__botaoVoltar.botao_hover(pos)