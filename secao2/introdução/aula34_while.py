"""
while condicao:
    pass                    # bloco de código a ser executado
"""

x = 0
while x < 11:
    print(x)
    x = x + 1

print("laço/loop acabou")



y = 0
while y < 10:
    if y == 3:
        y = y + 1
        continue            #código depois de continue para de executar (debugar para ver processo)

    print(y)
    y = y + 1
print('acabou')



z = 0
while z < 10:
    if z == 3:
        z = z + 1
        break            #finaliza código qdo for verdadeiro

    print(z)
    z = z + 1
print('acabou')