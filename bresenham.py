import pygame
import sys

# Inicialização do PyGame
pygame.init()

# Definição das cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Definição das dimensões da janela
LARGURA, ALTURA = 800, 400

# Configuração da janela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Algoritmos de Bresenham em PyGame")

# Função para desenhar um pixel na tela
def desenha_pixel(x, y, cor):
    tela.set_at((x, y), cor)

# Algoritmo de Bresenham para desenhar uma linha
def desenha_reta(x1, y1, x2, y2, cor):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1

    if dx > dy:
        erro = dx / 2.0
        while x != x2:
            desenha_pixel(x, y, cor)
            erro -= dy
            if erro < 0:
                y += sy
                erro += dx
            x += sx
    else:
        erro = dy / 2.0
        while y != y2:
            desenha_pixel(x, y, cor)
            erro -= dx
            if erro < 0:
                x += sx
                erro += dy
            y += sy
    desenha_pixel(x, y, cor)  # Desenha o último pixel

# Algoritmo de Bresenham para desenhar uma circunferência
def desenha_circunferencia(x_centro, y_centro, raio, cor):
    x = 0
    y = raio
    delta = 3 - 2 * raio
    while x <= y:
        desenha_pontos_circunferencia(x_centro, y_centro, x, y, cor)
        if delta < 0:
            delta = delta + 4 * x + 6
        else:
            delta = delta + 4 * (x - y) + 10
            y -= 1
        x += 1

# Função auxiliar para desenhar os pontos da circunferência
def desenha_pontos_circunferencia(x_centro, y_centro, x, y, cor):
    desenha_pixel(x_centro + x, y_centro + y, cor)
    desenha_pixel(x_centro - x, y_centro + y, cor)
    desenha_pixel(x_centro + x, y_centro - y, cor)
    desenha_pixel(x_centro - x, y_centro - y, cor)
    desenha_pixel(x_centro + y, y_centro + x, cor)
    desenha_pixel(x_centro - y, y_centro + x, cor)
    desenha_pixel(x_centro + y, y_centro - x, cor)
    desenha_pixel(x_centro - y, y_centro - x, cor)

# Coordenadas das retas e circunferências
reta1 = (150, 200, 450, 200)
reta2 = (200, 50, 400, 350)
reta3 = (400, 50, 200, 350)
circ1 = (300, 200, 50)
circ2 = (300, 200, 100)
circ3 = (300, 200, 150)

# Loop principal do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill(BRANCO)  # Preenche a tela com a cor branca

    # Desenha as linhas
    desenha_reta(*reta1, PRETO)
    desenha_reta(*reta2, VERDE)
    desenha_reta(*reta3, AZUL)

    # Desenha as circunferências
    desenha_circunferencia(*circ1, PRETO)
    desenha_circunferencia(*circ2, VERMELHO)
    desenha_circunferencia(*circ3, PRETO)

    pygame.display.flip()  # Atualiza a tela

# Finaliza o PyGame
pygame.quit()
sys.exit()