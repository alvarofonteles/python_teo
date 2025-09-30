print('Será que você pode beber ou comprar Alcool?')

idade = input('digite sua idade: ')

if int(idade) >= 70 :    
    print('Liberado a compra.')
    print('Mas não pode beber.')
elif int(idade) >= 18 :    
    print('Liberado a compra.')
    print('Pagar no caixa.')
else :     
    print('Proibido!!!')
    print('Não Insistir.')

idade = input('digite sua idade novamente: ')

if int(idade) >= 70 :    
        print('Liberado a compra.')
        print('Mas não pode beber.')
else :
    if int(idade) >= 18 :    
        print('Liberado a compra.')
        print('Pagar no caixa.')
    else :     
        print('Proibido!!!')
        print('Não Insistir.')