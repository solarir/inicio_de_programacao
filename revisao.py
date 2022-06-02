def verifica_par(n_entrada):
    x = n_entrada % 2
    if x == 0:
        print(" x e par")
    else: 
        print(" x e impar")


def verifica_valor(n_entrada):
    if n_entrada == 1:
        print("Esse numero e igual a um")
    elif n_entrada != 1:
        print("Esse numero e diferente de um")
    
    print("----")

    if n_entrada > 1:
        print("Esse numero e maior que um")
    elif n_entrada < 1:
        print("Esse numero e menor que um")

entrada = input ("entrada de numero: ")
verifica_par(entrada)
print("----")
verifica_valor(entrada)

