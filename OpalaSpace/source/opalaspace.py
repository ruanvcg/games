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
