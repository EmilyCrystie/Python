#funções de string: checagem de string para ser convertida em inteiro)

num1 = input('Digite um nº: ')
num2 = input('Digite outro nº: ')

# isnumeric: retorna true se tds caracteres da string forem numéricos
print(num1.isnumeric())


# isdecimal: retorna true se tds caracteres da string forem decimais
print(num1.isdecimal())


# isdigit: retorna true se tds caracteres da string forem dígitos (caracteres decimais, q precisem de tratamento especial)
print(num1.isdecimal())


#opção 1
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não pude converter nº para realizar contas')


#opção 2: tenta executar o código, qualquer erro, mostre a outra forma
try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR')



# https://docs.python.org/3/library/stdtypes.html