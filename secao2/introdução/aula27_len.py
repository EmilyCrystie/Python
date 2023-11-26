# não funciona com tipos numéricos
#retorna valor em tipo inteiro

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres)


if qtd_caracteres < 5:
    print("você precisa digitar pelo menos 5 caracteres")
else:
    print('você foi cadastrado no sistema')


string1 = input('digite alguma coisa: ')
string2 = input('digite outra coisa: ')
print(f'a qtd total de caracteres foi {len(string1) + len(string2)}')

