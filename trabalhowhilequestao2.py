# 2) O cardápio de uma lanchonete é o seguinte:  
 
# Especificação Código  Preço 
# Cachorro quente 100 R$ 1,20 
# Bauru simples 101 R$ 1,30 
# Bauru com ovo 102 R$ 1,50 
# Hambúrguer 103 R$ 1,30 
# Cheeseburguer 104 R$ 1,30 
# Refrigerante 105 R$ 1,00 
 

# Escrever um  algoritmo que leia o  código do item  pedido,  a quantidade  e  calcule  o valor a 
# ser  pago  por  aquele  lanche.  Considere  que  a  cada  execução  somente  será  calculado  um 
# item. O programa irá ler os pedidos enquanto o código do produto não for 999.  Quando o 
# cliente  informar  999,  o  algoritmo  deve  informar  a  quantidade  de  pedidos  realizada,  a 
# quantidade de itens vendido e o valor total arrecadado.

codigo = int(input('código do produto:'))
valor = 0
valortotal = 0
itenstotal = 0
pedidos = 0
while codigo != 999:
    quantidade = int(input('informe a quantidade:'))
    if codigo == 100:
        valor = quantidade * 1.20
        print(f"cachorro quente , valor:{valor:.2f}")
    elif codigo == 101:
        valor = quantidade * 1.30
        print(f"bauru simples , valor:{valor:.2f}")
    elif codigo == 102:
        valor = quantidade * 1.50
        print(f"bauru com ovo , valor:{valor:.2f}")
    elif codigo == 103:
        valor = quantidade * 1.30
        print(f"Hamburguer , valor:{valor:.2f}")
    elif codigo == 104:
        valor = quantidade * 1.30
        print(f"Cheeseburguer , valor:{valor:.2f}")
    elif codigo == 105:
        valor = quantidade * 1.00
        print(f"refrigerante , valor:{valor:.2f}")
    else:
        print("código inválido")
    valortotal += valor
    itenstotal += quantidade
    pedidos += 1
    codigo = int(input('código do produto:'))    
    
print(f"valor total:{valortotal:.2f}")
print(f"total de pedidos:{pedidos}")
print(f"total de itens: {itenstotal}")

    
    
