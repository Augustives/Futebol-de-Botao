import pygame

class Botao:
    def __init__(self, x, y, largura, altura, texto=''):
        self.x, self.y = x, y
        self.largura, self.altura = largura, altura
        self.texto = texto
        self.b1 = pygame.transform.scale(pygame.image.load("./imagens/botao01.png").convert(), [self.largura, self.altura])
        self.b2 = pygame.transform.scale(pygame.image.load("./imagens/botao02.png").convert(), [self.largura, self.altura])
        self.imagem = self.b1

    def desenha_botao(self, janela):
        pygame.draw.rect(janela,  (0, 0, 0), (self.x - 2, self.y - 2, self.largura + 4, self.altura + 4), 0)
        janela.blit(self.imagem, (self.x, self.y))

        if self.texto != '':
            font = pygame.font.Font('8-BIT.TTF', 30)
            text = font.render(self.texto, 1, (0, 0, 0))
            janela.blit(text, (self.x + (self.largura / 2 - text.get_width() / 2), (self.y-5) + (self.altura / 2 - text.get_height() / 2)))

    def botao_hover(self, event, pos):
        if self.mouse_sobre(pos):
            self.imagem = self.b2
        else:
            self.imagem = self.b1

    def mouse_sobre(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.largura:
            if pos[1] > self.y and pos[1] < self.y + self.altura:
                return True

        return False