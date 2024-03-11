import pygame

# Inicializa o pygame
pygame.init()

# Carrega o arquivo de áudio
pygame.mixer.music.load('teste10.mp3.mp3')

# Inicia a reprodução do áudio
pygame.mixer.music.play()

# Aguarda até que a música termine de tocar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)