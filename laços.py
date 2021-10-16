#exercício 1

s = 0
for i in range(11):
    if(i > 0):
        s = i/i**2 + s
        
        
print(s)


#exercício2
funcionarios = int(input('numero de funcionarios:'))
media = 0
soma = 0 
for x in range(10):
    salario = float(input('salario:'))
    codigo = int(input('código:'))
    soma = salario + soma
    media = soma / (x - 1)
print(f'o total da folha de pagamento é de {soma:.2f}')
print(f'a média salarial é de {media} reais')