import pygame
import sys
from View.BotaoMenu import BotaoMenu
from View.LanguageConfig import LANGUAGE_TEXTS
from View.Texto import Texto


class JanelaEscolhaTurno:
    def __init__(self, janela, controlador):
        self.__janela = janela
        self.__controlador = controlador
        self.__bg = pygame.image.load("./imagens/bg.png")
        self.__botaoTurnos10 = BotaoMenu(600, 450, 250, 100, "10", 30, controlador)
        self.__botaoTurnos20 = BotaoMenu(600, 575, 250, 100, "20", 30, controlador)
        self.__escolha_turnos = None

    @property
    def escolha_turnos(self):
        return self.__escolha_turnos

    def desenha_escolha(self):
        self.__janela.fill((255, 255, 255))
        self.__janela.blit(self.__bg, (0, 0))
        self.__botaoTurnos10.desenha_botao(self.__janela)
        self.__botaoTurnos20.desenha_botao(self.__janela)

        # Texto aqui
        titulo = Texto(LANGUAGE_TEXTS[self.__controlador.language]["select_num_turns_header"], 64, 700, 200, self.__janela, self.__controlador)
        titulo.desenha_texto()

    def check_events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__botaoTurnos10.mouse_sobre(pos):
                    self.__escolha_turnos = 10
                if self.__botaoTurnos20.mouse_sobre(pos):
                    self.__escolha_turnos = 20

            self.__botaoTurnos10.botao_hover(pos)
            self.__botaoTurnos20.botao_hover(pos)

        if self.__escolha_turnos is not None:
            event = pygame.event.Event(pygame.USEREVENT, UI='JOGO')
            pygame.event.post(event)
