#1) Desenvolva um algoritmo que leia o nome, a idade e o time de um jogador de futebol
# e posteriormente imprima essas informações na tela.

nome = str(input('qual o seu nome?'))
idade = int(input('qual a sua idade?'))
time = str(input('em que time você joga?'))

print('nome:{}'.format(nome))
print('idade: {} anos'.format(idade))
print('time:{}'.format(time))

#2)Faça um algoritmo que leia as seguintes informações do funcionário de uma empresa:
#nome, salário, idade, altura, peso, número de filho. Após essa leitura, escreva na tela essas
#informações.

nome = str(input('qual o seu nome?'))
salario = float(input('qual o seu salário?'))
idade = int(input('qual a sua idade?'))
altura = float(input('qual a sua altura?'))
peso = float(input('qual o seu peso?'))
filhos = int(input('quantos filhos você possui?'))

print('nome: {}'.format(nome))
print('salário: {}'.format(salario))
print('idade: {} anos'.format(idade))
print('altura: {}cm'.format(altura))
print('peso: {}kg'.format(peso))
print('filhos: {}'.format(filhos))

#3) Escreva um algoritmo que leia o nome e o curso de um aluno do Centro Tecnológico e
#imprima esta mensagem:  ‘O aluno cadastrado é o NOME_LIDO e é do curso
#CURSO_LIDO.'

nome = str(input('nome:'))
curso = str(input('curso:'))

print('o aluno cadastrado é o {} e é do curso {}'.format(nome,curso))

