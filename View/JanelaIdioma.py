import pygame
import sys
from View.BotaoMenu import BotaoMenu
from View.LanguageConfig import LANGUAGE_TEXTS
from View.Texto import Texto


class JanelaIdioma:
    def __init__(self, janela, controlador):
        self.__janela = janela
        self.__controlador = controlador
        self.__bg = pygame.image.load("./imagens/bg.png")
        self.__idioma_escolhido = None
        # Texto aqui
        self.__botaoPor = BotaoMenu(600, 400, 250, 100, "POR", 30, controlador)
        self.__botaoEsp = BotaoMenu(600, 510, 250, 100, "ESP", 30, controlador)
        self.__botaoEng = BotaoMenu(600, 620, 250, 100, "ENG", 30, controlador)

    @property
    def escolha1(self):
        return self.__escolha1

    @property
    def escolha2(self):
        return self.__escolha2

    def desenha_escolha(self):
        self.__janela.fill((255, 255, 255))
        self.__janela.blit(self.__bg, (0, 0))
        self.__botaoPor.desenha_botao(self.__janela)
        self.__botaoEsp.desenha_botao(self.__janela)
        self.__botaoEng.desenha_botao(self.__janela)

        # Texto aqui
        titulo = Texto(LANGUAGE_TEXTS[self.__controlador.language]["language_selection_title"], 64, 700, 200, self.__janela, self.__controlador)
        titulo.desenha_texto()


    def check_events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__botaoPor.mouse_sobre(pos):
                    self.__idioma_escolhido = 'POR'
                if self.__botaoEsp.mouse_sobre(pos):
                    self.__idioma_escolhido = 'ESP'
                if self.__botaoEng.mouse_sobre(pos):
                    self.__idioma_escolhido = 'ENG'

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.__botaoPor.botao_hover(pos)
            self.__botaoEsp.botao_hover(pos)
            self.__botaoEng.botao_hover(pos)

        if self.__idioma_escolhido is not None:
            self.__controlador.language = self.__idioma_escolhido
            self.__idioma_escolhido = None
            event = pygame.event.Event(pygame.USEREVENT, UI='MP')
            pygame.event.post(event)
