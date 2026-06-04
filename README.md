# Mission Control AI

## Sobre o projeto

O **Mission Control AI** é um sistema desenvolvido em Python para simular o monitoramento inteligente de uma missão espacial experimental.

O programa analisa diferentes ciclos da missão com base em dados simulados de:

- Temperatura interna
- Comunicação com a base
- Sistema de energia
- Suporte de oxigênio
- Estabilidade operacional

A partir desses dados, o sistema calcula o risco de cada ciclo, classifica a situação da missão, identifica ciclos críticos, aponta a área mais afetada e gera recomendações automáticas.

## Nome da missão

**Mercurio Omega**

## Nome da equipe

**Equipe Eros**

## Objetivo

O objetivo do projeto é criar uma prova de conceito em Python capaz de auxiliar no acompanhamento de uma missão espacial, utilizando regras lógicas para identificar riscos e apoiar a tomada de decisão.

## Como o sistema funciona

O sistema utiliza uma matriz chamada `dados_missao`, onde cada linha representa um ciclo de monitoramento e cada coluna representa uma informação da missão.

```python
dados_missao = [
    [20, 86, 93, 97, 95],
    [25, 83, 85, 93, 90],
    [27, 79, 76, 89, 78],
    [32, 69, 63, 85, 69],
    [38, 50, 49, 79, 44],
    [36, 38, 38, 83, 34]
]
```

A ordem dos dados em cada ciclo é:

```python
[temperatura, comunicacao, bateria, oxigenio, estabilidade]
```

## Áreas monitoradas

```python
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]
```

## Regras de classificação

Cada área monitorada pode ser classificada como:

- **Normal**
- **Atenção**
- **Crítico**

Cada classificação gera uma pontuação de risco:

- Normal: 0 ponto
- Atenção: 1 ponto
- Crítico: 2 pontos

Como cada ciclo possui 5 áreas monitoradas, a pontuação máxima de um ciclo é 10 pontos.

## Regras utilizadas

### Temperatura

| Condição | Classificação |
|---|---|
| Menor que 18 °C | Atenção |
| De 18 °C até menor que 30 °C | Normal |
| De 30 °C até 35 °C | Atenção |
| Maior que 35 °C | Crítico |

### Comunicação

| Condição | Classificação |
|---|---|
| Menor que 30% | Crítico |
| De 30% até 59% | Atenção |
| 60% ou mais | Normal |

### Bateria

| Condição | Classificação |
|---|---|
| Menor que 20% | Crítico |
| De 20% até 49% | Atenção |
| 50% ou mais | Normal |

### Oxigênio

| Condição | Classificação |
|---|---|
| Menor que 80% | Crítico |
| De 80% até 89% | Atenção |
| 90% ou mais | Normal |

### Estabilidade

| Condição | Classificação |
|---|---|
| Menor que 40% | Crítico |
| De 40% até 69% | Atenção |
| 70% ou mais | Normal |

## Classificação do ciclo

Depois de somar os pontos de risco, cada ciclo é classificado da seguinte forma:

| Pontuação | Classificação |
|---|---|
| 0 a 2 pontos | Missão Estável |
| 3 a 5 pontos | Missão em Atenção |
| 6 a 10 pontos | Missão Crítica |

## Funcionalidades implementadas

O sistema possui as seguintes funcionalidades:

- Análise de temperatura
- Análise de comunicação
- Análise de bateria
- Análise de oxigênio
- Análise de estabilidade
- Cálculo da pontuação de risco por ciclo
- Classificação de cada ciclo da missão
- Identificação do ciclo mais crítico
- Contagem da quantidade de ciclos críticos
- Cálculo da média dos indicadores
- Análise da tendência da missão
- Identificação da área mais afetada
- Geração de recomendações automáticas
- Relatório detalhado por ciclo
- Relatório final da missão

## Principais funções

Algumas das principais funções do projeto são:

```python
analisar_temperatura()
analisar_comunicacao()
analisar_bateria()
analisar_oxigenio()
analisar_estabilidade()
classificar_ciclo()
analisar_tendencia()
identificar_ciclo_mais_critico()
gerar_recomendacao()
gerar_relatorio()
gerar_relatorio_final()
```

## Saída do sistema

Ao executar o programa, o terminal exibe:

1. Relatório individual de cada ciclo.
2. Classificação de risco do ciclo.
3. Recomendações automáticas.
4. Relatório final da missão.
5. Médias gerais dos indicadores.
6. Tendência da missão.
7. Área mais afetada.
8. Classificação final.

## Como executar o projeto

1. Baixe ou clone este repositório.
2. Abra o arquivo `mission_control.py` em uma IDE ou editor de código.
3. Execute o arquivo com Python.

Exemplo pelo terminal:

```bash
python mission_control.py
```

## Tecnologias utilizadas

- Python 3
- Listas
- Matrizes
- Funções
- Estruturas condicionais
- Estruturas de repetição
- Operações matemáticas básicas

## Conclusão

O projeto **Mission Control AI** demonstra como o pensamento computacional pode ser aplicado para resolver problemas de monitoramento e tomada de decisão. Por meio de regras lógicas, o sistema consegue analisar dados simulados de uma missão espacial, identificar riscos, gerar alertas e apresentar um relatório final com informações úteis para a operação.

## Integrantes

- Matheus Pimenta - RM 569400
- Lucas Seiji - RM 569673
- Leonardo Soares Rodrigues RM:572986 
