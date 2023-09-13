import pygame

pygame.init()

largura = 900
altura = 800

tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('Jogo de Xadrez')

fonte = pygame.font.Font('freesansbold.ttf', 20)

fonte_instrucao = pygame.font.Font('freesansbold.ttf', 40)

cronometro = pygame.time.Clock()
fps = 60
# variaveis do jogo e imagens

rainha_branca=pygame.image.load('assets/imagens/W_Queen.png')
rainha_branca=pygame.image.scale(rainha_branca, (80,80))
torre_branca=pygame.image.scale(pygame.image.load('assets/imagens/W_Rook.png') (80, 80))


pecas_brancas = ['torre', 'cavalo', 'bispo', 'rei', 'rainha', 'bispo', 'cavalo', 'torre',
                 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']

brancas_localizacao = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                       (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

pecas_pretas = ['torre', 'cavalo', 'bispo', 'rei', 'rainha', 'bispo', 'cavalo', 'torre',
                'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']

pretas_localizacao = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                       (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

pecas_brancas_capturadas = []

pecas_pretas_capturadas =[]

turnos_fases=0

peca_selecionada=60

movimentos_validos=[]

# loop principal do jogo
run = True

while run:
    cronometro.tick(fps)
    tela.fill('black')

    # manipulação de eventos aqui em baixo

    # evento do xzinho para fechar o jogo

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
