/*
A atividade envolve a construcao de um algoritmo de ordenacao que permita classificar 
elementos gerados de forma aleatoria em um vetor com 50.000 posicoes. Ao final o algoritmo deve apresentar o 
tempo de execucao para classificacao, em ordem crescente, dos elementos gerados de forma aleatoria. 
Tambem, repetir o algoritmo implementado para apresentar o tempo de execucao para o mesmo tipo de classificacao 
com o  vetor ja ordenado.

Laura Castro
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

FILE *gnuplot;


// Metodo para ordenacao de um vetor de tamanho N
void insertionSort(int vetor[], int N)
{
    int i, chave, j;
    for(i=1; i < N; i++){
        chave = vetor[i];
        j = i-1;

        while(j >= 0 && vetor[j] > chave){
            vetor[j+1] = vetor[j];
            j = j - 1;
        }
        vetor[j + 1] = chave;
    }
}


// Metodo para preenhcher um vetor de tamanho N
void fillVetor(int vetor[], int N)
{
    int i;
    for (i = 0; i < N; i++)
    {
        vetor[i] = rand() % 100;
    }
}


// Metodo para preencher vetor, ordenar e calcular tempos
void principal(int N){
    float tempoTotalNord, tempoTotalOrd;
    int temp;
    int vet1[N];

    clock_t tempoInicialNord;
    srand(time(NULL));

    fillVetor(vet1, N);

    /*---------- Nao ordenado -----------*/
    gnuplot = fopen("C:/gnuplot/tarefa02/ordenado.dat", "w");
    printf("\nTipo \t Tempo de Exec.\n");
    printf("Nao ordenado\t\t");
    fprintf(gnuplot, "#Nao Ordenado - Tempo\n");
    /*-- Calculo --*/
    tempoInicialNord = clock();
    insertionSort(vet1, N);
    tempoTotalNord = clock() - tempoInicialNord;
    /*------*/
    fprintf(gnuplot, " %f \n", tempoTotalNord);
    printf(" %f \n", tempoTotalNord);
    fclose(gnuplot);


    clock_t tempoInicialOrd;
    srand(time(NULL));

    /*---------- Ordenado -----------*/
    gnuplot = fopen("C:/gnuplot/tarefa02/naordenado.dat", "w");
    printf("Ordenado\t\t");
    fprintf(gnuplot, "#Ordenado - Tempo\n");
    /*-- Calculo --*/
    tempoInicialOrd = clock();
    // pega o mesmo vetor, ordenado anteriormente e ordena de novo
    insertionSort(vet1, N);
    tempoTotalOrd = clock() - tempoInicialOrd;
    /*------*/
    fprintf(gnuplot, " %f \n", tempoTotalOrd);
    printf(" %f \n", tempoTotalOrd);
    fclose(gnuplot);
}


int main()
{
    system("cls");

    principal(50000);

    system("gnuplot c:/gnuplot/tarefa02/grafico.gnu");

    return 0;
}
