import pygame
from BotaoMenu import Botao
from Campo import Campo, Lado_do_campo
from Placar import Placar
from BarraForca import BarraForca

class Jogo:
    def __init__(self, janela):
        self.__janela = janela
        self.__clock = pygame.time.Clock()
        self.__botaoVoltar = Botao(90, 575, 250, 100, "Voltar")
        self.__placar = Placar(50, 50, 350, 60)
        self.__barraForca = BarraForca(65, 500, 300, 30)
        self.__campo = Campo()

    def loop(self):
        jogo_aberto = True
        pygame.key.set_repeat(5)

        while jogo_aberto:
            self.__janela.fill((255, 255, 255))
            self.__placar.desenha_placar(self.__janela)
            self.__barraForca.desenha_barra(self.__janela)
            self.__botaoVoltar.desenha_botao(self.__janela)
            self.__campo.desenhar(self.__janela)

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        jogo_aberto = False
                    if event.key == pygame.K_w:
                        self.__barraForca.aumenta_forca()
                    if event.key == pygame.K_q:
                        self.__barraForca.diminui_forca()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__botaoVoltar.mouse_sobre(pos):
                        jogo_aberto = False
                self.__botaoVoltar.botao_hover(event, pos)

            self.__clock.tick(60)
            pygame.display.update()