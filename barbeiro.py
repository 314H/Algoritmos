# PROBLEMA
""" Barbeiro Dorminhoco
Se nao ha clientes, o barbeiro dorme;
Se a cadeira do barbeiro estiver livre, um cliente pode ser atendido imediatamente;
O cliente espera pelo barbeiro se houver uma cadeira de espera vazia;
Se nao tiver onde sentar o cliente vai embora;
Para implementar o problema, mantenha o barbeiro ocupado enquanto ha clientes e descansando caso nao haja nenhum;
O barbeiro e seus clientes correspondem a threads.
"""

import time
from random import randrange, choice
from threading import Thread, Lock, Event


# EXPLICACAO DO CODIGO
""" Nao ha clientes, barbeiro dorme
cadeira livre, cliente atendido imediatamente
se nao tiver cadeira vazia (onde cliente sentar) ele vai embora

LOCK = Sala de espera
Barbeiro pega o lock no inicio do trabalho, se tiver clientes na sala de espera
Assim que ele puxa um cliente da sala de espera o lock eh liberado
Quando lock eh liberado, novos clientes podem entrar na barbearia
Quando cliente senta na sala de espera libera o lock
Se a sala estiver cheia cliente vai embora e lock eh liberado
##########
EVENT = BarbeiroTrabalhando
Quando nao tem clientes na fila, barbeiro aguarda gatilho do evento
Quando cliente senta na sala de espera da gatilho no evento
Apos finalizar corte de cabelo, o evento eh limpo (resetado)
"""


mutex = Lock() # variavel para prender uma thread ate que outra finalize

class Barbearia:
    barbeiroTrabalhandoEvento = Event() # gatilho para acoes

    def __init__(self, numeroCadeiras):
        self.numeroCadeiras = numeroCadeiras # da sala de espera
        self.clientesEsperando = [] # vetor com os clientes na sala de espera
        print("Barbearia iniciou com {0} cadeiras".format(numeroCadeiras))


    # inicia o trabalho/acoes do barbeiro
    def abrirBarbearia(self):
        print("### Barbearia esta abrindo ### \n(inicia a thread do barbeiro)\n")
        Thread(target=self.barbeiroVaiTrabalhar).start() # inicia thread para trabalho do barbeiro


    def barbeiroVaiTrabalhar(self):
        while True:
            mutex.acquire() # tenta pegar o Lock, caso esteja livre (se nao estiver, espera estar)
            # apenas com o lock o codigo abaixo e executado
            if len(self.clientesEsperando) > 0:  # se tiver cliente esperando
                clienteSelecionado = choice(self.clientesEsperando) # pega cliente aleatoriamente da fila de espera
                self.clientesEsperando.remove(clienteSelecionado) # apaga cliente cortando cabelo da espera
                mutex.release() # libera o lock - novos clientes podem entrar
                self.barbeiroTrabalhandoEvento.clear() # remove o evento (limpa) - para reinciar o processo
                print("  {0} - cortando o cabelo".format(clienteSelecionado))
                time.sleep(randrange(6, 10)) # corte de cabelo - 6 a 10s
                print("{0} finalizou".format(clienteSelecionado))
            else:
                mutex.release() # libera o lock
                print("Barbeiro dormindo")
                self.barbeiroTrabalhandoEvento.wait()


    def ClienteEntraBarbearia(self, cliente):
        mutex.acquire() # tenta pegar o Lock, caso esteja livre (se nao estiver, espera estar)
        print("\n{0} entrou na barbearia".format(cliente))

        if len(self.clientesEsperando) == self.numeroCadeiras:
            print(" > Sala de espera cheia, {0} esta indo embora.".format(cliente))
            mutex.release()
            return cliente
        else:
            print("{0} sentou na sala de espera".format(cliente))
            self.clientesEsperando.append(cliente)
            print("Espera: ", self.clientesEsperando, '\n')
            mutex.release()
            self.barbeiroTrabalhandoEvento.set()
            return None



barbearia = Barbearia(2)
barbearia.abrirBarbearia()  # inicia thread do barbeiro

desistentes, numClientes, i = [], 10, 0
while i < numClientes: 
    cliente = "Nome{0}".format(i)
    # Novo cliente entra na barbearia
    desistentes.append(barbearia.ClienteEntraBarbearia(cliente))
    for desit in desistentes:
        if desit == None:
            desistentes.remove(None)
    time.sleep(randrange(4, 6)) # intervalo da entrada de clientes na barbearia 4 a 6 seg
    i=i+1


print("> Clientes que dessitiram e foram embora: ", desistentes)


