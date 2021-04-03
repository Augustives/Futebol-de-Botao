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
        self.__clock = pygame.time.Clock()
        self.__view_atual = "MP"

        self.__campo = Campo()
        self.__campo.colisao_campo()
        self.__palheta = Palheta()
        self.__menuPrincipal = MenuPrincipal(self.__janela)
        self.__telaEscolhe = JanelaEscolhaTime(self.__janela)
        self.__telaTurnos = JanelaEscolhaTurno(self.__janela)
        self.__telaJogo = JanelaJogo(self.__janela)
        self.__telaCreditos = JanelaCreditos(self.__janela)

        self.__vez = 1
        self.__contador_vez = 0
        self.__gol_mov = 0

    def desenha_janela(self, x, y):
        self.__janela = pygame.display.set_mode((x, y))
        pygame.display.set_caption("Futebol de Botao")
        pygame.display.set_icon(pygame.image.load("./imagens/bola.png"))

    def reset_game(self):
        self.__campo = Campo()
        self.__telaEscolhe = JanelaEscolhaTime(self.__janela)
        self.__telaTurnos = JanelaEscolhaTurno(self.__janela)
        self.__telaJogo = JanelaJogo(self.__janela)

    def verifica_gol(self):
        if self.__campo.gol.verifica_gol(self.__campo.bola) == 1:
            self.reset()
            self.__telaJogo.placar.incrementa(2)
        elif self.__campo.gol.verifica_gol(self.__campo.bola) == 2:
            self.reset()
            self.__telaJogo.placar.incrementa(1)

    def passa_vez(self, event):
        if event.UI == 'VEZ':
            self.__vez += 1
            self.__contador_vez += 1
            if self.__contador_vez % 2 == 0:
                self.__telaJogo.indicadorTurnos.incrementa()
            if self.__vez > 4:
                self.__vez = 1

    def handle_palheta(self, event, pos):
        if self.__campo.time1 is not None and self.__campo.time2 is not None:
            if self.__vez == 1:
                self.__palheta.aplica_impulso(event, self.__campo.time1.lista_peao, pos,
                                          self.__janela)
            elif self.__vez == 3:
                self.__palheta.aplica_impulso(event, self.__campo.time2.lista_peao, pos,
                                              self.__janela)

    def handle_move_goleiro(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.__gol_mov = 3.5
            if event.key == pygame.K_a:
                self.__gol_mov = -3.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s or event.key == pygame.K_a:
                self.__gol_mov = 0

    def move_goleiro(self):
        if self.__vez == 2:
            self.__campo.time1.goleiro.move(self.__gol_mov)
        elif self.__vez == 4:
            self.__campo.time2.goleiro.move(self.__gol_mov)

    def set_max_turnos(self):
        self.__campo.turno_max = self.__telaTurnos.escolha_turnos

    def set_times(self):
        self.__campo.cria_time(self.__telaEscolhe.escolha1, self.__telaEscolhe.escolha2)
        self.__telaJogo.placar.set_times(self.__telaEscolhe.escolha1, self.__telaEscolhe.escolha2)

    def reset(self):
        self.__campo.bola.reset()
        self.__campo.time1.reset()
        self.__campo.time2.reset()

    def view_handler(self, event):
        if event.UI == 'MP':
            self.__view_atual = "MP"
            self.reset_game()
        elif event.UI == 'TIME':
            self.__view_atual = "TIME"
        elif event.UI == 'TURNO':
            self.__view_atual = "TURNO"
        elif event.UI == 'JOGO':
            self.set_times()
            self.set_max_turnos()
            self.__view_atual = "JOGO"

    def event_handler(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.view_handler(event)
                self.passa_vez(event)
            self.handle_move_goleiro(event)
            self.handle_palheta(event, pos)

        self.__palheta.desenha_palheta(pos, self.__janela)
        self.move_goleiro()
        self.verifica_gol()
        if self.__campo.time1 is not None and self.__campo.time2 is not None:
            self.__campo.atrito()

    def draw_view(self):
        if self.__view_atual == "MP":
            self.__menuPrincipal.desenha_mp()
            self.__menuPrincipal.check_events()
        elif self.__view_atual == "TIME":
            self.__telaEscolhe.desenha_escolha()
            self.__telaEscolhe.check_events()
        elif self.__view_atual == "TURNO":
            self.__telaTurnos.desenha_escolha()
            self.__telaTurnos.check_events()
        elif self.__view_atual == "JOGO":
            self.__telaJogo.desenha_jogo()
            self.__campo.desenha_campo(self.__janela)
            self.__telaJogo.check_events()

    def comeca(self):
        while True:
            self.draw_view()
            self.event_handler()
            self.__clock.tick(60)
            self.__campo.space.step(2 / 60)
            pygame.display.update()
