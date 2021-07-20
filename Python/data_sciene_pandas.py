# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 07:42:09 2020

@author: USER
"""

#Relatorio de Analise VIII
# Identificando e removendo outliers

%matplotlib inline
import pandas as pd 
import matplotlib.pyplot as plt

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')

dados.boxplot(['Valor'])
dados[dados['Valor'] >= 500000]

valor = dados['Valor']

q1 = valor.quantile(.25) # visualizando o 1º quartil;
q3 = valor.quantile(.75) # visualizando o 3º quartil;
seg_q = q3 - q1
limite_inferior = q1 - 1.5 * seg_q
limite_superior = q3 + 1.5 * seg_q

selecao = (valor >= limite_inferior) & (valor <= limite_superior)
dados_new = dados[selecao]

dados_new.boxplot(["Valor"])

dados.boxplot(['Valor'], by = ['Tipo'])

grupo_tipo = dados.groupby('Tipo')['Valor']

q_1 = grupo_tipo.quantile(.25) # 1º quartil;
q_3 = grupo_tipo.quantile(.75) # 3º quartil;
s_Q = q_3 - q_1 # 2º quartil = 3º - 1º quartil;
lim_inf = q_1 - 1.5 * s_Q
lim_sup = q_3 + 1.5 * s_Q

dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= lim_inf[tipo]) & (dados['Valor']) <= lim_sup[tipo]
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])

dados_new.boxplot(['Valor'], by = ['Tipo'])

dados_new.to_csv('aluguel_residencial_sem_outliers.csv', sep = ';', index = False)

# Utilizando matplotlib;

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')
area = plt.figure()

# adicionando graficos;
g1 = area.add_subplot(2, 2, 1) # posição 1 do grafico;
g2 = area.add_subplot(2, 2, 2)
g3 = area.add_subplot(2, 2, 3)
g4 = area.add_subplot(2, 2, 4)

# gerando os graficos;
g1.scatter(dados.Valor, dados.Area)
g1.set_title('Valor x Area')

g2.hist(dados.Valor)
g2.set_title('Histograma')

dados_g3 = dados.Valor.sample(100) # sample() -> amostra aleatoria
dados_g3.index = range(dados_g3.shape[0])
g3.plot(dados_g3)
g3.set_title('Amostra Valor')

grupo = dados.groupby('Tipo')['Valor']
label = grupo.mean().index
valores = grupo.mean().values
g4.bar(label, valores)
g4.set_title('Valor medio por tipo')

area.savefig('grafico.png', dpi = 300, bbox_inches = 'tuight') 
# dpi -> definição imagem
# bbox -> retira as bordas da imagem
















