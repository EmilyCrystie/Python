contador = 1            #conta de forma linear
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('cheguei no else')            #executar caso condição seja falsa
print('executado após chegar no break')         #executar caso loop seja encerrado, nesta situação, pelo break