import math
from math import *

class Fisica:

    #Dois objetos redondos.
    def colisao(self, obj1, obj2):
        dx = obj1.x -obj2.x
        dy = obj1.y - obj2.y

        distancia = math.hypot(dx, dy)
        if distancia < 60:
            return True
        else:
            return False

    def colisao_peoes(self, peao1, peao2):
        dx = peao1.x - peao2.x
        dy = peao1.y - peao2.y
        if self.colisao(peao1, peao2):
            tangente = math.atan2(dy, dx)
            angulo = tangente+90

            peao1.angulo = 2 * math.degrees(tangente) - radians(peao1.angulo)
            peao2.angulo = 2 * math.degrees(tangente) - radians(peao2.angulo)

            (peao1.velocidade, peao2.velocidade) = (peao2.velocidade, peao1.velocidade)

            peao1.velocidade *= 0.8
            peao2.velocidade *= 0.8

            peao1.x += math.sin(angulo)
            peao1.y -= math.cos(angulo)
            peao2.x -= math.sin(angulo)
            peao2.y += math.cos(angulo)


    def colisao_campo(self, peao):
        if not (peao.x < 1245):
            peao.x = 1245
            peao.angulo = 180 - peao.angulo
        if not (450 < peao.x):
            peao.x = 450
            peao.angulo = 180 - peao.angulo
        if not (peao.y < 555):
            peao.y = 555
            peao.angulo = 360 - peao.angulo
        if not (80 < peao.y):
            peao.y = 80
            peao.angulo = 360 - peao.angulo