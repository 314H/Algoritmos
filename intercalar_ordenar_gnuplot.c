/*
Disciplina: Analise e Complexidade de Algoritmo

Criar um algoritmo desenvolvido em uma linguagem da sua escolha para realizar a intercalação de dois 
vetores, conforme explicado na aula do dia 20/08. E importante que os dois vetores estejam ordenados
previamente. Ao final da execucao, apresente um grafico do tempo de execucao do algoritmo usando a 
ferramenta GNUPlot. Havera um sorteio para duas apresentacoes sobre o desenvolvimento deste exercicio

Laura Castro
*/


#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

FILE *gnuplot;

// Metodo para realizar a troca nos algoritmos de ordenacao
void trocar(int vetor[], int i, int j)
{
  int aux;
  aux = vetor[j];
  vetor[j] = vetor[i];
  vetor[i] = aux;
}


// Metodo de ordenacao com algoritmo Bubble Sort
void ordenarBubble(int vetor[], int N)
{
  int i, j;
  for (i = 0; i < N; i++)
  {
    for (j = i; j < N; j++)
    {
      if (vetor[j] < vetor[i])
      {
        trocar(vetor, i, j);
      }
    }
  }
}


// Metodo de ordenacao com algoritmo Select Sort
void ordenarSelect(int vetor[], int N)
{
  int posMin;
  for (int i = 0; i < N - 1; i++)
  {
    posMin = i;
    for (int j = i + 1; j < N; j++)
    {
      if (vetor[posMin] > vetor[j])
      {
        posMin = j;
      }
      if (i != posMin)
      {
        trocar(vetor, i, posMin);
      }
    }
  }
}


// Metodo para intercalar dois vetores de tamanho N em um terceiro vetor
void intercalar(int vet1[], int vet2[], int vet3[], int N)
{
  int j = 0, k = 0;
  for (int i = 0; i < 2 * N; i += 2)
  {
    vet3[i] = vet1[j];
    vet3[i + 1] = vet2[k];
    j++;
    k++;
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


// Metodo que executa o a intercalacao e ordenacao com Bubble Sort
void programaBubble(int N)
{
  float tempoExecucao;
  int temp;

  int vet1[N];
  int vet2[N];
  int vet3[2 * N];

  printf("%d\t\t", N);
  fprintf(gnuplot, "%d\t\t", N);

  clock_t tempoInicial;
  srand(time(NULL));

  /*-------------------*/
  tempoInicial = clock();

  fillVetor(vet1, N);
  fillVetor(vet2, N);

  ordenarBubble(vet1, N);
  ordenarBubble(vet2, N);
  intercalar(vet1, vet2, vet3, N);

  tempoExecucao = clock() - tempoInicial;
  /*-------------------*/
  fprintf(gnuplot, " %f \n", tempoExecucao);
  printf(" %f \n", tempoExecucao);
}


// Metodo que executa intercalacao e ordenacao com SelectSort
void programaSelect(int N)
{
  float tempoExecucao;
  int temp;

  int vet1[N];
  int vet2[N];
  int vet3[2 * N];

  printf("%d\t\t", N);
  fprintf(gnuplot, "%d\t\t", N);

  clock_t tempoInicial;
  srand(time(NULL));

  /*-------------------*/
  tempoInicial = clock();

  fillVetor(vet1, N);
  fillVetor(vet2, N);

  ordenarSelect(vet1, N);
  ordenarSelect(vet2, N);
  intercalar(vet1, vet2, vet3, N);

  tempoExecucao = clock() - tempoInicial;
  /*-------------------*/
  fprintf(gnuplot, " %f \n", tempoExecucao);
  printf(" %f \n", tempoExecucao);
}


int main()
{
  system("cls");

  gnuplot = fopen("C:/gnuplot/tarefa01/saida1.dat", "w");
  printf("\nVetores Bubble\nTamanho \t Tempo de Exec.\n");
  fprintf(gnuplot, "#Ordena Bubble \n#Tamanho \t Tempo\n");
  programaBubble(400);
  programaBubble(1000);
  programaBubble(2800);
  programaBubble(4000);
  programaBubble(5000);
  fclose(gnuplot);

  gnuplot = fopen("C:/gnuplot/tarefa01/saida2.dat", "w");
  printf("\nVetores Select\nTamanho \t Tempo de Exec.\n");
  fprintf(gnuplot, "#Ordena Select \n#Tamanho \t Tempo\n");
  programaSelect(400);
  programaSelect(1000);
  programaSelect(2800);
  programaSelect(4000);
  programaSelect(5000);
  fclose(gnuplot);

  system("gnuplot c:/gnuplot/tarefa01/grafico01.gnu");

  return 0;
}
