import pygame

class Campo():

    def __init__(self):
        self.__gol = None
        self.__laterais = pygame.sprite.Group()
        self.__esquerdo = [(500, 200), (500, 575), (790, 200), (790, 575), (650, 375), (455, 400)]
        self.__direito = [(1175, 200), (1175, 575), (890, 200), (890, 575), (1010, 375), (1255, 400)]

    @property
    def esquerdo(self):
        return self.__esquerdo

    @property
    def direito(self):
        return self.__direito

    def desenha_campo(self, janela):
        grupo = pygame.sprite.Group()
        gramado = pygame.sprite.Sprite(grupo)
        gramado.image = pygame.image.load('imagens/grama.png')
        gramado.image = pygame.transform.scale(gramado.image, [900, 600])
        gramado.rect = pygame.Rect(430, 100, 900, 600, )
        grupo.draw(janela)

        self.__laterais.add()

        transparente = pygame.Color(255, 255, 255, 255)
        pygame.draw.rect(janela, transparente, (450, 125, 850, 545), width=6)
        pygame.draw.rect(janela, transparente, (450, 270, 100, 260), width=6)
        pygame.draw.rect(janela, transparente, (1200, 270, 100, 260), width=6)
        pygame.draw.circle(janela, transparente, (880, 400), 120, width=6)
        pygame.draw.line(janela, transparente, (880, 125), (880, 670), width=6)
        pygame.draw.circle(janela, (255, 255, 255), (880, 400), 10, )
