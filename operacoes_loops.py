def verifica_par(n_entrada):
    x = n_entrada % 2
    if x == 0:
        print(str(n_entrada) + " e par")
    else: 
        print(str(n_entrada) + " e impar")

def verifica_par_lista(lista):
    for numero in lista:
        x = numero % 2
        if x == 0:
            print(str(numero) + " e par")
        else: 
            print(str(numero) + " e impar")

def verifica_par_lista_formal(lista):
    for numero in lista:
        verifica_par(numero)

def verificar_por_6(lista):
    iterador = 0
    while(lista[iterador] != 6):
        print(lista[iterador])
        iterador += 1

lista = [4, 5, 6, 7]

for numero in lista:
    verifica_par(numero)

verifica_par_lista(lista)

verificar_por_6(lista)