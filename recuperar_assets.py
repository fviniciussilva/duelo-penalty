import pygame
import os
import math

pygame.init()

if not os.path.exists("assets"):
    os.makedirs("assets")

print("Recriando assets básicos...")

# --- CAMPO REALISTA ---
campo = pygame.Surface((800, 600))
y = 250
band = 3.0
toggle = True
while y < 600:
    c = (45, 150, 45) if toggle else (35, 135, 35)
    pygame.draw.rect(campo, c, (0, int(y), 800, int(band) + 1))
    y += band
    band *= 1.15
    toggle = not toggle
pygame.draw.polygon(campo, (220, 220, 220), [(100, 600), (700, 600), (520, 250), (280, 250)], 3)
pygame.draw.ellipse(campo, (255, 255, 255), (385, 460, 30, 10))
pygame.image.save(campo, "assets/campo.png")

# --- BOLA 3D ---
bola = pygame.Surface((80, 80), pygame.SRCALPHA)
pygame.draw.circle(bola, (240, 240, 240), (40, 40), 38)
pygame.draw.circle(bola, (0, 0, 0), (40, 40), 38, 2)
sombra = pygame.Surface((80, 80), pygame.SRCALPHA)
pygame.draw.circle(sombra, (0, 0, 0, 100), (48, 48), 38, 10)
bola.blit(sombra, (0, 0))
pygame.image.save(bola, "assets/bola.png")

# --- GOLEIRO ---
goleiro = pygame.Surface((140, 200), pygame.SRCALPHA)
pygame.draw.circle(goleiro, (255, 220, 130), (70, 30), 18)
pygame.draw.polygon(goleiro, (200, 20, 40), [(50, 60), (90, 60), (92, 130), (48, 130)])
pygame.draw.circle(goleiro, (220, 220, 220), (15, 105), 14)
pygame.draw.circle(goleiro, (220, 220, 220), (125, 105), 14)
pygame.image.save(goleiro, "assets/goleiro.png")

print("✓ Campo, Bola e Goleiro recuperados!")
pygame.quit()