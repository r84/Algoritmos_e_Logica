print('questão 1')

def imposto():
    nome = str(input('informe o seu nome: '))    
    renda = float(input('informe sua renda: '))
    aliquota = (0 * renda) / 100
      

    if (renda <= 1903.98):
        aliquota = 0;
        print(aliquota)
        print('isento')

    elif (renda <= 2826.65):
        aliquota = (7.5 * renda) / 100
        print('nome:{}'.format(nome))
        print('aliquota: R${}'.format(aliquota))
        print('valor da parcela com desconto: R${:.2f}'.format(aliquota - 142.80))
        print('salario liquido: {}'.format(renda - (aliquota - 142.80)))

    elif (renda <= 2.826,65):
        aliquota = (15 * renda) / 100
        print('nome:{}'.format(nome))
        print('aliquota: R${}'.format(aliquota))
        print('valor da parcela com desconto: R${:.2f}'.format(aliquota - 354.80))
        print('salario liquido: R${}'.format(renda - (aliquota - 354.80)))

    elif (renda >= 3751.06):
        aliquota = (22.5 * renda) / 100
        print('nome:{}'.format(nome))
        print('aliquota: R${}'.format(aliquota))
        print('valor da parcela com desconto: R${:.2f}'.format(aliquota - 636.13))
        print('salario liquido: R${}'.format(renda - (aliquota - 636.13))) 

    elif (renda > 4664.68):
        aliquota = (27.5 * renda) / 100
        print('nome:{}'.format(nome))
        print('aliquota: R${}'.format(aliquota))
        print('valor da parcela com desconto:{:.2f}'.format(aliquota - 869.36))
        print('salario liquido: R${}'.format(renda (aliquota - 869.36)))
            
    else:
        print('valor inválido')



imposto()


