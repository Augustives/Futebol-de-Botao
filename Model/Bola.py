import pygame
import pymunk

class Bola():
    def __init__(self, x, y, space):
        self.__body = pymunk.Body()
        self.__body.position = x, y
        self.__pos_central = [x, y]
        self.__body.velocity = 0, 0
        self.__shape = pymunk.Circle(self.__body, 10)
        self.__shape.density = 1
        self.__shape.mass = 0.1
        self.__atrito = 0.98
        self.__shape.elasticity = 0.95
        self.__shape.collision_type = 1
        self.__imagem = pygame.transform.scale(pygame.image.load('./imagens/bola.png'), [20, 20])
        space.add(self.__body, self.__shape)

    @property
    def shape(self):
        return self.__shape

    @property
    def body(self):
        return self.__body

    def desenha_bola(self, janela):
        x, y = self.__body.position
        janela.blit(self.__imagem, (x+10, y+10))

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

    def reset(self):
        self.__body.position = self.__pos_central[0], self.__pos_central[1]
        self.__body.velocity = 0, 0
