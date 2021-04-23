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
        self.__atrito = 0.96
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

    def parado(self):
        x, y = self.__body.velocity
        if x == 0 and y == 0:
            return True
        else:
            return False

    def atrito(self):
        v1, v2 = self.__body.velocity

        v1 *= self.__atrito
        v2 *= self.__atrito

        if v1 < 1 and v1 > -1 and v2 < 1 and v2 > -1:
            v1, v2 = 0, 0

        self.__body.velocity = v1, v2

    def mouse_sobre(self, pos):
        x, y = self.__body.position
        if pos[0] > int(x) and pos[0] < int(x) + 40 :
            if pos[1] > int(y) and pos[1] < int(y) + 40:
                return True
        return False