"""Laura Castro - MergeSort"""

def MergeSort(v, inicio, fim):
    if (fim-inicio) > 1:  # verifica se o tamanho da lista e maior que 1
        meio = (fim+inicio)//2  # encontra o meio da lista passada
        # aplica o mergeSort a lista da esquerda - do inicio ao meio
        MergeSort(v, inicio, meio)
        # aplica o mergeSort a lista da direita - do meio ao fim
        MergeSort(v, meio, fim)

        # unir as duas listas criadas:
        esquerda = v[inicio:meio]  # lista da esquerda para comparacao
        direita = v[meio:fim]  # lista da direita para comparacao
        # indices dos primeiros elementos de cada lista
        primeiroDireita, primeiroEquerda = 0, 0
        for i in range(inicio, fim):
            # analisar primeiro os inicios das listas
            # verifica se o indice esta dentro da lista
            if primeiroEquerda >= len(esquerda):
                # substitui o primeiro elemento do vetor original pelo primeiro elemento da lista da direita
                v[i] = direita[primeiroDireita]
                # passa para proximo elemento da lista da direita - se torna o primeiro
                primeiroDireita += 1

            # verifica se o indice esta dentro da lista
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


vetor = [5, 98, 72, 45, 1, 25, 8, 32, 24, 16, 87]
print(vetor)
MergeSort(vetor, 0, len(vetor))
print(vetor)
