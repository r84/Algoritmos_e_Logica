dia = int(input('informe o dia: '))
mes = int(input('informe o mês: '))
ano = int(input('informe o ano: '))

calc1 = ano - 1900
calc2 = calc1 / 4

mesvalor = int

if mes == 1:
    mesvalor = 0
elif mes == 2 or mes == 3 or mes == 11:
    mesvalor = 3
elif mes == 4 or mes == 7: 
    mesvalor = 6
elif mes == 5:
    mesvalor = 1
elif mes == 6:
    mesvalor = 4
elif mes == 8:
    mesvalor = 2
elif mes == 9 or mes == 12:
    mesvalor = 5

soma = calc1 + calc2 + dia + mesvalor
result = soma % 7


if result == 0:
    print('domingo')
elif result >= 1:
    print('segunda-feira')
elif result >= 2:
    print('terça-feira')
elif result >= 3:
    print('quarta-feira')
elif result >= 4:
    print('quinta-feira')
elif result >= 5:
    print('sexta-feira')
elif result >= 6:
    print('sabado')
else:
    print('valor inválido')


