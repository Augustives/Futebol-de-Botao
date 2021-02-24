import pygame

class BarraForca:
    def __init__(self, x, y, largura, altura):
        self.x, self.y = x, y
        self.largura, self.altura = largura, altura
        self.imagem = pygame.transform.scale(pygame.image.load("./imagens/barraF.png").convert(),[self.largura, self.altura])
        self.forca_max = largura-28
        self.forca_atual = 1


    def desenha_barra(self, janela):
        janela.blit(self.imagem, (self.x, self.y))
        pygame.draw.rect(janela, (255,0,0), (self.x+15, self.y+5, self.forca_atual, self.altura-10))

    def aumenta_forca(self):
        if self.forca_atual < self.forca_max:
            self.forca_atual +=1

    def diminui_forca(self):
        if self.forca_atual > 0:
            self.forca_atual -= 1
