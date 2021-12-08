# PROBLEMA
""" Jantar dos Filosofos
O problema é estabelecido em uma comunidade isolada de 5 filósofos (0-4);
Os filósofos engajam-se somente em duas atividades: pensar e comer;
Implemente a solução evitando situações indesejadas como deadlocks e starvation;
"""

import time, random
from threading import Lock, Thread


# 5 filosofos e 5 garfos
# Cada garfo eh um lock (apenas um filosofo pode pegar um garfo)
# Cada filosofo eh uma Thread

garfo = []
for i in range(5):
   garfo.append(Lock()) # crio um lock pra cada garfo


def vezesFilosofoComeu(f, vezesComidas):
   # funcao para incrementar (contar) o numero de vezes que filosofo comeu
   # garantir que nao houve starvation
   if f == vezesComidas[0][0]: # thread0 = filosofo 0
      vezesComidas[0][1] = vezesComidas[0][1]+1 # incremento vezes que o filosofo comeu
   elif f == vezesComidas[1][0]: # thread1 = filosofo 1
      vezesComidas[1][1] = vezesComidas[1][1]+1
   elif f == vezesComidas[2][0]: # thread2 = filosofo 2
      vezesComidas[2][1] = vezesComidas[2][1]+1
   elif f == vezesComidas[3][0]: # thread3 = filosofo 3
      vezesComidas[3][1] = vezesComidas[3][1]+1
   elif f == vezesComidas[4][0]: # thread4 = filosofo 4
      vezesComidas[4][1] = vezesComidas[4][1]+1
   return vezesComidas


def filosofos(f, vezesComidas):
   start, end = time.time(), time.time() # temporizador para encerrar a thread (para nao rodar infinitamente na maquina)
   f = int(i)
   while (end-start) < 60: # thread dura 60 segundos
      garfo[f].acquire()  # pega garfo da esquerda
      garfo[(f + 1) % 5].acquire()  # pega garfo da direita

      print("Filosofo{0} pega garfo {1} (esquerda) e pega garfo {2} (direita)".format(f, f, (f + 1) % 5))

      print("* Filósofo{0} comendo...".format(f))
      print("> > Filósofo{0} pensando...".format((f + 1) % 5)) # filosofo a direita nao consegue comer - pensa
      print("> > Filósofo{0} pensando...".format((f - 1) % 5)) # filosofo a esquerda nao consegue comer - pensa
      vezesComidas = vezesFilosofoComeu(f, vezesComidas)
      
      if f == 0:
         print('Vezes comidas por cada filosofo: '.format(f), vezesComidas) # imprime apenas na thread 0, para nao poluir terminal
      
      time.sleep(random.randint(1, 5))  # tempo comendo

      garfo[f].release() # libera lock (garfo da esquerda)
      garfo[(f + 1) % 5].release() # libera lock (garfo da direita)

      print(" > Filósofo{0} pensando...".format(f)) # apos comer filosofo vai pensar

      time.sleep(random.randint(1, 10)) # espera entre cada filosofo
      end = time.time()

   print('\nFim da thread {0} ###'.format(f)) # fora do while, indica quando as threads acabam
   if f == 0: # para imprimir apenas uma vez
      print('Vezes comidas por cada filosofo: ', vezesComidas)
   
   exit(0)




print("Filosofos se sentam um ao lado do outro")
print("g0 - g1 - g2 - g3 - g4 - g0") # garfos
print("   f0   f1   f2   f3   f4\n") # filosofos

# inicio a thread de cada filosofo
numFilosofos, vezesComidas = 5, []
for i in range(numFilosofos):
   print("Iniciar thread - Filósofo{0}".format(i))
   vezesComidas.append(([i,0]))
   Thread(target=filosofos, args=tuple([i,vezesComidas])).start()

