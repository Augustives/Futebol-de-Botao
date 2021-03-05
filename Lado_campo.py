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
        self.__esquerdo = [(500, 100), (500, 500), (790, 100), (790, 500), (650, 300), (455, 300)]
        self.__direito = [(1175, 100), (1175, 500), (890, 100), (890, 500), (1010, 300), (1255, 300)]

    @property
    def esquerdo(self):
        return self.__esquerdo

    @property
    def direito(self):
        return self.__direito
