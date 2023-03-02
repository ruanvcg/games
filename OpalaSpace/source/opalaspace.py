import pygame, random

try:
    #inicia o pygame
    pygame.init()

except:
    print('Erro em algum módulo do PyGame. Reinicie a aplicação.')
    pygame.quit()

#largura e altura da janela
largura = 1280
altura = 720

#configura a janela e o texto do jogo
screen = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo Opala Space - IFPI campus Pedro II')

img_fundo = pygame.image.load('figs/fundo.jpg').convert_alpha()
img_fundo = pygame.transform.scale(img_fundo, (largura,altura))

img_alien = pygame.image.load('figs/alien.png').convert_alpha()
img_alien = pygame.transform.scale(img_alien, (50,50))

img_aviao = pygame.image.load('figs/aviao.png').convert_alpha()
img_aviao = pygame.transform.scale(img_aviao, (50,50))
img_aviao = pygame.transform.rotate(img_aviao, -90)

img_missil = pygame.image.load('figs/missil.png')
img_missil = pygame.transform.scale(img_missil,(25,25))
img_missil = pygame.transform.rotate(img_missil, -45)

x_alien = 500
y_alien = 360

x_aviao = 200 
y_aviao = 300

velocidade_missil = 1
x_missil = 200
y_missil = 300