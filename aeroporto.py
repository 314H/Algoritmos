# PROBLEMA
""" Trafego Aereo
Considere um aeroporto que tem somente uma pista de pouso e decolagem
- aeronaves estacionadas no patio do aeroporto;
- aeronaves taxiando (de chegada ou saida) no aeroporto;
- aeronaves precisando aterrissar (descer);
- aeronaves precisando decolar (subir), ou seja, que estao prontas para subir, preparadas na cabeceira da pista, aguardando a ordem da torre de controle para o procedimento de decolagem;
Para controlar o movimento deste aeroporto, existe uma torre de controle, que “escalona”, segundo prioridades pre-estabelecidas, o trafego de aeronaves;
Mais precisamente, aquelas que estao em procedimento de aterrissagem e aquelas que estao em procedimento para decolar deverao ter prioridades definidas como:
O procedimento de aterrisagem (A) tem prioridade maior que o procedimento de decolagem (D);
Num dado tempo, somente uma aeronave pode estar ocupando a pista para aterrissar ou para decolar;
Você pode escolher o valor das prioridades como for mais conveniente.

A pista de aterrissagem ou decolagem e a regiao critica para cada thread (aeronave).
"""

import time
from random import randrange
from threading import Thread, Lock, Event


# EXPLICACAO DO CODIGO
""" A Thread eh a Torre
A pista eh o lock
Aeroporto inicia vazio (avioes "entram" de 1 em 1)
Todo aviao tem uma prioridade associada - 0 ou 1
0 - mais prioritario (Aterrisagem)
1 - menos prioritario (Decolagem)
########## Acoes
EVENT = Chegada de aeronaves
Quando nao tem aeronave na fila, torre aguarda gatilho do evento
Quando aeronave aparece no radar da gatilho no evento
Apos finalizar aterrisagem/decolagem, o evento eh limpo (resetado)
> Taxiar ainda eh usando a pista
Aviao ATERRISA -> TAXIA -> ESTACIONA
Aviao estah ESTACIONADO -> TAXIA -> DECOLA
"""


mutex = Lock() # variavel para prender uma thread ate que outra finalize (uso da pista / tem aeronave esperando)

class Aeroporto:
    temAeronaveEvento = Event() # gatilho para acoes

    def __init__(self):
        self.aeronavesEsperando = [] # vetor com os aeronavess na patio
        self.ordemFinal = []

    # inicia o trabalho/acoes do torre
    def abrirAeroporto(self):
        print("### Aeroporto esta abrindo ### \n(inicia a thread da pista)")
        print("Prioridade 0 - Maxima (Aterrisagem)\nPrioridade 1 - Minima (Decolagem)")
        Thread(target=self.Torre).start()  # inicia thread para uso da pista


    def Torre(self):
        while True:
            if len(self.aeronavesEsperando) > 0:  # se tiver aeronaves esperando
                mutex.acquire() # tenta pegar o Lock, caso esteja livre (se nao estiver, espera estar)
                # apenas com o lock o codigo abaixo e executado                
                self.aeronavesEsperando = sorted(self.aeronavesEsperando,  key = lambda x: x[1]) # ordena aeronaves em espera por prioridade
                self.ordemFinal.append(self.aeronavesEsperando[0]) # cria vetor com a ordem final
                print("Espera: ", self.aeronavesEsperando, '\n') # imprimi a lista de aeronaves esperando (em ordem de prioridade)
                print("Aeronaves com prioridade 1 estao Estacionadas")

                if self.aeronavesEsperando[0][1] == 0: # prioridade = 0 (aterrisando)
                    aviao = self.aeronavesEsperando[0] # guarda numero da aeronave para prints
                    print("Aeronave {0} aterrisando (alta prioridade)!".format(aviao))
                    mutex.release() # finaliza uso da Torre
                    self.aeronavesEsperando.remove(aviao) # apaga aeronaves cortando cabelo da espera
                    time.sleep(randrange(5,9)) # tempo para Aterrisar
                    print("Aeronave {0} aterrisou".format(aviao))
                    print("> Aeronave {0} taxiando".format(aviao))
                    time.sleep(randrange(2,5)) # tempo para Taxiar
                    print("Aeronave {0} estacionada!".format(aviao))
                    self.temAeronaveEvento.clear()

                else: # prioridade eh 0 ou 1
                    aviao = self.aeronavesEsperando[0]
                    print("> Aeronave {0} taxiando".format(aviao))
                    mutex.release() # finaliza uso da Torre
                    time.sleep(randrange(2,5)) # tempo para Taxiar
                    print("- Aeronave {0} decolando (baixa prioridade)!".format(self.aeronavesEsperando[0]))
                    self.aeronavesEsperando.remove(self.aeronavesEsperando[0]) # apaga aeronaves cortando cabelo da espera
                    time.sleep(randrange(4,8)) # tempo para Decolar
                    print("- Aeronave {0} decolou".format(aviao))
                    self.temAeronaveEvento.clear() # limpa evento de aeronave esperando (uso da pista)

            else:
                # nao tem aeronaves "em espera"
                self.temAeronaveEvento.wait() # aguarda entrar aeronaves

        

    def aeronaveEntraAeroporto(self, aeronaves):
        mutex.acquire() # tenta pegar o Lock para "usar" a Torre (ou Torre gerencia pista ou olha o radar)
        print("\n> {0} entrou na radar".format(aeronaves))
        self.aeronavesEsperando.append(aeronaves)
        mutex.release()
        self.temAeronaveEvento.set() # gatilho do evento "tem aeronave" (iniciar uso da pista)



Aeroporto = Aeroporto()
Aeroporto.abrirAeroporto()  # inicia thread da pista

entrada, numAeronaves, i = [], 10, 0
while i < numAeronaves: 
    # aeronaves = [aviao, prioridade (0 ou 1)]
    aeronave = ["Aviao{0}".format(i), randrange(0,2)]
    entrada.append(aeronave)
    # Novo aeronaves entra na Aeroporto
    Aeroporto.aeronaveEntraAeroporto(aeronave)
    time.sleep(randrange(3,5)) # intervalo da entrada de aeronavess na Aeroporto 
    i+=1

print('* Ordem de entrada: ', entrada) # para comparar com ordem de saida (apos reordenacao por prioridade)


