"""
Faça um programa que peça ao usuário para digitar um nº inteiro,
informe se este nº é par ou ímpar. Caso o usuárionão digite um nº inteiro,
informe q não é inteiro
"""

numero = input("Informe um nº inteiro: ")
numero = int(numero)

if (numero % 2) == 0:
    print('Nº par')
else:
    print('Nº ímpar')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, 
exiba a saudaçao aprorpiada (bom dia: 0-11, boa tarde: 12-17, boa noite: 18-23)
"""

hora = int(input('Informe a hora deste momento: '))

if hora <= 11:
    print('bom dia')
elif hora >= 12 and hora <= 17:
    print('boa tarde')
else:
    print('boa noite')



"""
Faça um programa que peça o primeiro nome do usuário. se tiver 4 letras ou menos,
escreva "seu nome é curto", se tiver entre 5 e 6 letras, escreve seu nome é médio,
maior q 6 escreva seu nome é mto grande
"""

nome = input('Informe seu 1º nome: ')

if len(nome) <= 4:
    print('seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('seu nome é médio')
else:
    print('seu nome é grande')