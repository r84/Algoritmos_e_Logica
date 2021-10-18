#1) Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano, e 
#um país B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever um 
#algoritmo em PORTUGOL que seja capaz de calcular  e  imprimir o tempo necessário  para 
#que a população do país A ultrapasse a população do país B.


paisA = 5000000
paisB = 7000000
ano = 0

while paisA <= paisB:
    paisA += (paisA * 0.03)
    paisB += (paisB * 0.02)
    ano += 1
print(ano)  