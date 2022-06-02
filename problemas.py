from re import X


def localizar(lista):
    x = lista[0]
    for numero in lista:
        if x > numero:
            x = numero
    return x

        
lista = [3,4,5,1,6,7,10]

resultado = localizar(lista)
print(resultado)
print(min(lista))