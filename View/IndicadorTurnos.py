import pygame

from View.LanguageConfig import LANGUAGE_TEXTS


class IndicadorTurnos:
    def __init__(self, x, y, largura, altura, controlador):
        self.__x, self.__y = x, y
        self.__largura, self.__altura = largura, altura
        self.__turnos = 1
        self.__controlador = controlador
        self.__imagem = pygame.transform.scale(pygame.image.load("./imagens/turnos.png").convert(), [self.__largura, self.__altura])

    @property
    def turnos(self):
        return self.__turnos

    def desenha_turnos(self, janela):
        janela.blit(self.__imagem, (self.__x, self.__y))

        font1 = pygame.font.Font('./fonts/8-BIT.TTF', 25)
        turnos = font1.render(LANGUAGE_TEXTS[self.__controlador.language]["in_game_turn_header"]+str(self.__turnos), 1, (0, 0, 0))

        janela.blit(turnos, (self.__x + (self.__largura / 2 - turnos.get_width() / 2), (self.__y-5) + (self.__altura / 2 - turnos.get_height() / 2)))

    def incrementa(self):
        self.__turnos += 1
