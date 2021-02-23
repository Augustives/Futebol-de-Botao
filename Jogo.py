import pygame

class Jogo():
    def __init__(self):
        pygame.init()
        self.jogando = True
        self.screen = pygame.display.set_mode((800, 600))

    def loop(self):
        while self.jogando:
            self.screen.fill((255, 255, 255))
            pygame.display.update()




            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False

