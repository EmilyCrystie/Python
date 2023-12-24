nome = 'Emily'
idade = 25
altura = 1.61
maioridade = idade > 18
peso = 82
imc = int(peso /altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

# identificação do elemento na memória
# mesmo id
v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

# ids diferentes
v1 = 'a'
v2 = 'b'
print(id(v1))
print(id(v2))