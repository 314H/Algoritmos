"""Laura Castro / InsertionSort"""

from time import time # para calcular o tempo gasto
from os import system # para executar comandos no terminal
from random import randrange # para gerar numeros aleatorios (criar vetor)


dir = "C:/Usuario/Desktop/arquivos/" # diretorio onde esta a pasta para salvar os arquivos usados no gnuplot


# funcao para criar um vetor com "n" elementos
def criarVetor(n):
    vetor = []
    for j in range(0,n):
        vetor.append(randrange(0,100))

    return vetor


# funcao para ordenar vetor de forma crescente usando algoritmo InsertionSort
def insertionSortCre(v):
    for i in range( 1, len( v ) ):
        chave = v[i]
        k = i
        while k > 0 and chave < v[k - 1]:
            v[k] = v[k - 1]
            k -= 1
        v[k] = chave
    return v


# funcao para ordenar vetor de forma decrescente usando algoritmo InsertionSort
def insertionSortDec(v):
    for i in range( 1, len( v ) ):
        chave = v[i]
        k = i
        while k > 0 and chave > v[k - 1]:
            v[k] = v[k - 1]
            k -= 1
        v[k] = chave
    return v


# metodo principal para executar ordenacoes e calcular tempo de execucao
def programa(n):
    vetor = criarVetor(n)
    startC = time()
    crescente = insertionSortCre(vetor)
    cresTime = time() - startC

    startD = time()
    decrescente = insertionSortDec(vetor)
    decresTime = time() - startD
    print("Tempo Crescente = {} \nTempo Descrescente = {}".format(cresTime, decresTime))
    return cresTime, decresTime


# funcao para criar os arquivos com dados para gerar o grafico no gnuplot
def criarGnufiles(n):
    cres, dec = programa(n)

    arquivo = open(dir+'entrada1.dat', 'w+')
    arquivo.write('#Tempo\n' + str(cres) + '\n' + str(dec))
    arquivo.close()

    gnuplot = open(dir+'grafico.gnu', 'w+')
    gnuplot.write('set title "Crescente vs Decrescente"\n')
    gnuplot.write('set autoscale \nset xlabel "0- Crescente  |  1- Decrescente" \nset ylabel "Tempo de execucao"\n')
    gnuplot.write('set grid\nplot \\\n    ')
    gnuplot.write('"'+dir+'entrada1.dat" title "Crescente -> Descrescente  " w linespoints, ')
    gnuplot.write('\npause -1 "Pressione enter para sair e terminar as aplicacoes..."')
    gnuplot.close()


# funcao para executar comando gnuplot no terminal
def gnuplot(n):
    criarGnufiles(n)
    system("gnuplot " + dir + "grafico.gnu")


gnuplot(500) # cria vetor de tamanho 500
