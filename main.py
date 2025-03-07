import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

TAMANHO_DOMINIO = 100
TEMPO_TOTAL = 50
PASSOS_TEMPO = 100
DIFUSAO_BACTERIA = 0.1
DIFUSAO_ANTIBIOTICO = 0.2
TAXA_CRESCIMENTO = 0.3
CAPACIDADE_SUPORTE = 1.0
TAXA_MORTALIDADE = 0.1
DECAIMENTO_ANTIBIOTICO = 0.05
PROB_RESISTENCIA = 0.05

kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])

bacteria = np.zeros((TAMANHO_DOMINIO, TAMANHO_DOMINIO))
antibiotico = np.zeros((TAMANHO_DOMINIO, TAMANHO_DOMINIO))
resistente = np.zeros((TAMANHO_DOMINIO, TAMANHO_DOMINIO))

bacteria[TAMANHO_DOMINIO//2, TAMANHO_DOMINIO//2] = 0.5
antibiotico[TAMANHO_DOMINIO//4, TAMANHO_DOMINIO//4] = 1.0

def atualizar_sistema(bacteria, antibiotico, resistente):
    bacteria += DIFUSAO_BACTERIA * convolve(bacteria, kernel, mode='reflect')
    antibiotico += DIFUSAO_ANTIBIOTICO * convolve(antibiotico, kernel, mode='reflect')   
    bacteria += TAXA_CRESCIMENTO * bacteria * (1 - bacteria / CAPACIDADE_SUPORTE)  
    morte = TAXA_MORTALIDADE * antibiotico * bacteria
    bacteria -= morte
    resistente += PROB_RESISTENCIA * morte
    antibiotico -= DECAIMENTO_ANTIBIOTICO * antibiotico
    bacteria = np.clip(bacteria, 0, CAPACIDADE_SUPORTE)
    antibiotico = np.clip(antibiotico, 0, 1.0)
    resistente = np.clip(resistente, 0, CAPACIDADE_SUPORTE)
    
    return bacteria, antibiotico, resistente

plt.figure()
for passo in range(PASSOS_TEMPO):
    bacteria, antibiotico, resistente = atualizar_sistema(bacteria, antibiotico, resistente)
    if passo % 10 == 0:
        plt.clf()
        plt.imshow(bacteria + resistente, cmap='viridis', vmin=0, vmax=CAPACIDADE_SUPORTE)
        plt.colorbar(label='Densidade Bacteriana')
        plt.title(f"Tempo: {passo}")
        plt.pause(0.1)

plt.show()