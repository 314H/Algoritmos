# -*- coding: utf-8 -*-
"""
@author: Laura
"""
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix

base_dados = pd.read_csv('bd_tarefa5.csv', sep=';') # dataset
estatistica = base_dados.describe() # apenas de colunas numericas

# Separacao das variaveis Previsoras e a Classe
previsores = base_dados.iloc[:, 0:16].values
classe = base_dados.iloc[:, 16].values

# NORMALIZACAO DA BASE DE DADOS 
# converter dados textuais em numericos para interpretacao do programa
le = LabelEncoder()
for i in range(0, 16):
    previsores[:, i] = le.fit_transform(previsores[:, i])

# colocar as bases numericas em unidades proximas
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

# DIVISAO DA BASE EM CONJUNTOS DE TREINAMENTO E TESTE
previsores_treino, previsores_teste, classe_treino, classe_teste = train_test_split(
    previsores, classe, test_size=0.20, random_state=0)

# BIBLIOTECA DE REDE NEURAL PARA CLASSIFICAcaO - nn e arquitetura da rede desejada
"""
FOR para verificar eficiencia com diferentes funcoes e diferentes valores 
para camada intermediaria
Valores camada intermediaria indo de 10 a 1000, em passos de 20
"""

funcoes = ['logistic', 'tanh', 'identity', 'relu'] # vetor com as funcoes possiveis
eficiencia_funcoes = []
eficiencia_camadas = []
eficiencia_total = [[]]
camadas = [20,110,200,260,320,360,400,460,500]
"""
hidden_layer_size = tamanho da camada intermediaria
activation = funcao de ativacao (logistic, tanh, identity, relu)
max_iter = numero de iteracoes (problemas simples costumam nem precisar de 1000)
tol = tolerancia permitida
"""
for j in range(len(funcoes)):
    print('j = ',funcoes[j])
    eficiencia_camadas.clear()
    for k in range(len(camadas)):
        print(camadas[k])
        nn = MLPClassifier(hidden_layer_sizes=(camadas[k],),  
                           activation=funcoes[j], max_iter=1000, tol=0.001)
        
        treino = (nn.fit(previsores_treino, classe_treino))        
        teste = nn.predict(previsores_teste)
        # MATRIZ DE CONFUSaO
        matriz = confusion_matrix(classe_teste, teste)
        
        # vetor com as eficiencias para variacao do num de camadas
        acerto = (matriz[0,0]+matriz[1,1])/len(classe_teste)*100
        eficiencia_camadas.append(acerto)
        
    eficiencia_funcoes.insert(j, eficiencia_camadas)
    eficiencia_total.append(list(eficiencia_funcoes[0]))

del(eficiencia_total[0]) # apagar colchetes iniciais

max(eficiencia_total[1])
camadas[eficiencia_total[1].index(max(eficiencia_total[1]))]

plt.plot(eficiencia_total[0], label="Logistic")
plt.plot(eficiencia_total[1], label="Tanh")
plt.plot(eficiencia_total[2], label="Identity")
plt.plot(eficiencia_total[3], label="Relu")
plt.title('Eficiencia com camadas intermediaria variando de 4 a 225')
plt.legend(loc='lower right')
plt.show()

"""
CONSIDERACOES:
Selecionou-se trabalhar com Rede Neural de Classificacao pois o objetivo e definir a categoria dos valores da base de dados (e comparar com a coluna ‘y’, as classificacoes originais).
A matriz de confusao foi utilizada para calcular a eficiencia da rede, somando os acertos de 1 aos acertos de 0, e dividindo pelo tamanho da amostra (multiplicando por 100 para obter os valores em porcentagem).
( matriz[0,0] + matriz[1,1] ) * 100 / len(classe_teste)
Foram feitos testes para diferentes tamanhos e valores de camada intermediaria, e para cada uma das funcoes disponiveis (logistic, tanh, identity, relu).

Teste 01:
Os valores de camadas intermediarias usados inicialmente foram: 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196 e 225.
A maior eficiencia registrada foi de (aproximadamente) 89.7932%, e ocorre com a funcao de ativacao Relu, utilizando 81 camadas intermediarias.

Teste 02:
Executando o mesmo codigo, porem com menos camadas (1, 2, 4, 6, 8, 10, 12, 14, 16, 18 e 20), o grafico obtido e apresentado abaixo. 
Neste caso a melhor eficiencia foi de 89.7047%, ocorrendo com 10 camadas intermediarias, na funcao de ativacao Tangente Hiperbolica.

Teste 03:
Por fim testou-se as camadas com valores 20, 110, 200, 260, 320, 360, 400, 460 e 500. O grafico gerado esta registrado abaixo.

Conclusoes:
Destaca-se que, a rede Relu foi a que tomou menos tempo de processamento, com em media 2 minutos (o tempo foi verificado pelo terminal do Spyder, visualmente), em todas as situacoes testadas.
No geral, para esta base de dados as melhores funcoes para utilizar sao a Relu ou a Tangente Hiperbolica. Para a maquina utilizada, o Relu se mostrou melhor por ter a maior eficiencia e o menor tempo de processamento.
"""