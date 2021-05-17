import pygame
from pymunk.pygame_util import *
from pymunk.vec2d import Vec2d


class Palheta:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__comprimento = 100
        self.__alvo = None
        self.__pulling = False

    def desenha_palheta(self, pos, janela):
        if self.__alvo is not None:
            b = self.__alvo.shape.body
            p0 = to_pygame(b.position, janela)
            x, y = p0
            if self.__pulling:
                pygame.draw.line(janela, (0, 0, 255), (x + 20, y + 20), pos, 5)

        if self.__alvo is not None:
            s = self.__alvo.shape
            r = int(self.__alvo.shape.radius)
            p = to_pygame(s.body.position, janela)
            x, y = p
            pygame.draw.circle(janela, (0, 0, 255), (x + 20, y + 20), r + 5, 3)

    def seleciona_com_palheta(self, time, pos):
        for i in time:
            a, b = pos
            i.body.angle = ((a - i.shape.radius, b - i.shape.radius) - i.body.position).angle
            dist = i.shape.point_query(pos).distance
            if dist - i.shape.radius < 0:
                self.__alvo = i
                self.__pulling = True


    def aplica_impulso(self, event, janela):
        if self.__pulling:
            self.__pulling = False
            b = self.__alvo.shape.body
            raio = self.__alvo.shape.radius
            self.__alvo = None
            x, y = b.position
            p1x, p1y = Vec2d(x + raio, y + raio)
            p2x, p2y = from_pygame(event.pos, janela)
            impulsex, impulsey = 2 * Vec2d(p1x - p2x, p1y - p2y).rotated(-b.angle)
            if impulsex > 200:
                impulsex = 200
            elif impulsex < -200:
                impulsex = -200
            if impulsey > 200:
                impulsey = 200
            elif impulsey < -200:
                impulsey = -200
            b.apply_impulse_at_local_point((impulsex, impulsey))
