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
            self.__campo.gols2 += 1
        elif self.__campo.gol.verifica_gol(self.__campo.bola) == 2:
            self.reset()
            self.__telaJogo.placar.incrementa(1)
            self.__campo.gols1 += 1

    def verifica_vencedor(self):
        if self.__campo.turno_atual > self.__campo.turno_max:
            if self.__campo.gols1 > self.__campo.gols2:
                return True, '   ' + self.__campo.time1.nome + ' Venceu'
            elif self.__campo.gols1 < self.__campo.gols2:
                return True, '   ' + self.__campo.time2.nome + ' Venceu'
            else:
                return True, '      Empate'
        else:
            return False, ''

    def passa_vez(self, event):
        if event.UI == 'VEZ':
            if not self.__campo.parado():
                self.__telaJogo.notifica = True
            else:
                self.__campo.vez += 1
                self.__campo.turno_atual += 1
                if self.__campo.vez >= 3:
                    self.__campo.vez = 1
                self.__campo.nao_moveu = True
                self.__telaJogo.notifica = False
                self.__telaJogo.indicadorTurnos.incrementa()


    def handle_palheta(self, event, pos):
        if self.__campo.time1 is not None and self.__campo.time2 is not None:
            if self.__campo.vez == 1 and self.__campo.nao_moveu:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.__palheta.seleciona_com_palheta(self.__campo.time1.lista_peao, pos)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.__palheta.aplica_impulso(event, self.__janela)
                    if not self.__campo.parado():
                        self.__campo.nao_moveu = False
            elif self.__campo.vez == 2 and self.__campo.nao_moveu:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.__palheta.seleciona_com_palheta(self.__campo.time2.lista_peao, pos)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.__palheta.aplica_impulso(event, self.__janela)
                    if not self.__campo.parado():
                        self.__campo.nao_moveu = False

    def handle_move_goleiro(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.__campo.gol_mov = 3.5
            if event.key == pygame.K_a:
                self.__campo.gol_mov = -3.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s or event.key == pygame.K_a:
                self.__campo.gol_mov = 0

    def move_goleiro(self):
        if self.__campo.vez == 1 and self.__campo.time1 is not None and self.__campo.time2 is not None \
                and self.__campo.nao_moveu:
            self.__campo.time1.goleiro.move(self.__campo.gol_mov)
        elif self.__campo.vez == 2 and self.__campo.time1 is not None and self.__campo.time2 is not None \
                and self.__campo.nao_moveu:
            self.__campo.time2.goleiro.move(self.__campo.gol_mov)

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
        elif event.UI == 'CRED':
            self.__view_atual = "CRED"

    def event_handler(self):
        x, y = self.verifica_vencedor()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.view_handler(event)
                if not x:
                    self.passa_vez(event)
            if not x:
                self.handle_move_goleiro(event)
                self.handle_palheta(event, pos)

        self.__palheta.desenha_palheta(pos, self.__janela)
        self.move_goleiro()
        self.verifica_gol()
        if self.__campo.time1 is not None and self.__campo.time2 is not None:
            self.__campo.atrito()
        if x:
            self.__telaJogo.notifica_vencedor(y)



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
        elif self.__view_atual == "CRED":
            self.__telaCreditos.desenha_creditos()
            self.__telaCreditos.check_events()


    def comeca(self):
        while True:
            self.draw_view()
            self.event_handler()
            self.__clock.tick(60)
            self.__campo.space.step(2 / 60)
            pygame.display.update()
