import json

# Lendo o arquivo JSON com os dados do faturamento diário
with open('faturamento.json') as f:
    dados = json.load(f)

# Calculando o menor e o maior valor de faturamento ocorrido em um dia do mês
menor_valor = min(dados)
maior_valor = max(dados)

# Calculando a média mensal de faturamento, ignorando os dias sem faturamento
soma_faturamento = 0
dias_com_faturamento = 0
for valor in dados:
    if valor != 0:
        soma_faturamento += valor
        dias_com_faturamento += 1
media_mensal = soma_faturamento / dias_com_faturamento

# Contando o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = 0
for valor in dados:
    if valor > media_mensal:
        dias_acima_da_media += 1

# Imprimindo os resultados
print("Menor valor de faturamento diário: R$ {:.2f}".format(menor_valor))
print("Maior valor de faturamento diário: R$ {:.2f}".format(maior_valor))
print("Número de dias com faturamento acima da média mensal: {}".format(dias_acima_da_media))
