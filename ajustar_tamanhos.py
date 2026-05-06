import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def redimensionar(nome, largura, altura):
    caminho = os.path.join(ASSETS_DIR, nome)
    if os.path.exists(caminho):
        with Image.open(caminho) as img:
            # Força o tamanho exato para não achatar nada
            img_nova = img.resize((largura, altura), Image.Resampling.LANCZOS)
            img_nova.save(caminho)
        print(f"✓ {nome} redimensionado para {largura}x{altura}")

# Ronaldinho maior, Bola quadrada (para ser redonda) e Goleiro imponente
redimensionar("jogador.png", 120, 180) 
redimensionar("bola.png", 60, 60)
redimensionar("goleiro.png", 220, 280)