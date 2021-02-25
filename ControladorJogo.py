import pygame
from MenuPrincipal  import MenuPrincipal
from Tabuleiro import Tabuleiro
from Creditos import Creditos

class ControladorJogo():
    def __init__(self):
        pygame.init()
        self.__janela = None
        self.desennha_janela(1400, 700)
        self.__telaJogo = Tabuleiro(self.__janela)
        self.__telaCreditos = Creditos(self.__janela)
        self.__MP = MenuPrincipal(self.__janela, self.__telaJogo, self.__telaCreditos)

    def desennha_janela(self, x, y):
        self.__janela = pygame.display.set_mode((x, y))
        pygame.display.set_caption("Futebol de Botao")
        pygame.display.set_icon(pygame.image.load('./imagens/bola.png'))

    def comeca(self):
        self.__MP.loop()








