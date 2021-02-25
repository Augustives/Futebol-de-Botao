import pygame
from BotaoMenu import Botao
from Campo import Campo
from Lado_campo import Lado_do_campo
from Placar import Placar
from BarraForca import BarraForca
from Time import Time
from Bola import Bola

class Tabuleiro:
    def __init__(self, janela):
        self.__janela = janela
        self.__clock = pygame.time.Clock()
        self.__botaoVoltar = Botao(90, 575, 250, 100, "Voltar")
        self.__placar = Placar(50, 50, 350, 60)
        self.__barraForca = BarraForca(65, 500, 300, 30)
        self.__campo = Campo()
        self.__time_1 = Time('Figueirence', 'imagens/brasao_figueirence.png', 'imagens/brasao_figueirence_goleiro.png', Lado_do_campo().esquerdo)
        self.__time_2 = Time('Avai', 'imagens/brasao_avai.png', 'imagens/brasao_avai_goleiro.png', Lado_do_campo().direito)
        self.__bola = Bola()

    def loop(self):
        jogo_aberto = True
        barra_mov = 0

        while jogo_aberto:
            self.__janela.fill((200, 200, 200))
            self.__placar.desenha_placar(self.__janela)
            self.__barraForca.desenha_barra(self.__janela)
            self.__botaoVoltar.desenha_botao(self.__janela)
            self.__campo.desenhar(self.__janela)
            self.__time_1.desenhar(self.__janela)
            self.__time_2.desenhar(self.__janela)
            self.__bola.desenhar(self.__janela)

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        jogo_aberto = False
                    if event.key == pygame.K_w:
                        barra_mov = 5
                    if event.key == pygame.K_q:
                        barra_mov = -5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_q:
                        barra_mov = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__botaoVoltar.mouse_sobre(pos):
                        jogo_aberto = False
                self.__botaoVoltar.botao_hover(event, pos)

            self.__barraForca.incrementa(barra_mov)


            self.__clock.tick(60)
            pygame.display.update()