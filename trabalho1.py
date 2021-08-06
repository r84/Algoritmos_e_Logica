#Trabalho 1
#1) Escreva um algoritmo que leia o nome, idade, departamento, número de filhos, salário do funcionário, dia, mês (string) e ano de contratação de uma
#empresa. Posteriormente imprima esta mensagem:

#‘O NOME_FUNCIONARIO tem IDADE_FUNCIONARIO anos e trabalha no departamento NOME_DEPARTAMENTO.'
#‘O NOME_FUNCIONARIO tem NUMERO_FILHOS filhos e ganha mensalmente SALARIO_FUNCIONARIO.'
#
#‘O funcionário NOME_FUNCIONARIO foi contratado no dia DIA_ONTRATAÇÃO de MÊS_CONTRATAÇÃO de ANO_CONTRATAÇÃO’



nome = str(input('qual seu nome ?'))
idade = int(input('qual a sua idade? '))
departamento = str(input('qual o seu departamento? '))
filhos = int(input('quantos filhos você possui? '))
salario = float(input('qual o seu salário? '))
diacontratacao = int(input('qual dia você foi contratado? '))
mescontratacao = str(input('qual mês você foi contratado? '))
anocontratacao = int(input('qual ano você foi contratado?'))


print('')
print('o {} tem {} anos e trabalha no departamento {}.'.format(nome,idade,departamento))
print('o {} tem {} filhos e ganha mensalmente R${}'.format(nome,filhos,salario))
print('')
print('o funcionário {} foi contratado no dia {} de {} de {}'.format(nome,diacontratacao,mescontratacao,anocontratacao))


