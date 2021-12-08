"""Laura Castro """

from time import time # para calcular o tempo gasto
from os import system # para executar comandos no terminal
from random import randrange # para gerar numeros aleatorios (criar vetor)


dir = "C:/Usuario/Desktop/arquivos/" # diretorio onde esta a pasta para salvar os arquivos usados no gnuplot


# funcao para criar um vetor com "n" elementos
# <param> n = numero de elementos no vetor
def criarVetor(n):
    vetor = []
    for j in range(0,n):
        vetor.append(randrange(0,100))

    return vetor


# funcao para ordenar vetor de forma decrescente usando algoritmo InsertionSort
# <param> v = vetor a ser ordenado
# <param> inicio = posicao inicial do vetor
# <param> fim = posicao final do vetor
def QuickSort(v, inicio, fim=None): # fim = len(vetor) - 1 (um indice sera o pivo)
    if fim == None: fim = len(v) - 1
    # Escolhe um elemento pivo na lista, e passa todos os elementos do vetor que sao
    # maiores que o pivo para sua direita (a esquerda ficam os elementos menores que ele)
    if inicio < fim:
        pivo = v[fim]
        i = inicio # indice que acompanha elementos MENORES que o pivo
        for j in range(inicio, fim):  # indice que acompanha elementos analisados - maiores que o pivo
            if v[j] <= pivo: # se o elemento for menor ou igual ao pivo, faz a troca entre ele e o elemento de indice menor
                v[j], v[i] = v[i], v[j]
                i+=1 # apos a troca, incrementa indice do menor
        v[i], v[fim] = v[fim], v[i]
        pivo = i
        QuickSort(v, inicio, pivo-1) # aplica algoritmo na lista da esquerda (menores que o pivo)
        QuickSort(v, pivo+1, fim) # aplica algoritmo na lista da direita (maiores que o pivo)


# funcao para ordenar vetor de forma crescente usando algoritmo InsertionSort
# <param> v = vetor a ser ordenado
def InsertionSortCre(v):
    for i in range( 1, len( v ) ):
        chave = v[i]
        k = i
        while k > 0 and chave < v[k - 1]:
            v[k] = v[k - 1]
            k -= 1
        v[k] = chave
    return v


# funcao para ordenar vetor de forma decrescente usando algoritmo InsertionSort
# <param> v = vetor a ser ordenado
def InsertionSortDec(v):
    for i in range( 1, len( v ) ):
        chave = v[i]
        k = i
        while k > 0 and chave > v[k - 1]:
            v[k] = v[k - 1]
            k -= 1
        v[k] = chave
    return v


# funcao para ordenar vetor usando algoritmo MergeSort
# <param> v = vetor a ser ordenado
# <param> inicio = posicao inicial do vetor
# <param> fim = posicao final do vetor
def MergeSort(v, inicio, fim):
    if (fim-inicio) > 1:  # verifica se o tamanho da lista e maior que 1
        meio = (fim+inicio)//2  # encontra o meio da lista passada
        MergeSort(v, inicio, meio)
        MergeSort(v, meio, fim)
        # unir as duas listas criadas:
        esquerda = v[inicio:meio]  # lista da esquerda para comparacao
        direita = v[meio:fim]  # lista da direita para comparacao
        primeiroDireita, primeiroEquerda = 0, 0
        for i in range(inicio, fim):
            if primeiroEquerda >= len(esquerda):
                # substitui o primeiro elemento do vetor original pelo primeiro elemento da lista da direita
                v[i] = direita[primeiroDireita]
                # passa para proximo elemento da lista da direita - se torna o primeiro
                primeiroDireita += 1
            elif primeiroDireita >= len(direita):
                # substitui o primeiro elemento do vetor original pelo primeiro elemento da lista da esquerda
                v[i] = esquerda[primeiroEquerda]
                # passa para proximo elemento da lista da esquerda - se torna o primeiro
                primeiroEquerda += 1

            # comparacao dos primeiros elementos de cada lista
            elif esquerda[primeiroEquerda] < direita[primeiroDireita]:
                # substitui o primeiro elemento do vetor original pelo primeiro elemento da lista da esquerda
                v[i] = esquerda[primeiroEquerda]
                # passa para proximo elemento da lista da esquerda - se torna o primeiro
                primeiroEquerda += 1
            else:
                # substitui o primeiro elemento do vetor original pelo primeiro elemento da lista da direita
                v[i] = direita[primeiroDireita]
                # passa para proximo elemento da lista da direita - se torna o primeiro
                primeiroDireita += 1


# metodo principal para executar ordenacoes e calcular tempo de execucao
# <param> n = numero de elementos no vetor
def programa(n):
    # vetor = criarVetor(n)
    v1 = v2 = v3 = v4 = v5 = v6 = criarVetor(n)

    startIC = time()
    InsertionSortCre(v1)
    cresITime = time() - startIC
    # print("InsertionSort Cre",v1)

    startID = time()
    InsertionSortDec(v2)
    decresITime = time() - startID
    # print("InsertionSort Dec",v2)
    print("\nInsertion\nTempo Crescente = {} \nTempo Descrescente = {}".format(cresITime, decresITime))
    print("Diferenca entre crescente - decrescente: ", cresITime - decresITime)

    startMC = time()
    MergeSort(v3, 0, len(v3))
    cresMTime = time() - startMC
    # print("\nMergeSort Cre",v3)

    startMD = time()
    MergeSort(v4, 0, len(v4))
    v4.reverse()
    decresMTime = time() - startMD
    # print("MergeSort Dec",v4)
    print("\nMerge\nTempo Crescente = {} \nTempo Descrescente = {}".format(cresMTime, decresMTime))
    print("Diferenca entre crescente - decrescente: ", cresMTime - decresMTime)

    startQC = time()
    QuickSort(v5, 0)
    cresQTime = time() - startQC
    # print("\nQuick Cre",v5)

    startQD = time()
    QuickSort(v6, 0)
    v6.reverse()
    decresQTime = time() - startQD
    # print("QuickSort Dec",v6)
    print("\nQuick\nTempo Crescente = {} \nTempo Descrescente = {}".format(cresQTime, decresQTime))
    print("Diferenca entre crescente - decrescente: ", cresQTime - decresQTime, "\n")
    return cresITime, decresITime, cresMTime, decresMTime, cresQTime, decresQTime


# funcao para criar os arquivos com dados para gerar o grafico no gnuplot
# <param> n = numero de elementos no vetor
def criarGnufiles(n):
    cresITime, decresITime, cresMTime, decresMTime, cresQTime, decresQTime = programa(n)

    arquivo = open(dir+'insertion.dat', 'w')
    arquivo.write('#Tempo\n' + str(cresITime) + '\n' + str(decresITime))
    arquivo.close()
    arquivo = open(dir+'merge.dat', 'w')
    arquivo.write('#Tempo\n' + str(cresMTime) + '\n' + str(decresMTime))
    arquivo.close()
    arquivo = open(dir+'quick.dat', 'w')
    arquivo.write('#Tempo\n' + str(cresQTime) + '\n' + str(decresQTime))
    arquivo.close()

    xlabel = '"0 = Crescente  -->  1 = Descrescente"'

    gnuplot = open(dir+'grafico.gnu', 'w')
    gnuplot.write('set title "Crescente vs Decrescente"\nset autoscale \nset xlabel {} \nset ylabel "Tempo de execucao"\nset grid\nplot \\\n    '.format(xlabel))
    gnuplot.write('"'+dir+'insertion.dat" title "InsertionSort" w linespoints, ')
    gnuplot.write('"'+dir+'merge.dat" title "MergeSort" w linespoints, ')
    gnuplot.write('"'+dir+'quick.dat" title "QuickSort" w linespoints, ')
    gnuplot.write('\npause -1 "Pressione enter para sair e terminar as aplicacoes..."')
    gnuplot.close()


# funcao para executar comando gnuplot no terminal
# <param> n = numero de elementos no vetor
def gnuplot(n):
    criarGnufiles(n)
    system("gnuplot " + dir + "grafico.gnu")


gnuplot(500) # cria vetor de tamanho 500
