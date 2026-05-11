# Super Penalty 2026 ⚽🕹️

Um simulador arcade de cobranças de pênalti (Ronaldinho vs Kahn) desenvolvido em **Python** utilizando a biblioteca **Pygame**. Este projeto explora lógica de física de colisão, controle de estados, animações em tempo real e integração de hardware (HID).

## ⬇️ Download do Jogo (Versão Windows)

Não quer instalar o Python? Sem problemas! 
Você pode baixar o jogo pronto para rodar no Windows (arquivo `.exe`) diretamente na nossa página de Lançamentos:
👉 **[Clique aqui para acessar a aba Releases e baixar o jogo]** *(Nota: Quando colar no LinkedIn, você pode colocar o link direto aqui)*

## 🚀 Funcionalidades

* **Integração DualShock 4:** Suporte completo para controle de PlayStation 4, mapeando botões de ação e eixo analógico para controle suave da mira.
* **Game Feel e VFX:** * *Screen Shake:* Trepidação da câmera em defesas e chutes na trave.
    * *Motion Blur:* Rastro visual acompanhando a trajetória da bola.
    * *Dynamic Zoom:* Foco da câmera no batedor durante o momento da mira.
    * *Screen Flash:* Feedback visual imersivo ao marcar um gol.
* **Sistema de Competição:** Ranking integrado para 12 jogadores simultâneos, com limite de 5 chutes por participante. Pulo automático de turno (Auto-Skip).
* **Controle Híbrido:** Menus navegáveis via mouse; gameplay otimizada para controle/teclado.
* **Detecção de Fim de Jogo:** Cálculo automático do vencedor com tela de celebração dinâmica.

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Python 3.12** e **Pygame 2.6** (Gerenciamento de gráficos, eventos e joysticks).
* **Visual Studio Code (VS Code)** como IDE principal.
* **Inteligência Artificial (Google Gemini):** Utilizada como assistente de pair-programming para estruturação lógica, refatoração de código, síntese generativa dos recursos visuais (assets/sprites) e documentação.

## 📋 Pré-requisitos (Para Desenvolvedores)

Caso queira rodar o projeto direto do código-fonte, certifique-se de ter o Python instalado. Para instalar a dependência necessária, execute no terminal:

```bash
pip install pygame
