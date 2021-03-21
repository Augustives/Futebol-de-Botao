import pygame
import pymunk

class Goleiro():
    def __init__(self, x, y, imagem, space):
        self.__body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.__body.position = x, y
        self.__pos_central = [x, y]
        self.__shape = pymunk.Segment(self.__body, (0, 30), (0, -30), 15)
        self.__shape.elasticity = 1
        self.__limites = [y + 60, y - 100]
        self.__imagem = pygame.transform.scale(imagem, [30, 90])
        space.add(self.__body, self.__shape)

    def desenha_goleiro(self, janela):
        x, y = self.__body.position
        janela.blit(self.__imagem, (x+5, y-25))

    def move(self, valor):
        x, y = self.__body.position

        if valor > 0 and (y + valor) < (self.__limites[0]):
            y += valor
        elif valor < 0 and (y + valor) > (self.__limites[1]):
            y += valor

        self.__body.position = x, y

    def reset(self):
        self.__body.position = self.__pos_central[0], self.__pos_central[1]
