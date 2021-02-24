import pygame

class Botao:
    def __init__(self, cor, x, y, largura, altura, texto=''):
        self.cor = cor
        self.x, self.y = x, y
        self.largura, self.altura = largura, altura
        self.texto = texto

    def desenha_botao(self, janela, outline=None):
        if outline:

            pygame.draw.rect(janela, outline, (self.x - 2, self.y - 2, self.largura + 4, self.altura + 4), 0)


        pygame.draw.rect(janela, self.cor, (self.x, self.y, self.largura, self.altura), 0)

        if self.texto != '':
            font = pygame.font.SysFont('Charter', 60)
            text = font.render(self.texto, 1, (0, 0, 0))
            janela.blit(text, (
                self.x + (self.largura / 2 - text.get_width() / 2), self.y + (self.altura / 2 - text.get_height() / 2)))

    def mouse_sobre(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.largura:
            if pos[1] > self.y and pos[1] < self.y + self.altura:
                return True

        return False




