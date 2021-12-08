# -*- coding: utf-8 -*- #
"""
@author: Laura
"""

import struct
from collections import namedtuple
from binaryFile import binaryFile

Vendedor = namedtuple("Vendedor", "Codigo_Vendedor Nome_Vendedor Valor_da_Venda Mes_Ano")
# O CAMPO DO FORMATO DO REGISTRO é sf ( sizeformat ) estava assim i015sfb
sf = 'i020sf007s'
"""
formato string do nome vc colocou 20 estava 15
não colocou a formatação do campo MM/AAAA str com 7
e estava com um campo boolean no final e não existe
"""
mf = binaryFile(sf)


def cria_arquivo():
    mf.fopen('vendedor.dat', 'wb')
    mf.fclose()
    pass


def inserir_vendedor():
    Nome_Vendedor = str(input("Digite o nome do vendedor: "))
    Nome_Vendedor = Nome_Vendedor.ljust(20)
    Codigo_Vendedor = int(input("Digite o codigo do vendedor: "))
    Valor_da_Venda = float(input("Digite o valor da venda: "))
    Mes_Ano = str(input("Digite o mes e o ano no formato MM/AAAA: "))
    mf.fopen('vendedor.dat', 'ab+')
    mf.fwrite([Codigo_Vendedor, Nome_Vendedor, Valor_da_Venda, Mes_Ano])
    mf.fclose()
    pass


def remover_vendedor():
    Codigo_Vendedor = int(input("Digite o codigo do vendedor: "))
    mf.fopen('vendedor.dat', 'rb+')
    pos = mf.find(Codigo_Vendedor, 0)
    if pos == -1:
        print('Vendedor nÃ£o cadastrado')
        return
    mf.remove(Codigo_Vendedor, 0)
    mf.fclose()
    pass


def listagem():
    print('Vendedores Cadastrados')
    mf.fopen('vendedor.dat', 'rb')
    mf.fseek(0)
    while not mf.feof():
        fields = mf.fread()
        vendedor = Vendedor(Codigo_Vendedor=fields[0], Nome_Vendedor=fields[1], Valor_da_Venda=fields[2],
                            Mes_Ano=fields[3])
        print(vendedor)
    mf.fclose()
    pass


def dump():
    mf.fopen('vendedor.dat', 'rb')
    mf.dump()
    mf.fclose()
    pass


def consultaCodigo():
    mf.fopen('vendedor.dat', 'rb')
    Codigo_Vendedor = int(input("Digite o codigo do vendedor: "))
    pos = mf.find(Codigo_Vendedor, 0)
    if pos == -1:
        print('Vendedor nÃ£o cadastrado')
        return
    mf.fseek(pos)
    fields = mf.fread()
    vendedor = Vendedor(Codigo_Vendedor=fields[0], Nome_Vendedor=fields[1], Valor_da_Venda=fields[2], Mes_Ano=fields[3])
    print(vendedor)
    mf.fclose()
    pass


def consultaNome():
    mf.fopen('vendedor.dat', 'rb')
    Nome_Vendedor = input("Digite o nome : ")
    Nome_Vendedor = Nome_Vendedor.ljust(15)
    pos = mf.find(Nome_Vendedor, 1)
    if pos == -1:
        print('Vendedor não cadastrado')
        return
    mf.fseek(pos)
    fields = mf.fread()
    vendedor = Vendedor(Codigo_Vendedor=fields[0], Nome_Vendedor=fields[1], Valor_da_Venda=fields[2], Mes_Ano=fields[3])
    print(vendedor)
    mf.fclose()
    pass


def alterarVenda():
    mf.fopen('vendedor.dat', 'rb')
    Codigo_Vendedor = int(input("Digite o codigo do vendedor que realizou a venda: "))
    posCod = mf.find(Codigo_Vendedor, 0)
    if posCod == -1:
        print('Vendedor nÃ£o cadastrado')
        return
    else:
        Mes_Ano = int(input("Digite o mes e ano da venda (no formato MM/AAAA): "))
        posMes = mf.find(Mes_Ano, 0)
        novoValor = float(input('Digite o novo valor da venda: '))
        Valor_da_Venda = novoValor
        mf.fwrite(Valor_da_Venda)


def vendedorMaiorVenda():
    maiorVenda = 0
    print('Vendedor com Maior Venda: ')
    mf.fopen('vendedor.dat', 'rb')
    mf.fseek(0)

    while not mf.feof():
        fields = mf.fread()
        vendedor = Vendedor(Codigo_Vendedor=fields[0], Nome_Vendedor=fields[1], Valor_da_Venda=fields[2],
                            Mes_Ano=fields[3])
        if fields[2] > maiorVenda:
            maiorVenda = fields[2]

    pos = mf.find(maiorVenda, 2)
    mf.fseek(pos)
    fields = mf.fread()
    vendedor = Vendedor(Codigo_Vendedor=fields[0], Nome_Vendedor=fields[1], Valor_da_Venda=fields[2], Mes_Ano=fields[3])
    print(vendedor)
    mf.fclose()


menu = 9
while menu != 0:
    print(
        '1- Criar arquivo \n2- Incluir vendedor \n3- Excluir vendedor \n4- Alterar valor de uma venda \n5- Imprimir registros \n6- Consultar vendedor de maior venda')
    print('0- Sair')
    menu = int(input('O que deseja fazer? '))
    if menu == 1:
        cria_arquivo()
    if menu == 2:
        inserir_vendedor()
    if menu == 3:
        remover_vendedor()
    if menu == 4:
        print('Para alterar o valor de uma venda informe codigo do vendedor: ')
        alterarVenda()
    if menu == 5:
        listagem()
    if menu == 6:
        vendedorMaiorVenda()
