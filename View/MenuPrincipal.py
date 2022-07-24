import pygame
import sys
from View.BotaoMenu import BotaoMenu
from View.Texto import Texto


class MenuPrincipal:
    def __init__(self, janela):
        self.__janela = janela
        self.__clock = pygame.time.Clock()
        self.__bg = pygame.image.load("./imagens/bg.png")
        
        # Texto aqui
        self.__botaoStart = BotaoMenu(575, 400, 250, 100, "Start", 30)
        self.__botaoIdioma = BotaoMenu(575, 525, 250, 100, "Idioma", 30)
        self.__botaoCreditos = BotaoMenu(575, 650, 250, 100, "Credits", 30)

    def desenha_mp(self):
        self.__janela.fill((255, 255, 255))
        self.__janela.blit(self.__bg, (0, 0))
        
        # Texto aqui
        titulo = Texto('FUTEBOL DE BOTAO', 64, 700, 200, self.__janela)
        titulo.desenha_texto()

        self.__botaoStart.desenha_botao(self.__janela)
        self.__botaoIdioma.desenha_botao(self.__janela)
        self.__botaoCreditos.desenha_botao(self.__janela)

    def check_events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__botaoStart.mouse_sobre(pos):
                    event = pygame.event.Event(pygame.USEREVENT, UI='TIME')
                    pygame.event.post(event)
                elif self.__botaoIdioma.mouse_sobre(pos):
                    event = pygame.event.Event(pygame.USEREVENT, UI='LANG')
                    pygame.event.post(event)
                elif self.__botaoCreditos.mouse_sobre(pos):
                    event = pygame.event.Event(pygame.USEREVENT, UI='CRED')
                    pygame.event.post(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.__botaoStart.botao_hover(pos)
            self.__botaoIdioma.botao_hover(pos)
            self.__botaoCreditos.botao_hover(pos)
