frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0

#fazer iteração: ato de percorrer cada um do elementos
while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1



# passar iteração para variável
nova_string = ''

while contador < tamanho_frase:
    nova_string += frase[contador]
    print(nova_string)
    contador += 1

print(nova_string)