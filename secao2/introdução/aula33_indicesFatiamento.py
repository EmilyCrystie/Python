#positivos   [012345678]
texto      = 'Python s2'
print(texto[4])

#negativos  -[987654321]
texto      = 'Python s2'
print(texto[:-1])           #excluir último caracter


#fatiamento
nova_string = texto[2:6]
print(nova_string)

nova_string2 = texto[-9:-3]
print(nova_string2)

nova_string3 = texto[0:6:2]         #pegar do indice 0 até 6, pulando de 2 em 2 caracteres
print(nova_string3)

nova_string4 = texto[0::3]         #passar por td palavra, pulando de 3 em 3 caracteres
print(nova_string4)