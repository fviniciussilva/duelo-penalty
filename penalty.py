import pygame
import random
import sys

# Inicialização
pygame.init()
pygame.joystick.init()

# Setup Controle
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for j in joysticks:
    j.init()

LARGURA, ALTURA = 1000, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Super Penalty 2026 - Fernando vs Kahn")

# Cores e Fontes
BRANCO, AMARELO, PRETO, CINZA, AZUL, VERDE, VERMELHO = (255, 255, 255), (255, 215, 0), (0, 0, 0), (50, 50, 50), (30, 144, 255), (0, 255, 0), (255, 0, 0)
fonte_lista = pygame.font.SysFont("arial", 20, bold=True)
fonte_titulo = pygame.font.SysFont("arial", 50, bold=True)
fonte_vitoria = pygame.font.SysFont("arial", 80, bold=True)
# Nova fonte para o alerta de limite
fonte_alerta = pygame.font.SysFont("arial", 45, bold=True)

try:
    img_menu = pygame.transform.scale(pygame.image.load("assets/tela_inicial.png").convert(), (1000, 600))
    img_campo = pygame.transform.scale(pygame.image.load("assets/campo_2.png").convert(), (800, 600))
    img_bola = pygame.image.load("assets/bola.png").convert_alpha()
    ronaldinho_base = pygame.image.load("assets/jogador.png").convert_alpha()
    ronaldinho_impacto = pygame.image.load("assets/ronaldinho_chute.png").convert_alpha()
    kahn_base = pygame.image.load("assets/goleiro.png").convert_alpha()
    kahn_centro = pygame.image.load("assets/kahn_centro.png").convert_alpha()
    kahn_esq = pygame.image.load("assets/kahn_esquerda.png").convert_alpha()
    kahn_dir = pygame.image.load("assets/kahn_direita.png").convert_alpha()
except:
    print("Erro nos assets!"); pygame.quit(); sys.exit()

# Dados dos Jogadores (Fernando Vinícius da Silva)
lista_jogadores = ["Fernando", "Ana", "Bruno", "Carlos", "Dani", "Eduardo", "Sophia", "Alessandra", "Fabíola", "Victor", "Lucas", "Mariana"]
pontos = {n: 0 for n in lista_jogadores}
chutes_feitos = {n: 0 for n in lista_jogadores}
LIMITE_CHUTES = 5 
idx_aluno = 0

# Estados e Variáveis
estado_global = "MENU"
estado_penalty = 0 
mira_x, mira_y = 400, 280 
bola_x, bola_y, bola_z = 400, 455, 1.0 
goleiro_x, goleiro_dest = 400, 400
GOLEIRO_Y = 225 
img_ronaldinho_atual = ronaldinho_base
img_kahn_atual = kahn_base
res_txt = ""

# Efeitos
shake_timer = 0
flash_timer = 0
rastro_bola = [] 
zoom_escala = 1.0
vencedor_nome = ""

def desenhar_texto_com_contorno(texto, fonte, cor_texto, cor_contorno, x, y):
    # Renderiza o contorno (desenhando em volta)
    for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
        contorno = fonte.render(texto, True, cor_contorno)
        tela.blit(contorno, (x + dx, y + dy))
    # Renderiza o texto principal
    principal = fonte.render(texto, True, cor_texto)
    tela.blit(principal, (x, y))

def desenhar_botao(texto, y, mouse_pos):
    rect = pygame.Rect(350, y, 300, 50)
    selecionado = rect.collidepoint(mouse_pos)
    cor = (0, 200, 0) if selecionado else AZUL
    pygame.draw.rect(tela, cor, rect, border_radius=12)
    pygame.draw.rect(tela, BRANCO, rect, 2, border_radius=12)
    txt = fonte_lista.render(texto, True, BRANCO)
    tela.blit(txt, (rect.centerx - txt.get_width()//2, rect.centery - txt.get_height()//2))
    return rect

relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    mouse_pos = pygame.mouse.get_pos()
    clicou_esquerdo = False
    clicou_direito = False
    
    offset_x, offset_y = 0, 0
    if shake_timer > 0:
        offset_x = random.randint(-6, 6)
        offset_y = random.randint(-6, 6)
        shake_timer -= 1

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: pygame.quit(); sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1: clicou_esquerdo = True
            if ev.button == 3: clicou_direito = True

        if ev.type == pygame.KEYDOWN and estado_global == "JOGO":
            if estado_penalty == 0:
                if ev.key == pygame.K_UP: idx_aluno = (idx_aluno - 1) % len(lista_jogadores)
                if ev.key == pygame.K_DOWN: idx_aluno = (idx_aluno + 1) % len(lista_jogadores)
                if ev.key == pygame.K_SPACE and chutes_feitos[lista_jogadores[idx_aluno]] < LIMITE_CHUTES:
                    estado_penalty = 1
                    zoom_escala = 1.1

        if ev.type == pygame.JOYBUTTONDOWN and estado_global == "JOGO":
            nome_atual = lista_jogadores[idx_aluno]
            if ev.button == 0 and estado_penalty == 0 and chutes_feitos[nome_atual] < LIMITE_CHUTES:
                estado_penalty = 1
                zoom_escala = 1.1
            if ev.button in [2, 3] and estado_penalty == 1: # Quadrado
                estado_penalty = 2
                zoom_escala = 1.0
                chutes_feitos[nome_atual] += 1 
                goleiro_dest = random.choice([280, 400, 520])
                img_kahn_atual = kahn_esq if goleiro_dest == 280 else (kahn_dir if goleiro_dest == 520 else kahn_centro)
                img_ronaldinho_atual = ronaldinho_impacto
            if ev.button == 1 and estado_penalty == 3: # Bolinha
                if all(c >= LIMITE_CHUTES for c in chutes_feitos.values()):
                    vencedor_nome = max(pontos, key=pontos.get)
                    estado_global = "VITORIA"
                else:
                    bola_x, bola_y, bola_z, goleiro_x, goleiro_dest = 400, 455, 1.0, 400, 400
                    img_kahn_atual, img_ronaldinho_atual, estado_penalty = kahn_base, ronaldinho_base, 0
                    rastro_bola = []

    if clicou_direito:
        estado_global = "MENU"
        estado_penalty = 0

    if estado_global == "MENU":
        tela.blit(img_menu, (0, 0))
        if desenhar_botao("INICIAR JOGO", 320, mouse_pos).collidepoint(mouse_pos) and clicou_esquerdo:
            estado_global = "JOGO"
        if desenhar_botao("INSTRUÇÕES", 390, mouse_pos).collidepoint(mouse_pos) and clicou_esquerdo:
            estado_global = "INSTRUCOES"
        if desenhar_botao("CRÉDITOS", 460, mouse_pos).collidepoint(mouse_pos) and clicou_esquerdo:
            estado_global = "CREDITOS"

    elif estado_global == "VITORIA":
        tela.fill(PRETO)
        v_offset = random.randint(-10, 10)
        txt_venc = fonte_vitoria.render(f"{vencedor_nome} Ganhou o duelo!", True, AMARELO)
        tela.blit(txt_venc, (500 - txt_venc.get_width()//2 + v_offset, 250 + v_offset))
        txt_sub = fonte_titulo.render("CAMPEÃO ABSOLUTO", True, BRANCO)
        tela.blit(txt_sub, (500 - txt_sub.get_width()//2, 360))
        if desenhar_botao("VOLTAR AO MENU", 500, mouse_pos).collidepoint(mouse_pos) and clicou_esquerdo:
            pontos = {n: 0 for n in lista_jogadores}
            chutes_feitos = {n: 0 for n in lista_jogadores}
            estado_global = "MENU"

    elif estado_global == "JOGO":
        if flash_timer > 0:
            tela.fill(random.choice([AMARELO, VERDE]))
            flash_timer -= 1
        else:
            tela.fill(CINZA)
            
        tela.blit(img_campo, (offset_x, offset_y))
        
        if estado_penalty == 1 and pygame.joystick.get_count() > 0:
            joy = pygame.joystick.Joystick(0)
            mira_x = max(250, min(550, mira_x + joy.get_axis(0) * 8))
            mira_y = max(180, min(350, mira_y + joy.get_axis(1) * 8))
            pygame.draw.circle(tela, AMARELO, (int(mira_x), int(mira_y)), 12, 3)

        elif estado_penalty == 2:
            rastro_bola.append((bola_x, bola_y, bola_z))
            if len(rastro_bola) > 8: rastro_bola.pop(0)
            if bola_y > mira_y:
                bola_y -= 12; bola_x += (mira_x - bola_x) * 0.15; bola_z -= 0.02
                if bola_y < 300 and abs(bola_x - goleiro_x) < 90:
                    res_txt, estado_penalty, shake_timer = "DEFENDEU!", 3, 15
                    bola_y, bola_x = 275, goleiro_x
            else:
                estado_penalty = 3
                if 240 < bola_x < 560 and 170 < bola_y < 350:
                    res_txt, flash_timer = "GOOOOOOOL!", 15
                    pontos[lista_jogadores[idx_aluno]] += 1
                else: res_txt, shake_timer = "FORA!", 10
            
            if goleiro_x < goleiro_dest: goleiro_x += 12
            elif goleiro_x > goleiro_dest: goleiro_x -= 12

        # Rastro e Sprites
        for i, pos in enumerate(rastro_bola):
            transp = int((i / len(rastro_bola)) * 150)
            sup = pygame.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.circle(sup, (255, 255, 255, transp), (10, 10), int(10 * pos[2]))
            tela.blit(sup, (pos[0] - 10, pos[1] - 10))

        tela.blit(img_kahn_atual, (goleiro_x - img_kahn_atual.get_width()//2 + offset_x, GOLEIRO_Y + offset_y))
        ron_z = pygame.transform.smoothscale(img_ronaldinho_atual, (int(img_ronaldinho_atual.get_width() * zoom_escala), int(img_ronaldinho_atual.get_height() * zoom_escala)))
        tela.blit(ron_z, (330 - ron_z.get_width()//2 + offset_x, 390 + offset_y))
        dim = int(68 * max(0.3, bola_z))
        tela.blit(pygame.transform.scale(img_bola, (dim, dim)), (int(bola_x) - dim//2, int(bola_y) - dim//2))

        # Ranking Lateral
        pygame.draw.rect(tela, CINZA, (800, 0, 200, 600))
        for i, nome in enumerate(lista_jogadores):
            cor = AMARELO if i == idx_aluno else BRANCO
            txt_rank = f"{nome}: {pontos[nome]} ({LIMITE_CHUTES - chutes_feitos[nome]})"
            tela.blit(fonte_lista.render(txt_rank, True, cor), (810, 50 + (i * 35)))

        # Alerta Superior Aprimorado (Acima do Gol)
        if chutes_feitos[lista_jogadores[idx_aluno]] >= LIMITE_CHUTES and estado_penalty == 0:
            aviso_txt = "SUAS CHANCES ACABARAM!"
            # Centralizado horizontalmente em 400 (meio do campo de jogo) e acima do gol (y=120)
            x_aviso = 400 - (fonte_alerta.size(aviso_txt)[0] // 2)
            desenhar_texto_com_contorno(aviso_txt, fonte_alerta, AMARELO, PRETO, x_aviso, 120)
        
        if estado_penalty == 3:
            r = fonte_titulo.render(res_txt, True, AMARELO)
            tela.blit(r, (400 - r.get_width()//2, 240))

    pygame.display.flip()
    #alterar para que quando acabar as chances e mostrar na tela suas chances acabaram ja pular pro proximo batedor 
    #adicionar sons 
    #pedir pra fazer arquivo download para baixar o jogo 
    #subir no github
    #postar no portfolio
    