import pygame


pygame.init()
tela = pygame.display.set_mode([500, 400])
pygame.display.set_caption('Redenção')
relogio = pygame.time.Clock()


cor_branca = (255,255,255)
cor_azul = (108, 194, 236)

sair = False

while sair != True:
    while True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        relogio.tick(27)
        tela.fill(cor_azul)
        pygame.display.update()



pygame.quit()