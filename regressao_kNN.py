# -*- coding: utf-8 -*-
"""
@author: Laura
"""
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

base_dados = pd.read_csv('bd_tarefa4.CSV')
estatisticas = base_dados.describe()

previsores = base_dados.iloc[:,0:5].values
saida = base_dados.iloc[:,5].values

scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

x = 0.25

(prev_treino, prev_teste, saida_treino, saida_teste) = train_test_split(
        previsores, saida, test_size=x, random_state=0)

"""
Grafico - Evolucao do erro
"""

erro = []
for i in range(1, len(prev_treino)):
    regressao = KNeighborsRegressor(n_neighbors=i)
    regressao.fit(prev_treino, saida_treino)
    regressaoFinal = regressao.predict(prev_teste)
    
    erro.append(mean_absolute_error(saida_teste, regressaoFinal))


print('Menor erro e {} e ocorre com {} vizinhos'.format(
    round(min(erro), 3), erro.index( min(erro) ) ))
print('Maior erro e {} e ocorre com {} vizinhos'.format(
    round(max(erro), 3), erro.index( max(erro) ) ))


# erro[50]
# ideal_x = range(25,200)
# plt.plot(ideal_x, erro[25:200])
# plt.show()


plt.plot(erro)
plt.title("Grafico de Erros para Diferentes valores de Vizinhos")
plt.annotate('Considerando Test_Size de {}'.format(x), xy=(5, 2))
plt.xlabel("Numero de Vizinhos")
plt.ylabel("Erro")
plt.show()

"""
CONSIDERACOES:
Inicialmente, na propria base de dados acrescentou-se uma linha com os titulos das colunas.

O grafico gerado refere-se a valores de erro, para valores de vizinhos (n_neighbors) diferentes,
para comparacao e otimizacao de valores.
Tambem foram simulados diferentes “test_sizes” (entre 10% e 75%) porem os resultados se mostraram
extremamente semelhantes.
Percebe-se que, quanto mais vizinhos, maior o numero de erros (como esperado), porem pode-se
considerar um ponto ideal na regiao entre 0 e 100 vizinhos (proximo a um “pico”).

Define-se este ponto pois e o que apresenta menos erros, considerando um número razoavel de
vizinhos (aproximado em 50 com erro de 3.32873). Sabendo que o maior erro registrado eh de 5.515 
e que o menor erro e 1.645, pode-se definir uma boa aproximacao, ja que a media entre estes valores
eh de 3,58 (o erro definido e menor).
"""