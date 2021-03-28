import pygame
from View.MenuPrincipal import MenuPrincipal
from View.JanelaJogo import JanelaJogo
from View.JanelaCreditos import JanelaCreditos
from Model.Campo import Campo
from Model.Palheta import Palheta
from View.JanelaEscolhaTime import JanelaEscolhaTime
from View.JanelaEscolhaTurno import JanelaEscolhaTurno

class ControladorJogo():
    def __init__(self):
        pygame.init()
        self.__janela = None
        self.desenha_janela(1400, 800)
        self.__campo = None
        self.__palheta = Palheta()
        self.__telaEscolhe = None
        self.__telaTurnos = None
        self.__telaJogo = None
        self.__telaCreditos = JanelaCreditos(self.__janela)
        self.__menuPrincipal = MenuPrincipal(self.__janela)



    def desenha_janela(self, x, y):
        self.__janela = pygame.display.set_mode((x, y))
        pygame.display.set_caption("Futebol de Botao")
        pygame.display.set_icon(pygame.image.load("./imagens/bola.png"))

    def set_max_turnos(self):
        self.__campo.turno_max = self.__telaTurnos.escolha_turnos

    def set_times(self):
        self.__campo.cria_time(self.__telaEscolhe.escolha1, self.__telaEscolhe.escolha2)

    def comeca(self):
        while True:
            self.__campo = Campo()
            if self.__menuPrincipal.loop() == "times":
                self.__telaEscolhe = JanelaEscolhaTime(self.__janela)
                if self.__telaEscolhe.loop() == "turnos":
                    self.__telaTurnos = JanelaEscolhaTurno(self.__janela)
                    if self.__telaTurnos.loop() == "jogo":
                        self.set_times()
                        self.set_max_turnos()
                        self.__telaJogo = JanelaJogo(self.__janela, self.__campo, self.__palheta)
                        self.__telaJogo.loop()
            else:
                self.__telaCreditos.loop()

