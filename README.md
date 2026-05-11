```markdown
# Super Penalty 2026 ⚽🕹️

Um simulador arcade de cobranças de pênalti (Ronaldinho vs Kahn) desenvolvido em **Python** utilizando a biblioteca **Pygame**. Este projeto explora lógica de física de colisão, controle de estados, animações em tempo real e integração de hardware (HID).

## 🚀 Funcionalidades

*   **Integração DualShock 4:** Suporte completo para controle de PlayStation 4, mapeando botões de ação e eixo analógico para controle suave da mira.
*   **Game Feel e VFX:** 
    *   *Screen Shake:* Trepidação da câmera em defesas e chutes na trave.
    *   *Motion Blur:* Rastro visual acompanhando a trajetória da bola.
    *   *Dynamic Zoom:* Foco da câmera no batedor durante o momento da mira.
    *   *Screen Flash:* Feedback visual imersivo ao marcar um gol.
*   **Sistema de Competição:** Ranking integrado para 12 jogadores simultâneos, com limite de 5 chutes por participante.
*   **Controle Híbrido:** Menus navegáveis via mouse; gameplay otimizada para controle/teclado.
*   **Detecção de Fim de Jogo:** Cálculo automático do vencedor com tela de celebração dinâmica.

## 🛠️ Tecnologias Utilizadas

*   **Python 3.x**
*   **Pygame** (Gerenciamento de gráficos, áudio, eventos e joysticks)

## 📋 Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina. Para instalar a dependência necessária do projeto, execute:
```bash
pip install pygame

```

## 🎮 Controles

### Menus

* **Mouse Esquerdo:** Confirmar opção
* **Mouse Direito:** Voltar à tela anterior

### Durante o Jogo

* **Setas do Teclado (Cima/Baixo):** Trocar batedor
* **X (Controle) / Espaço (Teclado):** Iniciar mira e ativar o foco
* **Analógico Esquerdo (Controle):** Mover a mira pelo gol
* **Quadrado (Controle):** Realizar o chute
* **Bolinha (Controle):** Reiniciar a jogada para o próximo pênalti

## 📁 Estrutura do Projeto

O projeto espera que os recursos visuais estejam em uma pasta `assets` no mesmo diretório do script principal:

```text
├── main.py
└── assets/
    ├── tela_inicial.png
    ├── campo_2.png
    ├── bola.png
    ├── jogador.png
    ├── ronaldinho_chute.png
    ├── goleiro.png
    ├── kahn_centro.png
    ├── kahn_esquerda.png
    ├── kahn_direita.png
    └── logo_transparente.png

```

## 👨‍💻 Desenvolvedor

**Fernando Vinícius da Silva**
Estudante de Análise e Desenvolvimento de Sistemas (ADS).

```

```
