import pygame
from BotaoMenu import Botao
from Jogo import Jogo
from Campo import Campo, Lado_do_campo


class MenuPrincipal:
    def __init__(self, janela, telaJogo, telaCreditos):
        self.__janela = janela
        self.__telaJogo = telaJogo
        self.__telaCreditos = telaCreditos
        self.__clock = pygame.time.Clock()
        self.__botaoStart = Botao(575, 300, 250, 100, "Start")
        self.__botaoCreditos = Botao(575, 425, 250, 100, "Credits")
        self.__bg = pygame.image.load("./imagens/bg.png")

    def loop(self):
        while True:
            self.__janela.fill((255, 255, 255))
            self.__janela.blit(self.__bg, (0, 0))
            self.__botaoStart.desenha_botao(self.__janela)
            self.__botaoCreditos.desenha_botao(self.__janela)

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
                        self.__telaJogo.loop()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__botaoCreditos.mouse_sobre(pos):
                        self.__telaCreditos.loop()

                self.__botaoStart.botao_hover(event, pos)
                self.__botaoCreditos.botao_hover(event, pos)

            self.__clock.tick(60)
            pygame.display.update()