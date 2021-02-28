import math
from math import *
import time

class Fisica:

    #Dois objetos redondos.
    def colisao(self, obj1, obj2):
        dx = obj1.x - obj2.x
        dy = obj1.y - obj2.y

        distancia = math.hypot(dx, dy)
        if distancia < 40:
            return True
        else:
            return False

    def colisao_peoes(self, peao1, peao2):
        dx = peao1.x - peao2.x
        dy = peao1.y - peao2.y
        if self.colisao(peao1, peao2):
            tangente = math.atan2(dy, dx)
            angulo = 0.5 * math.pi + tangente

            peao1.angulo = (2*tangente) - (peao1.angulo-1.5708)
            peao2.angulo = (2*tangente) - (peao2.angulo-1.5708)

            (peao1.velocidade, peao2.velocidade) = (peao2.velocidade, peao1.velocidade)

            peao1.velocidade *= 0.8
            peao2.velocidade *= 0.8

            peao1.x += 1.3*(peao1.velocidade * math.sin(angulo))
            peao1.y -= 1.3*(peao1.velocidade * math.cos(angulo))
            peao2.x -= 1.3*(peao2.velocidade * math.sin(angulo))
            peao2.y += 1.3*(peao2.velocidade * math.cos(angulo))


    def colisao_campo(self, obj):
        if not (obj.x < 1275 - obj.raio):
            obj.x = 1275 - obj.raio
            obj.angulo = -obj.angulo
        elif not (430 + obj.raio < obj.x):
            obj.x = 430 + obj.raio
            obj.angulo = -obj.angulo
        if not (obj.y < 600 - obj.raio):
            obj.y = 600 - obj.raio
            obj.angulo = math.pi - obj.angulo
        elif not (55 + obj.raio < obj.y):
            obj.y = 55 + obj.raio
            obj.angulo = math.pi - obj.angulo



    def colisao_bola(self, peao, bola):
        dx = peao.x - bola.x
        dy = peao.y - bola.y
        if self.colisao(peao, bola):
            tangente = math.atan2(dy, dx)
            angulo = 0.5 * math.pi + tangente

            peao.angulo = (2*tangente) - (peao.angulo)
            bola.angulo = (2*tangente) - (bola.angulo-1.5708)

            if peao.velocidade != 0:
                bola.velocidade = peao.velocidade * 1.25
            else:
                bola.velocidade *= 0.9

            peao.x += (peao.velocidade * math.sin(angulo))
            peao.y -= (peao.velocidade * math.cos(angulo))
            bola.y += (bola.velocidade * math.sin(angulo))
            bola.x -= (bola.velocidade * math.cos(angulo))