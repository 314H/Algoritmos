"""
@author: Laura
"""


def GravarReceita():
    arquivoReceitas = open("Receitas.txt", 'a')
    vetorIngredientes = []
    numReceitas = int(input('Numero de Receitas: '))
    for i in range (numReceitas):
           titulo = input("Digite o nome da receita:  ")
           arquivoReceitas.write(titulo.upper())
           numIngredientes = int(input("Digite o numero de ingredientes: "))
           
           vetorIngredientes = []
           for j in range (0,numIngredientes,+1):
               vetorIngredientes.append(input("Digite o {}º ingrediente: ".format(j+1)))
           
           arquivoReceitas.write('\nIngredientes: \n\n')
           arquivoReceitas.write(str(vetorIngredientes))
           
           arquivoReceitas.write('\nModo de Preparo: \n')
           preparo = input("Descreva o modo de preparo: ")
           arquivoReceitas.write(preparo)
           arquivoReceitas.write('\n\n')
    arquivoReceitas.close()
    pass


def ListarReceitas():
    arquivoReceitas = open("Receitas.txt", 'r')
    listaReceitas = arquivoReceitas.read()
    arquivoReceitas.close()
    print(listaReceitas)
    return listaReceitas


def EncontrarReceita():
    nome = (input('Digite o titulo da receita procurada: '))
    arquivoReceitas = open( "Receitas.txt", 'r' )
    titulo = nome.upper()
    for line in arquivoReceitas:
        if titulo in line:
            ing = arquivoReceitas.readline()
            ingredientes = arquivoReceitas.readline()
            modoP = arquivoReceitas.readline()
            preparo = arquivoReceitas.readline()
            print(titulo, "\n", ing, ingredientes, modoP, preparo)
    if titulo not in line:
        print ('Receita não encontrada!')
        print("não encontrada!")
    pass


menu = 0
while menu != 4:
    print('\nMENU\n1- Cadastrar Receita \n2- Ler todas as receitas \n3-Buscar uma receita \n4-Sair')
    menu = int(input('O que deseja fazer? '))
    if menu == 1:
        GravarReceita()
    if menu == 2:
        print("Receitas Gravadas: \n")
        ListarReceitas()
    if menu == 3:
        EncontrarReceita()
    if menu == 4:
        print("Saiu")
