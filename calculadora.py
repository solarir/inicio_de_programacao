def calculo():
    operacao = input('''Escolha uma das funcoes para realizar o seu calculo:
+ para soma
- para subtracao
* para multiplicacao
/ para duvisao
: ''' ) 

    num_1 = float(input("Escreva o primerio numero:"))
    num_2 = float(input("Escreva o segundo numero:"))

    if operacao == '+':
        print('{} + {} = '.format(num_1, num_2))
        print(num_1 + num_2)

    elif operacao == '-':
        print('{} - {} = '.format(num_1, num_2))
        print(num_1 - num_2)

    elif operacao == '*':
        print('{} * {} = '.format(num_1, num_2))
        print(num_1 * num_2)

    elif operacao == '/':
        print('{} / {} = '.format(num_1, num_2))
        print(num_1 / num_2)

    else:
        print("Operacao incorreta. Por facor, tente novamente.")

calculo()