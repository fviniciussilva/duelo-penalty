from PIL import Image

def remover_fundo():
    img = Image.open("assets/logo.png").convert("RGBA")
    dados = img.getdata()
    
    novo_dados = []
    for item in dados:
        # Se o pixel for muito claro (branco), define alpha como 0
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            novo_dados.append((255, 255, 255, 0))
        else:
            novo_dados.append(item)
            
    img.putdata(novo_dados)
    img.save("assets/logo_transparente.png", "PNG")
    print("Fundo removido com sucesso!")

remover_fundo()