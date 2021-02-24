import pygame
import sys
from BotaoMenu import Botao
from Placar import Placar
from BarraForca import BarraForca
from Campo import Campo, Lado_do_campo
from MenuPrincipal  import MenuPrincipal
from Jogo import Jogo
from Creditos import Creditos

class ControladorJogo():
    def __init__(self):
        pygame.init()
        self.janela = pygame.display.set_mode((1400, 700))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Futebol de Botao")
        pygame.display.set_icon(pygame.image.load('./imagens/bola.png'))
        self.__telaJogo = Jogo(self.janela)
        self.__telaCreditos = Creditos(self.janela)
        self.__MP = MenuPrincipal(self.janela, self.__telaJogo, self.__telaCreditos)


    def comeca(self):
        self.__MP.loop()








