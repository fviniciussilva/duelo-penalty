from rembg import remove
from PIL import Image
import os

if not os.path.exists("assets"):
    os.makedirs("assets")

# O arquivo original que você tem
entrada = "Gemini_Generated_Image_fuab8ofuab8ofuab.png"
saida = "assets/jogador.png"

print("Processando Ronaldinho...")
try:
    with open(entrada, 'rb') as i:
        input_image = i.read()
        output_image = remove(input_image)
        with open(saida, 'wb') as o:
            o.write(output_image)
    
    # Redimensiona para ele não ficar gigante na tela
    img = Image.open(saida)
    img.thumbnail((180, 240), Image.Resampling.LANCZOS)
    img.save(saida)
    print("✓ Tudo pronto na pasta assets!")
except Exception as e:
    print(f"Erro: Verifique se o arquivo {entrada} está na pasta.")