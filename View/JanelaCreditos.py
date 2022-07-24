import pygame
import sys
from View.BotaoMenu import BotaoMenu
from View.Texto import Texto


class JanelaCreditos:
    def __init__(self, janela):
        self.__janela = janela
        self.__bg = pygame.image.load("./imagens/bg.png")
        self.__clock = pygame.time.Clock()

        # Texto aqui
        self.__botaoVoltar = BotaoMenu(600, 575, 250, 100, "Voltar", 30)

    def desenha_creditos(self):
        self.__janela.fill((255, 255, 255))
        self.__janela.blit(self.__bg, (0, 0))
        self.__botaoVoltar.desenha_botao(self.__janela)

        # Texto aqui
        titulo = Texto('FUTEBOL DE BOTAO', 64, 700, 200, self.__janela)
        autor = Texto('AUGUSTO S DE O', 64, 700, 300, self.__janela)
        titulo.desenha_texto()
        autor.desenha_texto()

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