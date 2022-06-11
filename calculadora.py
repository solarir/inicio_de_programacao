# Funções devem ser simplificadas para facilitar a leitura do código
# Se a lógica pode sem encapsulada em uma função a mesma deve ser deslocada 
def get_input_data():
    operacao = input('''Escolha uma das funcoes para realizar o seu calculo:
+ para soma
- para subtracao
* para multiplicacao
/ para duvisao
: ''' ) 

    num_1 = float(input("Escreva o primerio numero:"))
    num_2 = float(input("Escreva o segundo numero:"))
    return[operacao, num_1, num_2]

def sum(num_1, num_2): 
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)

def subtraction(num_1, num_2):
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)

def multiply(num_1, num_2):
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)
    
def division(num_1, num_2):
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)


def calculate(operacao, num_1, num_2):
    if operacao == '+': # Isso facilita a leitura nesse ponto
        sum(num_1, num_2) # Fica laro que o retorno é uma soma 

    elif operacao == '-':
        subtraction(num_1, num_2)

    elif operacao == '*':
        multiply(num_1, num_2)

    elif operacao == '/':
        division(num_1, num_2)

    else:
        print("Operacao incorreta. Por facor, tente novamente.")

# Se a funcao chama calculate ela deve conter apenas calculos
# A funcao de input deve ter um nome que remete a entrada
[operacao, num_1, num_2] = get_input_data()
calculate(operacao, num_1, num_2) 