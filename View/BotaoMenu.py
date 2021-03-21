import pygame

class Botao:
    def __init__(self, x, y, largura, altura, texto=''):
        self.__x, self.__y = x, y
        self.__largura, self.__altura = largura, altura
        self.__texto = texto
        self.__b1 = pygame.transform.scale(pygame.image.load("./imagens/botao01.png").convert(), [self.__largura, self.__altura])
        self.__b2 = pygame.transform.scale(pygame.image.load("./imagens/botao02.png").convert(), [self.__largura, self.__altura])
        self.__imagem = self.__b1

    def desenha_botao(self, janela):
        pygame.draw.rect(janela,  (0, 0, 0), (self.__x - 2, self.__y - 2, self.__largura + 4, self.__altura + 4), 0)
        janela.blit(self.__imagem, (self.__x, self.__y))

        if self.__texto != '':
            fonte = pygame.font.Font('./fonts/8-BIT.TTF', 30)
            texto = fonte.render(self.__texto, 1, (0, 0, 0))
            janela.blit(texto, (self.__x + (self.__largura / 2 - texto.get_width() / 2), (self.__y-5) + (self.__altura / 2 - texto.get_height() / 2)))

    def botao_hover(self, event, pos):
        if self.mouse_sobre(pos):
            self.__imagem = self.__b2
        else:
            self.__imagem = self.__b1

    def mouse_sobre(self, pos):
        if pos[0] > self.__x and pos[0] < self.__x + self.__largura:
            if pos[1] > self.__y and pos[1] < self.__y + self.__altura:
                return True

        return False