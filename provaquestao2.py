print('questão 2')

n1 = int(input('informe o primeiro número:'))
op = str(input('qual operação será realizada? '))
n2 = int(input('informe o segundo número:'))

if(n1 == 0 or n2 == 0) and (op == '/'):
    print('operação inválida, impossível divisão por 0')
elif (op == '+'):
    print(n1 + n2)
elif (op == '-'):
    print(n1 - n2)
elif (op == '*'):
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
else:
    print('operação realizada com sucesso')