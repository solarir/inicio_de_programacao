def soma(n1, n2):  
    # def - Comando para criar uma funcao
    # *nome_na_frente_do_def* - nome da funcao
    # variaveis no parenteses - argumentos da funcao
    return n1 + n2 # return volta o resultado passado para ele

def subitracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    n3 = n1 * n2
    return n3 

def divisao(n1, n2):
    n3 = float(n1) / float(n2)
    return n3

num_1 = input("Escreva o primeiro numero: ")
num_2 = input("Escreva o segundo numero: ")

resultado_1 = soma(num_1, num_2)
resultado_2 = subitracao(n1 = num_1, n2 = num_2)
resultado_3 = multiplicacao(n1 = num_1, n2 = num_2)
resultado_4 = divisao(n1 = num_1, n2 = num_2)
print("soma " + str(resultado_1))
print("subitracao " + str(resultado_2))
print("multiplicacao " + str(resultado_3))
print("divisao " + str(resultado_4))
print(" {}".format(resultado_4))

# type cast : ato de transformar um tipo de variavel em outro. 
# str: texto; float/doble: numero fracionado; int: numero inteiro.
# juntar texto, listar ou objetos se chama concatenacao
# def = comando para criar funcao
# print = "escrever na tela"
# return = retornar ao comando ou variavel indicada.
# input = entrada dinamica: se adapita ao tipo de variavel indicada.
# output = print
# format = referenciar texto para chave.