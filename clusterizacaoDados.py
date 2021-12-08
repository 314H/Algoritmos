# -*- coding: utf-8 -*-
"""
@author: Laura
"""

import numpy as np 
import pandas as pd #LIDAR COM DADOS
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

#ler o arquivo, e considerar as separacoes por virgula
base_dados = pd.read_csv('bd_tarefa1.CSV', sep=';')
estatisticas = base_dados.describe()

"""PRE PROCESSAMENTO"""
#mudar os titulos das colunas (de acordo com o que ele nomeou na tarefa)
base_dados.columns = ['CT', 'CU', 'LT', 'TC', 'TS']

#e necessario ser vetor para conseguir clusterizar
#file.drop para retirar a coluna TS // axis=1 indica coluna, e axis=0
#indica linha
vetor = np.array(base_dados.drop(['TS'], axis=1))

#converter dados textuais em numericos
#para interpretacao do programa
vetor[:, 0] = LabelEncoder().fit_transform(vetor[:,0])
vetor[:, 1] = LabelEncoder().fit_transform(vetor[:,1])
vetor[:, 2] = LabelEncoder().fit_transform(vetor[:,2])
vetor[:, 3] = LabelEncoder().fit_transform(vetor[:,3])


"""CLUSTERIZANDO"""
clusterizar = KMeans(n_clusters=4, random_state=0)
#variavel que vai guardar a clusterizacao
#n_clusters = define o numero de "clusters" (grupos) - como sao 4 colunas...
#random_state = numero de vezes que se inicia os clusters aleatoriamente

clusterizar.fit(vetor)  #coloco algoritimo para trabalhar/analisar os dados - 
#achar os padroes

base_dados["Clusters"] = clusterizar.labels_
#nome_clusterizacoes  #cria nova coluna no arquivo com
#os valores da clusterizacao


"""Graficos de Dispersao"""
plt.figure( figsize=(18, 8))
plt.scatter(base_dados["TC"], base_dados["Clusters"], color='red', label="TC")
plt.scatter(base_dados["CT"], base_dados["Clusters"], color='blue', label="CT")
plt.scatter(base_dados["CU"], base_dados["Clusters"], color='purple', label="CU")
plt.scatter(base_dados["LT"], base_dados["Clusters"], color='orange', label="LT")
plt.title("Colunas x Clusters")
plt.legend()
plt.show()

"""Numero de elementos em cada cluster"""
base_dados["Clusters"].plot(kind="hist", title="Elementos de cada cluster")


"""
CONSIDERACOES:
Primeiramente foi feita uma analise superficial dos dados a partir da variavel “estatistica” e a partir disso foi possivel ver que os dados nao estavam de extrema discrepancia, entao nao houve necessidade de normalizar os dados (as faixas dos dados estavam proximas).

O primeiro grafico gerado coloca os clusters criados (eixo Y), em relacao as colunas da base de dados. Isso foi feito para que fosse possivel ver como esta a distribuicao em relacao as classes. O segundo grafico e apenas uma representacao do número de amostras em cada cluster.

Para melhor compreensao, e possivel ver que, em relacao a coluna “TC” (que continha os dados sport, EComm e holid) a divisao criada pelos clusters esta englobando duas classes em cada cluster. Exemplificando: a categoria “sport” esta dentro do cluster 1.0 e 0; a categoria game esta dentro do cluster 1.0 e 2.0;

Assim, conclui-se que a clusterizacao resultante foi aceitavel, mas poderia ter sido melhor, havendo mais amostras
"""