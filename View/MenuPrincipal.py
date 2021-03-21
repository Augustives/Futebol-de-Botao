import pygame
import sys
from View.BotaoMenu import BotaoMenu


class MenuPrincipal:
    def __init__(self, janela):
        self.__janela = janela
        self.__clock = pygame.time.Clock()
        self.__bg = pygame.image.load("./imagens/bg.png")
        self.__botaoStart = BotaoMenu(575, 400, 250, 100, "Start")
        self.__botaoCreditos = BotaoMenu(575, 525, 250, 100, "Credits")

    def desenha_mp(self):
        self.__janela.fill((255, 255, 255))
        self.__janela.blit(self.__bg, (0, 0))
        self.__janela.blit((pygame.transform.scale(pygame.image.load("./imagens/titulo.png").convert(), [600, 200])), (400, 100))
        self.__botaoStart.desenha_botao(self.__janela)
        self.__botaoCreditos.desenha_botao(self.__janela)

    def loop(self):
        aberto = True
        while aberto:
            self.desenha_mp()

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
                    if self.__botaoStart.mouse_sobre(pos):
                        return "jogo"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__botaoCreditos.mouse_sobre(pos):
                        return "creditos"

                self.__botaoStart.botao_hover(event, pos)
                self.__botaoCreditos.botao_hover(event, pos)

            self.__clock.tick(60)
            pygame.display.update()
