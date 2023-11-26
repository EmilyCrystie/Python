"""
variavel = [valor, valor, valor]

suporta: strings, nºs, booleanos, fatiamento
"""

alfabeto = ['A', 'B', 'C', 'D', 'E']
print(alfabeto[-1])


# extend: acrescenta dados de uma lista em outra
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1)
print(l2)


l1.extend(l2)
print(l1)


# append: adiciona dados ao final de uma lista
l2.append('b')
print(l2)


# insert: adiciona dados em local determinado da lista (indice, valor a ser adicionado)
l2.insert(0, 'a')
print(l2)


#deletar último elemento da lista
l2.pop()
print(l2)


#deletar fatia da lista
del(l2[1:3])
print(l2)


#pegar valor máximo ou mínimo da lista
print(max(l1))
print(min(l1))


#criar lista de forma rápida
l3 = list(range(1,10))
print(l3)

l4 = list(range(0,100,8))
print(l4)


# jogo da palavra secreta
secreto = 'borboleta'
digitadas = []
chances = 3

while True:
    if chances <= 0:...

    letra = input('Digite uma letra: ')

    if len(letra) > 1:...

    digitadas.append(letra)

    if letra in secreto:
        print()