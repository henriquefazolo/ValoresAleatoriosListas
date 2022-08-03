'''
Crie uma lista de int vetF com tamanho 100 e atribua aos índices pares um valor aleatório entre 0 e 100 e aos ímpares o
valor de seu índice multiplicado por 2 e mostre seu valor na tela de cada um dos elementos.
'''

import random
vetF = []
for i in range(100):
    if i % 2 == 0:
        vetF.append(random.randint(0, 100))
    else:
        vetF.append(i*2)
print(vetF)


