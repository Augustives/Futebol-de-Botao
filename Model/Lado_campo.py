import pymunk

class Lado_do_campo():
    def __init__(self, p1, p2, space, collision_number=None):

        self.__body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.__shape = pymunk.Segment(self.__body, p1, p2, 10)
        self.__shape.elasticity = 0.9
        space.add(self.__body, self.__shape)
        if collision_number:
            self.__shape.collision_type = collision_number


