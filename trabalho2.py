#01)  A  lanchonete  Gostosura  vende  apenas  um  tipo  de  sanduíche,  cujo  recheio  inclui 
#duas fatias de queijo, três fatias de presunto e uma rodela de hambúrguer. Sabendo que 
#cada fatia de queijo pesa 50 gramas, cada fatia de presunto pesa 55 gramas, e que cada 
#hambúrguer  pesa  130  gramas,  faça  um  algoritmo  em  que  o  dono  forneça  a  quantidade 
#de  sanduíches  a  fazer,  e  o  software  informe  as  quantidades  (em  quilos)  de  queijo, 
#presunto e carne necessário para compra.

queijo = 0.050 * 2
presunto = 0.055 * 3
carne = 0.130

quantidade = int(input('quantos hamburgueres serão feitos? '))

print('quantidades')
print('queijo: {} kg'.format(queijo * quantidade))
print('presunto: {} kg'.format(presunto * quantidade))
print('carne: {} kg'.format(carne * quantidade))

#02) Escreva um algoritmo que leia dois números que deverão ser colocados, 
#respectivamente, nas variáveis VA e VB. O algoritmo deve, então, trocar os valores de 
#VA por VB e vice-versa e mostrar o conteúdo destas variáveis.

VA = int(input('insira o primeiro número: '))
VB = int(input('insira o segundo número: '))

print('VA: {}'.format(VA))
print('VB: {}'.format(VB))
print('agora...')

aux = VB
VB = VA
VA = aux

print('VA: {}'.format(VA))
print('VB: {}'.format(VB))
