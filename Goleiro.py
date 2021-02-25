import pygame

class Goleiro():
    def __init__(self, x, y, imagem):
        self.__x = x
        self.__y = y
        self.__imagem = imagem
        self.__sprit = pygame.sprite.Sprite()
        self.__sprit.image = self.__imagem
        self.__sprit.image = pygame.transform.scale(self.__sprit.image, [30, 90])
        self.__sprit.rect = pygame.Rect(self.__x, self.__y, 30, 90)

    @property
    def get_sprit(self):
        return self.__sprit