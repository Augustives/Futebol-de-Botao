import pygame

class Placar:
    def __init__(self, x, y, largura, altura):
        self.x, self.y = x, y
        self.largura, self.altura = largura, altura
        self.p1 = 0
        self.p2 = 0
        self.imagem = pygame.transform.scale(pygame.image.load("./imagens/placar.png").convert(), [self.largura, self.altura])

    def desenha_placar(self, janela):
        janela.blit(self.imagem, (self.x, self.y))
        pontos = f"{self.p1}*{self.p2}"

        font1 = pygame.font.Font('8-BIT.TTF', 25)
        font2 = pygame.font.Font('8-BIT.TTF', 18)
        time1 = font1.render("FIG", 1, (0, 0, 0))
        time2 = font1.render("AVA", 1, (0, 0, 0))
        score = font2.render(pontos, 1, (0, 0, 0))

        janela.blit(time1, ((self.x - 110) + (self.largura / 2 - time1.get_width() / 2), (self.y) + (self.altura / 2 - time1.get_height() / 2)))
        janela.blit(time2, ((self.x + 110) + (self.largura / 2 - time2.get_width() / 2), (self.y) + (self.altura / 2 - time2.get_height() / 2)))
        janela.blit(score, ((self.x) + (self.largura / 2 - score.get_width() / 2), (self.y) + (self.altura / 2 - score.get_height() / 2)))

    def incrementa(self, jogador):
        if int(jogador) == 1:
            self.p1 += 1
        else:
            self.p2 += 1

    def reset(self):
        self.p1, self.p2 = 0, 0
