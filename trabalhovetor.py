#01) Tentando descobrir se um dado era viciado, um dono de cassino
#honesto (ha! ha! ha! ha!) o lançou 20 vezes. Dados os 20 resultados
#dos lançamentos armazenados em um vetor, faça um algoritmo que
#determine o número de ocorrências de cada face.

import random

print('trabalho vetores')

verificardado = str(input('deseja verificar o dado?(s/n) '))

if(verificardado == "s"):
    rodadas = []
    for i in range(20):
        rodadas.append(random.randint(1,6))
        print(rodadas)
        print('')
    print('o número 1 apareceu',rodadas.count(1),'vezes')
    print('o número 2 apareceu',rodadas.count(2),'vezes')
    print('o número 3 apareceu',rodadas.count(3),'vezes')
    print('o número 4 apareceu',rodadas.count(4),'vezes')
    print('o número 5 apareceu',rodadas.count(5),'vezes')
    print('o número 6 apareceu',rodadas.count(6),'vezes')
else:
    print('obrigado')
