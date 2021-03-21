import pygame

class Placar:
    def __init__(self, x, y, largura, altura, nome1, nome2):
        self.__x, self.__y = x, y
        self.__largura, self.__altura = largura, altura
        self.__nome1 = nome1
        self.__nome2 = nome2
        self.__p1 = 0
        self.__p2 = 0
        self.__imagem = pygame.transform.scale(pygame.image.load("./imagens/placar.png").convert(), [self.__largura, self.__altura])

    def desenha_placar(self, janela):
        janela.blit(self.__imagem, (self.__x, self.__y))
        pontos = f"{self.__p1}*{self.__p2}"

        font1 = pygame.font.Font('./fonts/8-BIT.TTF', 25)
        font2 = pygame.font.Font('./fonts/8-BIT.TTF', 18)
        time1 = font1.render(self.__nome1[0]+self.__nome1[1]+self.__nome1[2], 1, (0, 0, 0))
        time2 = font1.render(self.__nome2[0]+self.__nome2[1]+self.__nome2[2], 1, (0, 0, 0))
        score = font2.render(pontos, 1, (0, 0, 0))

        janela.blit(time1, ((self.__x - 110) + (self.__largura / 2 - time1.get_width() / 2), (self.__y) + (self.__altura / 2 - time1.get_height() / 2)))
        janela.blit(time2, ((self.__x + 110) + (self.__largura / 2 - time2.get_width() / 2), (self.__y) + (self.__altura / 2 - time2.get_height() / 2)))
        janela.blit(score, ((self.__x) + (self.__largura / 2 - score.get_width() / 2), (self.__y) + (self.__altura / 2 - score.get_height() / 2)))

    def incrementa(self, jogador):
        if int(jogador) == 1:
            self.__p1 += 1
        else:
            self.__p2 += 1

    def reset(self):
        self.__p1, self.__p2 = 0, 0
