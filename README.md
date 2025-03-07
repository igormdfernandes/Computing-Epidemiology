# Modelagem Computacional do Crescimento Bacteriano

Este repositório apresenta um modelo baseado em autômatos celulares para simular a dinâmica do crescimento bacteriano sob diferentes condições ambientais. A simulação permite explorar os impactos da administração de antibacterianos, limitação de nutrientes e barreiras físicas, além de investigar o surgimento de resistência microbiana.

## Objetivos

A modelagem proposta permite:

Analisar padrões de crescimento de colônias bacterianas ao longo do tempo.

Simular efeitos de restrições ambientais na proliferação de microrganismos.

Estudar a eficiência do uso de antibacterianos no controle das populações microbianas.

Investigar o desenvolvimento de resistência a antibióticos em um sistema simulado.

Avaliar o impacto de barreiras físicas no controle do crescimento bacteriano.

## Fundamentação Teórica

A modelagem do crescimento microbiano baseia-se em princípios de dinâmica populacional e interação ambiental. O modelo se inspira nos conceitos apresentados por autores como:

Murray, J. D. (2003). Mathematical Biology.

Nowak, M. A., & May, R. M. (2000). Virus Dynamics: Mathematical Principles of Immunology and Virology.

Edelstein-Keshet, L. (2005). Mathematical Models in Biology.

## Estrutura da Simulação

O modelo opera em um espaço discreto onde cada célula representa uma região do meio de cultura. A evolução do sistema segue regras de transição baseadas em interações locais e disponibilidade de recursos.

As principais variáveis da simulação incluem:

Taxa de crescimento bacteriano: Depende da disponibilidade de nutrientes e espaço.

Efeito de antibacterianos: Influencia a taxa de mortalidade e resistência.

Barreiras físicas: Limitam a propagação das colônias.

Mutabilidade: Possibilita o surgimento de variantes resistentes.

# Executando a Simulação

## 1 **Clonando o Repositório**
```bash
git clone https://github.com/YOUR-USERNAME/Computing-Epidemiology.git
```

## 2. Configuração do Ambiente

Certifique-se de ter o Python instalado. Instale as dependências necessárias com:

pip install numpy matplotlib

## 3. Rodando o Modelo

Execute o script principal:

python main.py

Isso gerará visualizações gráficas da evolução do crescimento bacteriano.

## Considerações Científicas

Este modelo computacional permite explorar mecanismos fundamentais de resistência e disseminação bacteriana. Os resultados podem ser utilizados para compreender a dinâmica epidemiológica e o impacto de estratégias de controle de infecções.