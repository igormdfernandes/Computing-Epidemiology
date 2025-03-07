import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors

# Estados das células
VAZIO, MICROBIO, OBSTACULO, MORTO, RESISTENTE = 0, 1, 2, 3, 4

# Parâmetros principais
TAMANHO_GRADE = 50
PASSOS = 50
PROB_CRESCIMENTO = 0.3
TAXA_MORTALIDADE = 0.1
PROB_RESISTENCIA = 0.05
EFICACIA_ANTIBIOTICO = 0.8

# Inicialização da grade
ambiente = np.zeros((TAMANHO_GRADE, TAMANHO_GRADE), dtype=int)

# Posições iniciais das bactérias
for _ in range(5):
    linha, coluna = np.random.randint(0, TAMANHO_GRADE, size=2)
    ambiente[linha, coluna] = MICROBIO

# Inserindo barreiras aleatórias
for _ in range(3):
    linha, coluna = np.random.randint(0, TAMANHO_GRADE, size=2)
    ambiente[max(0, linha-2):min(TAMANHO_GRADE, linha+2), max(0, coluna-2):min(TAMANHO_GRADE, coluna+2)] = OBSTACULO

def atualizar(_):
    global ambiente
    nova_grade = ambiente.copy()
    
    for linha in range(1, TAMANHO_GRADE - 1):
        for coluna in range(1, TAMANHO_GRADE - 1):
            if ambiente[linha, coluna] == VAZIO:
                # Crescimento bacteriano baseado em vizinhança
                vizinhos = [ambiente[linha-1, coluna], ambiente[linha+1, coluna], ambiente[linha, coluna-1], ambiente[linha, coluna+1]]
                if MICROBIO in vizinhos and np.random.rand() < PROB_CRESCIMENTO:
                    nova_grade[linha, coluna] = MICROBIO
            elif ambiente[linha, coluna] == MICROBIO:
                # Mortalidade e resistência
                if np.random.rand() < TAXA_MORTALIDADE:
                    nova_grade[linha, coluna] = RESISTENTE if np.random.rand() < PROB_RESISTENCIA else MORTO
                elif np.random.rand() < EFICACIA_ANTIBIOTICO:
                    nova_grade[linha, coluna] = MORTO
    
    ambiente[:] = nova_grade
    matriz.set_data(ambiente)
    return [matriz]

# Configuração visual
mapa_cores = mcolors.ListedColormap(["white", "green", "gray", "red", "blue"])
norma = mcolors.BoundaryNorm([0, 1, 2, 3, 4, 5], mapa_cores.N)

figura, eixo = plt.subplots()
matriz = eixo.matshow(ambiente, cmap=mapa_cores, norm=norma)
animacao = animation.FuncAnimation(figura, atualizar, frames=PASSOS, interval=200, blit=True)
plt.show()
