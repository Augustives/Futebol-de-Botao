import pygame

class Campo():

    def __init__(self):
        pass

    def desenhar(self, janela):

        grupo = pygame.sprite.Group()
        gramado = pygame.sprite.Sprite(grupo)
        gramado.image = pygame.image.load('imagens/grama.png')
        gramado.image = pygame.transform.scale(gramado.image, [900, 600])
        gramado.rect = pygame.Rect(430, 50, 900, 600, )
        grupo.draw(janela)

        transparente = pygame.Color(255, 255, 255, 255)
        pygame.draw.rect(janela, transparente, (450, 75, 850, 545), width=6)
        pygame.draw.rect(janela, transparente, (450, 220, 100, 260), width=6)
        pygame.draw.rect(janela, transparente, (1200, 220, 100, 260), width=6)
        pygame.draw.circle(janela, transparente, (880, 350) , 120, width=6)
        pygame.draw.line(janela, transparente, (880,75), (880,620), width=6)
        pygame.draw.circle(janela, (255,255,255), (880, 350), 10,)




