print('Trabalho comando For')

def imposto():
    contribuintes = int(input('informe o número de contribuintes: '))
    total = []
    
    
    for i in range(contribuintes):
        cpf = int(input('informe o cpf do contribuinte: '))
        renda = float(input('informe o renda do contribuinte: '))
        aliquota = (0 * renda) / 100
        total.append(renda)
        
   
        

        if (renda <= 1903.98):
            aliquota = 0;
            print(aliquota)
            print('isento')

        elif (renda <= 2826.65):
            aliquota = (7.5 * renda) / 100
            print('aliquota: {}'.format(aliquota))
            print('valor da parcela com desconto: R${:.2f}'.format(aliquota - 142.80))
            print('salario liquido: {}'.format(renda - (aliquota - 142.80)))

        elif (renda <= 2.826,65):
            aliquota = (15 * renda) / 100
            print('aliquota: {}'.format(aliquota))
            print('valor da parcela com desconto: R${:.2f}'.format(aliquota - 354.80))
            print('salario liquido: {}'.format(renda - (aliquota - 354.80)))

        elif (renda >= 3751.06):
            print('aliquota: {}'.format(aliquota))
            print('valor da parcela com desconto: R${:.2f}'.format(aliquota - 636.13))
            print('salario liquido: {}'.format(renda - (aliquota - 636.13))) 

        elif (renda > 4664.68):
            aliquota = (27.5 * renda) / 100
            print('aliquota: R${}'.format(aliquota))
            print('valor da parcela com desconto:{:.2f}'.format(aliquota - 869,36))
            print('salario liquido: {}'.format(renda (aliquota - 869,36)))
            
        else:
            print('valor inválido')

    print('valor total:{}'.format(sum(total)))

imposto()


