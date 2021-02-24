import pygame
import sys
from BotaoMenu import Botao
from Placar import Placar

class Jogo():
    def __init__(self):
        pygame.init()
        self.janela = pygame.display.set_mode((1400, 700))
        self.clock = pygame.time.Clock()

    def jogo_loop(self):
        jogo_aberto = True
        botao_voltar = Botao(575, 575, 250, 100, "Voltar")
        placar = Placar(575, 0, 500, 60)


        while jogo_aberto:
            self.janela.fill((255, 255, 255))

            placar.desenha_placar(self.janela)
            botao_voltar.desenha_botao(self.janela, (0,0,0))

            grupo = pygame.sprite.Group()
            avai1 = pygame.sprite.Sprite(grupo)
            avai1.image = pygame.image.load('./imagens/brasao_avai.png')
            avai1.image = pygame.transform.scale(avai1.image, [80, 80])
            #pygame.sprite.collide_circle()
            avai1.rect = pygame.Rect(50, 50, 80, 80)

            fig1 = pygame.sprite.Sprite(grupo)
            fig1.image = pygame.image.load('./imagens/brasao_figueirence_.png')
            fig1.image = pygame.transform.scale(fig1.image, [80, 80])
            fig1.rect = pygame.Rect(200, 50, 80, 80)

            grupo.draw(self.janela)

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        jogo_aberto = False
                    if event.key == pygame.K_a:
                        placar.incrementa(1)
                    if event.key == pygame.K_d:
                        placar.incrementa(2)
                    if event.key == pygame.K_s:
                        placar.reset()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_voltar.mouse_sobre(pos):
                        jogo_aberto = False
                botao_voltar.botao_hover(event, pos)

            self.clock.tick(60)
            pygame.display.update()




    def menuPrincipal_loop(self):
        botao_start = Botao(575, 300, 250, 100, "Start")
        botao_creditos = Botao(575, 425, 250, 100, "Credits")

        while True:
            self.janela.fill((255, 255, 255))
            botao_start.desenha_botao(self.janela, (0, 0, 0))
            botao_creditos.desenha_botao(self.janela, (0, 0, 0))


            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_start.mouse_sobre(pos):
                        self.jogo_loop()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_creditos.mouse_sobre(pos):
                        self.creditos_loop()
                botao_start.botao_hover(event, pos)
                botao_creditos.botao_hover(event, pos)


            self.clock.tick(60)
            pygame.display.update()


    def creditos_loop(self):
        botao_voltar = Botao(600, 575, 250, 100, "Voltar")
        credito_aberto = True
        while credito_aberto:
            self.janela.fill((255, 255, 255))
            botao_voltar.desenha_botao(self.janela, (0, 0, 0))


            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        credito_aberto = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_voltar.mouse_sobre(pos):
                        credito_aberto = False
                botao_voltar.botao_hover(event, pos)

            self.clock.tick(60)
            pygame.display.update()
