import os
from rembg import remove
from PIL import Image

# Configuração de caminhos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def processar_HD(nome_arquivo, tamanho_HD):
    caminho = os.path.join(ASSETS_DIR, nome_arquivo)
    
    if not os.path.exists(caminho):
        print(f"Atenção: {nome_arquivo} não encontrado em assets.")
        return

    print(f"Limpando e otimizando: {nome_arquivo}...")
    try:
        with open(caminho, 'rb') as i:
            # Remove o fundo branco da IA
            img_clean = remove(i.read())
            with open(caminho, 'wb') as o:
                o.write(img_clean)
        
        # Redimensiona com alta qualidade (LANCZOS)
        img = Image.open(caminho).convert("RGBA")
        img.thumbnail(tamanho_HD, Image.Resampling.LANCZOS)
        img.save(caminho)
        print(f"✓ {nome_arquivo} pronto para o jogo!")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    # Ajustando tamanhos para as novas imagens HD
    processar_HD("jogador.png", (400, 400))
    processar_HD("goleiro.png", (300, 300))
    processar_HD("bola.png", (100, 100))