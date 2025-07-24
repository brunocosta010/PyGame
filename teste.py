import pygame
import time

pygame.init()
pygame.mixer.init()

try:
    pygame.mixer.music.load('./asset/Menu.wav')
    print("✅ Som carregado com sucesso.")
except pygame.error as e:
    print(f"❌ Erro ao carregar o som: {e}")
    exit()

pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

# Espera o som tocar por 5 segundos
print("▶️ Tocando som por 5 segundos...")
time.sleep(5)

pygame.quit()
