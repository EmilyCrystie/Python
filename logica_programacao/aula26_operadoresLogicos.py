"""
and : e
or : ou
not : sem valor
in e not in : dentro/está e não há/não está
"""

# not
a = ''
b = 0

if not a:
    print('pfv, preencha o valor de A')

#######

num_1 = 0
num_2 = 0

if not num_1 != num_2:          # está invertendo o falso para verdadeiro
    print('Retorno 1')
else:
    print('Retorno 2')

# in
nome = 'emily'

if 'y' in nome:
    print('existe a letra Y no seu nome')