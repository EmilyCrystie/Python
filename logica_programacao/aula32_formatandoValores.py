"""
Formatando valores com modificadores

:s - texto (informa ser uma string)
:d - inteiros
:f - flutuantes
:.(numero)f - qtd de casa decimais
:(caractere)(> ou < ou ^)(qtd)(tipo - s, d ou f) - determinar tamanho especifico

> - esquerda
< - direita
^ - centro
"""

num1 = 10
num2 = 3
divisao = num1 / num2

print('{}'.format(divisao))

print('{:.2f}'.format(divisao))
#ou
print(f'{divisao:.2f}')


#qtd delimitada
num_1 = 1
print(f'{num_1:0>10}')

print(f'{num_1:0^10}')


nome = 'emily crystie'
print(f'{nome:#^40}')

nome2 = 'emily'
sobrenome = 'crystie'
nome_formatado = '{0:$^20} {1:#^20}'.format(nome2, sobrenome)       #uso do index
print(nome_formatado)