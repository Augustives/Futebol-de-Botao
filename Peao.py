import pygame
import pymunk

class Peao():
    def __init__(self, x, y, imagem, space):
        self.__body = pymunk.Body()
        self.__body.position = x, y
        self.__body.velocity = 0, 0
        self.__shape = pymunk.Circle(self.__body, 20)
        self.__shape.density = 1
        self.__shape.mass = 1
        self.__atrito = 0.95
        self.__shape.elasticity = 0.75
        self.__shape.collision_type = 1
        space.add(self.__body, self.__shape)
        self.__imagem = pygame.transform.scale(imagem, [40, 40])

    @property
    def body(self):
        return self.__body

    @property
    def shape(self):
        return self.__shape

    def desenha_peao(self, janela):
        janela.blit(self.__imagem, self.__body.position)

    def atrito(self):
        v1, v2 = self.__body.velocity

        if v1 > 0:
            v1 *= self.__atrito
        elif v1 < 0:
            v1 *= self.__atrito
        if v2 > 0:
            v2 *= self.__atrito
        elif v2 < 0:
            v2 *= self.__atrito

        self.__body.velocity = v1, v2

    def mouse_sobre(self, pos):
        x, y = self.__body.position
        if pos[0] > int(x) and pos[0] < int(x) + 40 :
            if pos[1] > int(y) and pos[1] < int(y) + 40:
                return True
        return False