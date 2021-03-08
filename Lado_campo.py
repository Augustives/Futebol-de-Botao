import pymunk

class Lado_do_campo():
    def __init__(self, p1, p2, space, collision_number=None):

        self.__body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.__shape = pymunk.Segment(self.__body, p1, p2, 10)
        self.__shape.elasticity = 0.9
        space.add(self.__body, self.__shape)
        if collision_number:
            self.__shape.collision_type = collision_number


class CordenadasCampo:
    def __init__(self):
        self.__esquerdo = [(500, 200), (500, 575), (790, 200), (790, 575), (650, 375), (455, 400)]
        self.__direito = [(1175, 200), (1175, 575), (890, 200), (890, 575), (1010, 375), (1255, 400)]

    @property
    def esquerdo(self):
        return self.__esquerdo

    @property
    def direito(self):
        return self.__direito
