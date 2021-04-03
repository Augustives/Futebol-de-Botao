import pygame
import sys
from View.BotaoMenu import BotaoMenu
from View.Placar import Placar
from View.BarraForca import BarraForca
from View.IndicadorTurnos import IndicadorTurnos


class JanelaJogo:
    def __init__(self, janela):
        self.__janela = janela
        self.__botaoVoltar = BotaoMenu(90, 620, 250, 80, "Voltar", 20)
        self.__botaoVez = BotaoMenu(90, 520, 250, 80, "Passar Turno", 20)
        self.__barraForca = BarraForca(65, 500, 300, 30)
        self.__placar = Placar(40, 100, 350, 60, "", "")
        self.__indicadorTurnos = IndicadorTurnos(115, 40, 200, 50)
        self.__notifica = False

    @property
    def placar(self):
        return self.__placar

    @property
    def indicadorTurnos(self):
        return self.__indicadorTurnos

    @property
    def notifica(self):
        return self.__notifica

    @notifica.setter
    def notifica(self, value):
        self.__notifica = value

    def desenha_jogo(self):
        self.__janela.fill((200, 200, 200))
        self.__placar.desenha_placar(self.__janela)
        self.__indicadorTurnos.desenha_turnos(self.__janela)
        self.__botaoVez.desenha_botao(self.__janela)
        self.__botaoVoltar.desenha_botao(self.__janela)
        if self.__notifica:
            self.notifica_movimento()


    def notifica_movimento(self):
        font = pygame.font.Font('./fonts/8-BIT.TTF', 15)
        notifica1 = font.render('Espere os peoes e bolas', 1, (0, 0, 0))
        notifica2 = font.render('    estarem parados', 1, (0, 0, 0))
        self.__janela.blit(notifica1, (55, 250))
        self.__janela.blit(notifica2, (55, 270))

    def notifica_vencedor(self, string):
        font = pygame.font.Font('./fonts/8-BIT.TTF', 25)
        notifica1 = font.render(string, 1, (0, 0, 0))
        self.__janela.blit(notifica1, (55, 250))

    def check_events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.post(event)
                if self.__botaoVoltar.mouse_sobre(pos):
                    event = pygame.event.Event(pygame.USEREVENT, UI='MP')
                    pygame.event.post(event)
                if self.__botaoVez.mouse_sobre(pos):
                    event = pygame.event.Event(pygame.USEREVENT, UI='VEZ')
                    pygame.event.post(event)
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.event.post(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pygame.event.post(event)
                if event.key == pygame.K_a:
                    pygame.event.post(event)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_a:
                    pygame.event.post(event)
            self.__botaoVez.botao_hover(pos)
            self.__botaoVoltar.botao_hover(pos)




