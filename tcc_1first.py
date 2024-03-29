# -*- coding: utf-8 -*-
"""tcc-1first.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xhbOBTNpPAggSu_wfuw3Q0xuhQR_oIcZ
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
# %matplotlib inline
# %pylab inline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import seaborn as sns
plt.style.use('ggplot')

plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'

# Carregando a base de dados:
dataset = pd.read_csv('mencoes-cr.csv')

# Visualizando as 5 primeiras linhas do Dataframe:
dataset.head()

dataset.shape

#As 10 mais citadas 
dataabc = dataset["citadas"].value_counts(dropna=True)[:5] 

dataabc = dataabc.rename_axis('citadas').reset_index(name='counts')

dataabc.head(10)

#Deputados que mais tuitaram  
#Os 10 que mais tuitaram 
usernames_data = dataset["nome_eleitoral"].value_counts(dropna=True) 

usernames_data = usernames_data.rename_axis('nome_eleitoral').reset_index(name='counts')

usernames_data.head(10)

len(usernames_data)

usernames = list(usernames_data['nome_eleitoral'][:10]) 
contagem = list(usernames_data['counts'][:10]) 
   
fig = plt.figure(figsize = (4, 4)) 
# creating the bar plot 
plt.barh(usernames, contagem, color ='black') 
  
plt.ylabel("Nome eleitoral") 
plt.xlabel("Quantidade de tweets")  
plt.show()

citacoes = list(dataabc['citadas']) 
qtds = list(dataabc['counts']) 
   
fig = plt.figure(figsize = (4, 3)) 

plt.bar(citacoes, qtds, color ='black') 
  
plt.xlabel("Citação") 
plt.ylabel("Quantidade") 
#plt.title("As cinco mais citadas pelos parlamentares") 

plt.show()

#Agrupamento das citações por partido
agrupamentoPorPartidoCitacoes = dataset.groupby('partido')[u'citadas'].value_counts()

agrupamentoPorPartidoCitacoes.rename_axis().reset_index(name='counts')

def graficosMaisCitadas(proposicao):

  df2 = dataset[dataset['citadas'] == proposicao]
  df2 = df2.groupby(u'citadas')['partido'].value_counts(ascending=False).rename_axis().reset_index(name='counts')

  cincoPartidos = df2.iloc[:5]

  fig = plt.figure(figsize = (4, 2)) 

  partidos = list(cincoPartidos['partido'])
  interacoes = list(cincoPartidos['counts'])

  plt.xlabel("Partido") 
  plt.ylabel("Quantidade") 
  plt.bar(partidos, interacoes, color ='black',  width = 0.5)
  plt.show()

dfx = dataset[dataset['citadas'] == 'MP 927']
#dfx = dfx.groupby(u'citadas')['nome_eleitoral']#.value_counts(ascending=False).rename_axis().reset_index(name='counts')

dfx = dfx[dfx['nome_eleitoral'] == 'PAULO PAIM'] 

dfx

graficosMaisCitadas('MP 927')

graficosMaisCitadas('PL 1075')

graficosMaisCitadas('PEC 45')

graficosMaisCitadas('MP 936')

graficosMaisCitadas('PL 873')

#Agrupamento das citações por nome dos parlamentares
agrupamentoCitacoesNomeEleitoral = dataset.groupby('citadas')[u'nome_eleitoral'].value_counts()

agrupamentoCitacoesNomeEleitoral.rename_axis().reset_index(name='counts')

#Quantas interações por partido?
agrupamentoPartidoInteracoes = dataset.groupby('partido')[u'interactions'].value_counts()

agrupamentoPartidoInteracoes = agrupamentoPartidoInteracoes.rename_axis().reset_index(name='counts')

totalInteracoes = agrupamentoPartidoInteracoes[["interactions", "counts"]].product(axis=1)

totalInteracoes = totalInteracoes.rename_axis().reset_index(name='counts')

totalInteracoes

#agrupamentoPartidoInteracoes.head(5)

#Gerando um Dataframe com os partidos e a contagem de interações
new = pd.DataFrame([agrupamentoPartidoInteracoes.partido, totalInteracoes.counts]).transpose()

#Gera um dicionário com todas as interações que um partido recebeu
dicionario_interacoes = {k: g["counts"].tolist() for k,g in new.groupby("partido")}

dicionario_interacoes.keys()

#Capturando a soma das interações por partido e adicionando numa estrutura de dados de dicionario
dict_totalInteracoesPorPartido = {}
for key in dicionario_interacoes:
  dict_totalInteracoesPorPartido[key] = sum(dicionario_interacoes.get(key))

len(dict_totalInteracoesPorPartido)

#Transformando o dicionario em Dataframe
dt_fromdict = pd.DataFrame.from_dict(dict_totalInteracoesPorPartido, orient='index').reset_index()

dt_fromdict.columns = ['partido', 'totalInteracoes']

dt_fromdict = dt_fromdict.sort_values(by=['totalInteracoes'])

dezMaisInfluentes = dt_fromdict.iloc[17:27]

#Plotando grafico com os partidos e as interações totais em cada um
partidos = list(dezMaisInfluentes['partido']) 
totalInteracoesPartidos = list(dezMaisInfluentes['totalInteracoes']) 

fig = plt.figure(figsize = (5, 4)) 

plt.barh(partidos, totalInteracoesPartidos, color ='black')
#plt.scatter(partidos, totalInteracoesPartidos, label = 'Pontos', color = 'b', marker = '', s = 100)

#plt.xticks([0, 10000, 20000, 30000])

plt.xlabel("Quantidade de interações") 
plt.ylabel("Partidos") 
#plt.title("Interações por partido") 

plt.show()

# define o nível de separabilidade entre as partes, ordem do vetor representa as partes
#explode = (0.1, 0, 0, 0) 

# define o formato de visualização com saída em 1.1%%, sombras e a separação entre as partes
plt.pie(totalInteracoesPartidos, labels = partidos, autopct='%1.1f%%', shadow=True)#, explode=explode)

# inseri a legenda e a localização da legenda.
plt.legend(partidos, loc=3)


# define que o gráfico será plotado em circulo
plt.axis('equal')

plt.show()



#Quantas interações por partido?

agrupamentoParlamentarInteracoes = dataset.groupby('nome_eleitoral')[u'interactions'].value_counts() 

agrupamentoParlamentarInteracoes = agrupamentoParlamentarInteracoes.rename_axis().reset_index(name='counts')

totalInteracoesParlamentar = agrupamentoParlamentarInteracoes[["interactions", "counts"]].product(axis=1)

totalInteracoesParlamentar = totalInteracoesParlamentar.rename_axis().reset_index(name='counts')

totalInteracoesParlamentar

#Gerando um Dataframe com os partidos e a contagem de interações
new = pd.DataFrame([agrupamentoParlamentarInteracoes.nome_eleitoral, totalInteracoes.counts]).transpose()

dicionario_interacoes_parlamentar = {k: g["counts"].tolist() for k,g in new.groupby("nome_eleitoral")}

dict_totalInteracoesPorParlamentar = {}
for key in dicionario_interacoes_parlamentar:
  dict_totalInteracoesPorParlamentar[key] = sum(dicionario_interacoes_parlamentar.get(key))

dt_fromdict_parlamentar = pd.DataFrame.from_dict(dict_totalInteracoesPorParlamentar, orient='index').reset_index()

dt_fromdict_parlamentar.columns = ['nome_eleitoral', 'totalInteracoes']

dt_fromdict_parlamentar = dt_fromdict_parlamentar.sort_values(by=['totalInteracoes'])

dezMaisInfluentesParlamentares = dt_fromdict_parlamentar.iloc[17:27]

#Plotando grafico com os partidos e as interações totais em cada um
parlamentares = list(dezMaisInfluentesParlamentares['nome_eleitoral']) 
totalInteracoesPorParlamentar = list(dezMaisInfluentesParlamentares['totalInteracoes']) 

fig = plt.figure(figsize = (4, 3)) 

plt.barh(parlamentares, totalInteracoesPorParlamentar, color ='black')

plt.xlabel("Quantidade de interações") 
plt.ylabel("Nome do parlamentar") 

plt.show()

#Quantas interações por partido?
agrupamentoParlamentarInteracoes = dataset.groupby('nome_eleitoral')['interactions'].agg('sum').reset_index()

name_frequenc = dataset.groupby('nome_eleitoral')[u'citadas'].count().reset_index()

agrupamentoInfluenciaParlamentar = agrupamentoParlamentarInteracoes[['nome_eleitoral', 'interactions']].copy()

agrupamentoInfluenciaParlamentar['postagens'] = name_frequenc[['citadas']].copy()

agrupamentoInfluenciaParlamentar = agrupamentoInfluenciaParlamentar.sort_values('postagens', ascending=False)

agrupamentoInfluenciaParlamentar

plt.figure(figsize=(8,8))
plt.ylabel("Interações") 
plt.xlabel("Quantidade de tweets")
plt.legend(agrupamentoInfluenciaParlamentar.nome_eleitoral, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
pl = sns.scatterplot(data=agrupamentoInfluenciaParlamentar[:10], x="postagens", y="interactions", hue="nome_eleitoral", legend='full', edgecolors='b')

x = agrupamentoInfluenciaParlamentar[:10]['postagens']
y = agrupamentoInfluenciaParlamentar[:10]['interactions']
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(x, y, alpha=0.70, c= df[category], cmap=cm.brg)
ax.set_xlabel('Postagens')
ax.set_ylabel('Interações')