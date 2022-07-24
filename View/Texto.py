import pygame

class Texto:
    def __init__(self, texto, tamanho, x, y, janela):
        self.__janela = janela
        self.__font = pygame.font.Font('./fonts/8-BIT.ttf', tamanho)
        self.__text = self.__font.render(texto, True, (0,0,0), (0, 255, 0))
        self.__textRect = self.__text.get_rect()
        self.__textRect.center = (x, y)
    
    def desenha_texto(self):
        self.__janela.blit(self.__text, self.__textRect)