import pygame
import sys
from View.BotaoMenu import BotaoMenu


class JanelaCreditos:
    def __init__(self, janela):
        self.__janela = janela
        self.__bg = pygame.image.load("./imagens/bg.png")
        self.__clock = pygame.time.Clock()
        self.__botaoVoltar = BotaoMenu(600, 575, 250, 100, "Voltar", 30)

    def desenha_creditos(self):
        self.__janela.fill((255, 255, 255))
        self.__janela.blit(self.__bg, (0, 0))
        self.__botaoVoltar.desenha_botao(self.__janela)

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