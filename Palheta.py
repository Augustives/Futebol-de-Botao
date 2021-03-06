import pygame
from pymunk.pygame_util import *
from pymunk.vec2d import Vec2d
from pygame.locals import *

class Palheta:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__comprimento = 100
        self.__tangente = 0
        self.__alvo = None
        self.__pulling = False

    def desenha_palheta(self, pos, janela):
        if self.__alvo is not None:
            b = self.__alvo.shape.body
            p0 = to_pygame(b.position, janela)
            x, y = p0
            if self.__pulling:
                pygame.draw.line(janela, (0, 0, 255), (x + 20, y + 20), pos, 3)

        if self.__alvo is not None:
            s = self.__alvo.shape
            r = int(self.__alvo.shape.radius)
            p = to_pygame(s.body.position, janela)
            x, y = p
            pygame.draw.circle(janela, (0, 0, 255), (x + 20, y + 20), r + 5, 3)

    def aplica_impulso(self, event, time_1, time_2, pos, janela):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in (time_1 + time_2):
                a, b = pos
                i.body.angle = ((a-20, b-20) - i.body.position).angle
                dist = i.shape.point_query(pos).distance
                if dist - 20 < 0:
                    self.__alvo = i
                    self.__pulling = True

        if event.type == pygame.MOUSEBUTTONUP:
            if self.__pulling:
                self.__pulling = False
                b = self.__alvo.shape.body
                self.__alvo = None
                x, y = b.position
                p1x, p1y = Vec2d(x, y)
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
