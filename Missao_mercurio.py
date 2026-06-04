#definindo dados da missao
dados_missao = [
    [20, 86, 93, 97, 95],
    [25, 83, 85, 93, 90],
    [27, 79, 76, 89, 78],
    [32, 69, 63, 85, 69],
    [38, 50, 49, 79, 44],
    [36, 38, 38, 83, 34]
]
areas_monitoradas = [
 "Temperatura interna",
 "Comunicação com a base",
 "Sistema de energia",
 "Suporte de oxigênio",
 "Estabilidade operacional"
]

#Variaveis:

temperatura = 0
comunicacao = 0
bateria = 0
oxigenio = 0 
estabilidade = 0
nivel = 0 


#função de analise e avaliação de temperatura

def analisar_temperatura(temperatura):
    if temperatura < 18:
        return "Atenção"
    elif temperatura >= 18 and temperatura < 30:
        return "Normal"
    elif temperatura <= 35:
        return "Atenção"
    else:
        return "Crítico"  
analisar_temperatura(temperatura)

def avaliacao_temperatura(temperatura):
    if temperatura < 18:
        return "Risco de sub-resfriamento"
    elif temperatura >= 18 and temperatura < 30:
        return "Temperatura estável"
    elif temperatura <= 35:
        return "Temperatura acima do recomendado"
    else:
        return "Risco de superaquecimento"  
avaliacao_temperatura(temperatura)

#função de analise e avaliação de comunicação

def analisar_comunicacao(comunicacao):
    if comunicacao < 30:
        return "Crítico"
    elif comunicacao >= 30 and comunicacao <= 59:
        return "Atenção"
    else:
        return "Normal"


def avaliacao_comunicacao(comunicacao):
    if comunicacao < 30:
        return "Comunicação severamente comprometida"
    elif comunicacao >= 30 and comunicacao <= 59:
        return "Comunicação em nível de alerta"
    else:
        return "Comunicação estável"


#função de analise e avaliação de bateria

def analisar_bateria(bateria):
    if bateria < 20:
        return "Crítico"
    elif bateria >= 20 and bateria <= 49:
        return "Atenção"
    else:
        return "Normal"


def avaliacao_bateria(bateria):
    if bateria < 20:
        return "Nível crítico de bateria"
    elif bateria >= 20 and bateria <= 49:
        return "Nível de bateria abaixo do ideal"
    else:
        return "Nível de bateria ideal"


#função de analise e avaliação de oxigenio

def analisar_oxigenio(oxigenio):
    if oxigenio < 80:
        return "Crítico"
    elif oxigenio >= 80 and oxigenio <= 89:
        return "Atenção"
    else:
        return "Normal"


def avaliacao_oxigenio(oxigenio):
    if oxigenio < 80:
        return "Concentração de oxigênio em estado crítico"
    elif oxigenio >= 80 and oxigenio <= 89:
        return "Níveis de oxigênio reduzidos"
    else:
        return "Oxigênio em condição estável"


#função de analise e avaliação de estabilidade

def analisar_estabilidade(estabilidade):
    if estabilidade < 40:
        return "Crítico"
    elif estabilidade >=40 and estabilidade <= 69:
        return "Atenção"
    else:
        return "Normal"


def avaliacao_estabilidade(estabilidade):
    if estabilidade < 40:
        return "Estabilidade severamente comprometida"
    elif estabilidade >=40 and estabilidade <= 69:
        return "Estabilidade abaixo do ideal"
    else:
        return "Estabilidade dentro dos parâmetros esperados"


#classificação de ciclo

def classificar_ciclo(dados_missao):
    pontuacoes = []
    for i in range(len(dados_missao)):
        pontuacao_total = 0
        temperatura = dados_missao[i][0]
        
        if temperatura < 18:
            pontuacao_total += 1
        elif temperatura >= 18 and temperatura < 30:
            pontuacao_total += 0
        elif temperatura >= 30 and temperatura <= 35:
            pontuacao_total += 1
        else:
            pontuacao_total += 2

        comunicacao = dados_missao[i][1]
        if comunicacao < 30:
            pontuacao_total += 2
        elif comunicacao >= 30 and comunicacao <= 59:
            pontuacao_total += 1
        else:
            pontuacao_total += 0
    
        bateria = dados_missao[i][2]
        if bateria < 20:
            pontuacao_total += 2
        elif bateria >= 20 and bateria <= 49:
            pontuacao_total += 1
        else:
            pontuacao_total += 0

        oxigenio = dados_missao[i][3]
        if oxigenio < 80:
            pontuacao_total += 2
        elif oxigenio >= 80 and oxigenio <= 89:
            pontuacao_total += 1
        else:
            pontuacao_total += 0

        estabilidade = dados_missao[i][4]
        if estabilidade < 40:
            pontuacao_total += 2
        elif estabilidade >=40 and estabilidade <= 69:
            pontuacao_total += 1
        else:
            pontuacao_total += 0

        # Classificação do ciclo

        if pontuacao_total <= 2:
            classificacao = "MISSÃO ESTÁVEL"
        elif pontuacao_total <= 5:
            classificacao = "MISSÃO EM ATENÇÃO"
        else:
            classificacao = "MISSÃO CRÍTICA"

        pontuacoes.append(pontuacao_total) 

    return pontuacoes
        
pontuacoes = classificar_ciclo(dados_missao)
   

#Analisar as tendencias

def analisar_tendencia(pontuacoes):
    if pontuacoes[0] < pontuacoes [-1]:
        return("A missão demonstrou uma evolução negativa.")
    elif pontuacoes[-1] < pontuacoes[0]:
        return("A missão demonstrou uma evolução positiva.")
    elif pontuacoes[0] == pontuacoes[-1]:
        return("Não foram observadas alterações significativas em relação ao início da missão")
tendencia = analisar_tendencia(pontuacoes)

#identificar a area mais afetada

def identificar_ciclo_mais_critico(pontuacoes):
    mais_afetada = pontuacoes[0]
    ciclo = 1
    for i in range(len(pontuacoes)):
        afetada = pontuacoes[i]

        if afetada > mais_afetada:
            mais_afetada = afetada
            ciclo = i + 1
    return ciclo, mais_afetada
ciclo_critico, maior_pontuacao = identificar_ciclo_mais_critico(pontuacoes)

#Geração de recomendação

def gerar_recomendacao(temperatura,comunicacao,bateria,oxigenio,estabilidade,): 
    recomendacao = ""

    if temperatura < 18 or temperatura > 35:
        recomendacao += ("Os níveis de temperatura atingiram estado crítico, sendo necessária a verificação dos mecanismos de controle térmico\n")
    elif temperatura >= 30 and temperatura <= 35:
        recomendacao += ("Foi identificada uma anomalia na temperatura, exigindo a análise do controle térmico da missão\n")
    if comunicacao < 30:
        recomendacao += ("Foi identificada uma falha crítica na comunicação, exigindo tentativas imediatas de reconexão com a base.\n")
    elif comunicacao >= 30 and comunicacao <= 59:
        recomendacao += ("Os sistemas de comunicação apresentam desempenho inferior ao esperado, sendo necessária a verificação do contato com a base.\n")
    if bateria < 20:
        recomendacao += ("Foi detectado um nível crítico de carga da bateria, exigindo a ativação de medidas de economia energética.\n")
    elif bateria >= 20 and bateria <= 49:
        recomendacao += ("Foi identificado um nível de bateria inferior ao ideal, sendo necessária a otimização do consumo energético.\n")
    if oxigenio < 80:
        recomendacao += ("Foi detectada uma condição crítica nos níveis de oxigênio, exigindo a ativação imediata dos sistemas de suporte à vida.\n")
    elif oxigenio >= 80 and oxigenio <= 89:
        recomendacao += ("Foi identificado um nível de oxigênio inferior ao ideal, sendo necessária a adoção de medidas para otimizar seu consumo.\n")
    if estabilidade < 40:
        recomendacao += ("Foi identificada uma condição crítica de estabilidade, exigindo a suspensão de atividades secundárias.\n")
    elif estabilidade >=40 and estabilidade <= 69:
        recomendacao += ("Foi identificado um nível de estabilidade inferior ao ideal, exigindo a análise das operações atualmente em execução.\n")
    if recomendacao == "":
        recomendacao = "Condições estáveis. Continuar o monitoramento."
    return recomendacao
recomendacao = gerar_recomendacao(temperatura,comunicacao,bateria,oxigenio,estabilidade)

#Calculo de medias

def calcular_media(dados_missao, coluna):
    soma = 0

    for i in range(len(dados_missao)):
        soma += dados_missao[i][coluna]

    media = soma / len(dados_missao)

    return media

#Soma de riscos da missão

def soma_de_riscos(pontuacoes):
    soma = 0
    
    for i in range(len(pontuacoes)):
        soma += pontuacoes[i]

    media = soma / (len(pontuacoes))
    
    return media
media_risco = soma_de_riscos(pontuacoes)

def classificacao_final_missao(media_risco):
    if media_risco <= 2:
        classificacao = "MISSÃO ESTÁVEL"
    elif media_risco <= 5:
        classificacao = "MISSÃO EM ATENÇÃO"
    else:
        classificacao = "MISSÃO CRÍTICA"
    return classificacao
classificacao = classificacao_final_missao(media_risco)

#Identificar ciclo critico

def identificar_ciclos_criticos(pontuacoes):
    quantidade = 0

    for i in range(len(pontuacoes)):
        if pontuacoes[i] > 5:
            quantidade += 1

    return quantidade
quantidade_criticos = identificar_ciclos_criticos(pontuacoes)

#Calcular risco por area

def pontuar_temperatura(temperatura, dados_missao):
    pontos_temperatura = 0
    for i in range(len(dados_missao)):
        temperatura = dados_missao[i][0]

        if temperatura < 18:
            pontos_temperatura += 1
        elif temperatura >= 18 and temperatura < 30:
            pontos_temperatura += 0
        elif temperatura <= 35:
            pontos_temperatura += 1
        else:
            pontos_temperatura += 2
    return pontos_temperatura
pontos_temperatura = pontuar_temperatura(temperatura, dados_missao)

def pontuar_comunicacao(comunicacao, dados_missao):
    pontos_comunicacao = 0
    for i in range(len(dados_missao)):
        comunicacao = dados_missao[i][1]

        if comunicacao < 30:
            pontos_comunicacao += 2
        elif comunicacao >= 30 and comunicacao <= 59:
            pontos_comunicacao += 1
        else:
            pontos_comunicacao += 0

    return pontos_comunicacao
pontos_comunicacao = pontuar_comunicacao(comunicacao, dados_missao)


def pontuar_bateria(bateria, dados_missao):
    pontos_bateria = 0
    for i in range(len(dados_missao)):
        bateria = dados_missao[i][2]

        if bateria < 20:
            pontos_bateria += 2
        elif    bateria >= 20 and bateria <= 49:
            pontos_bateria += 1
        else:
            pontos_bateria += 0
    return pontos_bateria
pontos_bateria = pontuar_bateria(bateria, dados_missao)

def pontuar_oxigenio(oxigenio, dados_missao):
    pontos_oxigenio = 0
    for i in range(len(dados_missao)):
        oxigenio = dados_missao[i][3]

        if oxigenio < 80:
            pontos_oxigenio += 2
        elif oxigenio >= 80 and oxigenio <= 89:
            pontos_oxigenio += 1
        else:
            pontos_oxigenio += 0
    return pontos_oxigenio
pontos_oxigenio = pontuar_oxigenio(oxigenio, dados_missao)

def pontuar_estabilidade(estabilidade, dados_missao):
    pontos_estabilidade = 0
    for i in range(len(dados_missao)):
        estabilidade = dados_missao[i][4]
        if estabilidade < 40:
            pontos_estabilidade += 2
        elif estabilidade >=40 and estabilidade <= 69:
            pontos_estabilidade += 1
        else:
            pontos_estabilidade += 0
    return pontos_estabilidade
pontos_estabilidade = pontuar_estabilidade(estabilidade, dados_missao)

#Área mais afetada:

def area_mais_afetada(pontos_temperatura,pontos_comunicacao,pontos_estabilidade,pontos_oxigenio,pontos_bateria):
    maior = pontos_oxigenio
    area = "Suporte de oxigênio"
    
    if pontos_comunicacao > maior:
        maior = pontos_comunicacao
        area = "Comunicação com a base"
    
    if pontos_bateria > maior:
        maior = pontos_bateria
        area = "Sistema de energia"
    
    if pontos_temperatura > maior:
        maior = pontos_temperatura
        area = "Temperatura interna"
    
    if pontos_estabilidade > maior:
        maior = pontos_estabilidade
        area = "Estabilidade operacional"

    return area

area = area_mais_afetada(pontos_temperatura,pontos_comunicacao,pontos_estabilidade,pontos_oxigenio,pontos_bateria)

#conclussão da misssão

def conclusao_missao(tendencia):
    if tendencia == "A missão demonstrou uma evolução negativa.":
        return("A missão demonstrou uma evolução negativa. "
        "O aumento progressivo dos riscos resultou em ciclos críticos e comprometeu diferentes sistemas da operação."
        "Apesar da continuidade da missão, recomenda-se atenção reforçada e ações corretivas para restabelecer condições seguras de funcionamento.")
    elif tendencia == "A missão demonstrou uma evolução positiva.":
        return("A missão demonstrou uma evolução positiva."
            "Os indicadores apresentaram melhora ao longo da operação, reduzindo o nível de risco e aumentando a estabilidade dos sistemas monitorados. Recomenda-se manter o monitoramento para garantir a continuidade dessa recuperação.")
    elif tendencia == "Não foram observadas alterações significativas em relação ao início da missão":
        return("Não foram observadas alterações significativas em relação ao início da missão."
               "Os sistemas permaneceram relativamente estáveis durante a operação, mantendo um nível de risco semelhante ao registrado nos ciclos iniciais. Recomenda-se a continuidade do monitoramento preventivo")
conclusao = conclusao_missao(tendencia)          


#relatorio

def gerar_relatorio(dados_missao,pontuacoes):
            
    print("===============================================")
    print("Mission Control AI")
    print("===============================================")
    print("Missão: Mercurio Omega")
    print("Equipe: Equipe Eros")
    print("Quantidade de ciclos analisados: 6")
    print("===============================================")

    for i in range(len(dados_missao)):
        temperatura = dados_missao[i][0]
        comunicacao = dados_missao[i][1]
        bateria = dados_missao[i][2]
        oxigenio = dados_missao[i][3]
        estabilidade = dados_missao[i][4]
        pontuacao = pontuacoes[i]
        nivel_de_temperatura = analisar_temperatura(temperatura)
        nivel_de_comunicacao = analisar_comunicacao(comunicacao)
        nivel_de_bateria = analisar_bateria(bateria)
        nivel_de_oxigenio = analisar_oxigenio(oxigenio)
        nivel_de_estabilidade = analisar_estabilidade(estabilidade)
        estado_temperatura = avaliacao_temperatura(temperatura)
        estado_comunicacao = avaliacao_comunicacao(comunicacao)
        estado_bateria = avaliacao_bateria(bateria)
        estado_oxigenio = avaliacao_oxigenio(oxigenio)
        estado_estabilidade = avaliacao_estabilidade(estabilidade)
        
        recomendacao = gerar_recomendacao(temperatura,comunicacao,bateria,oxigenio,estabilidade)
        

        if pontuacao <= 2:
            classificacao = "MISSÃO ESTÁVEL"
        elif pontuacao <= 5:
            classificacao = "MISSÃO EM ATENÇÃO"
        else:
            classificacao = "MISSÃO CRÍTICA"


        print()
        print("CICLO: ", i + 1)
        print("-----------------------------------------------")
        print("Temperatura:", temperatura,"°C", "|", nivel_de_temperatura, "|", estado_temperatura)
        print("Comunicação:",comunicacao, "%", "|", nivel_de_comunicacao, "|", estado_comunicacao)
        print("Bateria:", bateria,"%", "|", nivel_de_bateria, "|", estado_bateria)
        print("Oxigenio:", oxigenio,"%", "|",nivel_de_oxigenio, "|", estado_oxigenio)
        print("Estabilidade","%", estabilidade, "|",nivel_de_estabilidade, "|", estado_estabilidade )
        print()
        print("Pontuação de risco do ciclo:", pontuacao)
        print("Classificação do ciclo:", classificacao)
        print("Recomendação: ", recomendacao)
        print()
gerar_relatorio(dados_missao,pontuacoes)

#Relatorio final

def gerar_relatorio_final(dados_missao,pontuacoes,temperatura,comunicacao,bateria,oxigenio,estabilidade,media_risco):

    media_temp = calcular_media(dados_missao, 0)
    media_comunic = calcular_media(dados_missao, 1)
    media_bateria = calcular_media(dados_missao, 2)
    media_oxigenio = calcular_media(dados_missao, 3)
    media_estabilidade = calcular_media(dados_missao, 4)
    ciclo_critico, maior_pontuacao = identificar_ciclo_mais_critico(pontuacoes)
    media_risco = soma_de_riscos(pontuacoes)
    quantidade_criticos = identificar_ciclos_criticos(pontuacoes)
    tendencia = analisar_tendencia(pontuacoes)
    pontos_temperatura = pontuar_temperatura(temperatura, dados_missao)
    pontos_comunicacao = pontuar_comunicacao(comunicacao, dados_missao)
    pontos_bateria = pontuar_bateria(bateria, dados_missao)
    pontos_oxigenio = pontuar_oxigenio(oxigenio, dados_missao)
    pontos_estabilidade = pontuar_estabilidade(estabilidade, dados_missao)
    classificacao = classificacao_final_missao(media_risco)
    conclusao = conclusao_missao(tendencia)
    area = area_mais_afetada(pontos_temperatura,pontos_comunicacao,pontos_estabilidade,pontos_oxigenio,pontos_bateria)

    print("===============================================")
    print("RELATÓRIO DE STATUS FINAL DA MISSÃO")
    print("===============================================")
    print("Missão: Mercurio Omega")
    print("Equipe: Equipe Eros")
    print()
    print("Quantidade de ciclos analisados: 6")
    print()
    print(f"Média de temperatura: {media_temp:.2f}°C")
    print(f"Média de comunicação: {media_comunic:.2f}%")
    print(f"Média de bateria: {media_bateria:.2f}%")
    print(f"Média de oxigênio: {media_oxigenio:.2f}%")
    print(f"Média de estabilidade: {media_estabilidade:.2f}%")
    print()
    print("Ciclo mais crítico:",ciclo_critico)
    print("Maior pontuação de risco: ",maior_pontuacao)
    print(f"Risco médio da missão: {media_risco:.2f}")
    print("Quantidade de ciclos críticos:",quantidade_criticos)
    print()
    print("Tendência da missão:")
    print(tendencia)
    print()
    print("Pontuação acumulada por área:",)
    print("Temperatura interna:",pontos_temperatura)
    print("Comunicação com a base:",pontos_comunicacao)
    print("Sistema de energia:",pontos_bateria)
    print("Suporte de oxigênio:",pontos_oxigenio)
    print("Estabilidade operacional:",pontos_estabilidade)
    print()
    print("Área mais afetada:")
    print(area)
    print()
    print("Classificação final da missão:")
    print(classificacao)
    print()
    print("Conclusão:")
    print(conclusao)
gerar_relatorio_final(dados_missao,pontuacoes,temperatura,comunicacao,bateria,oxigenio,estabilidade,media_risco)