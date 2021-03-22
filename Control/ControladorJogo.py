import pygame
from View.MenuPrincipal import MenuPrincipal
from View.JanelaJogo import JanelaJogo
from View.JanelaCreditos import JanelaCreditos
from Model.Campo import Campo
from Model.Palheta import Palheta
from View.JanelaEscolhaTime import JanelaEscolhaTime
from View.JanelaEscolheTurno import JanelaEscolhaTurno

class ControladorJogo():
    def __init__(self):
        pygame.init()
        self.__janela = None
        self.desenha_janela(1400, 800)
        self.__campo = Campo()
        self.__palheta = Palheta()
        self.__telaEscolhe = JanelaEscolhaTime(self.__janela)
        self.__telaTurnos = JanelaEscolhaTurno(self.__janela)
        self.__telaJogo = None
        self.__telaCreditos = JanelaCreditos(self.__janela)
        self.__menuPrincipal = MenuPrincipal(self.__janela)



    def desenha_janela(self, x, y):
        self.__janela = pygame.display.set_mode((x, y))
        pygame.display.set_caption("Futebol de Botao")
        pygame.display.set_icon(pygame.image.load("./imagens/bola.png"))

    def comeca(self):
        while True:
            self.__campo = Campo()
            if self.__menuPrincipal.loop() == "times":
                if self.__telaEscolhe.loop() == "turnos":
                    self.__campo.cria_time(self.__telaEscolhe.escolha1, self.__telaEscolhe.escolha2)
                    if self.__telaTurnos.loop() == "jogo":
                        self.__campo.turnos = self.__telaTurnos.turnos
                        self.__telaJogo = JanelaJogo(self.__janela, self.__campo, self.__palheta)
                        self.__telaJogo.loop()
            else:
                self.__telaCreditos.loop()



