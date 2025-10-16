texto = '''digite sua opção: 
1 - Água
2 - Refrigerante
3 - Suco
'''
opcao = input(texto)
if opcao == '1':
    bebida = 'água'
elif opcao == '2':
    bebida = 'refrigerante'
elif opcao == '3':
    bebida = 'suco'
else:
    bebida = 'inválida'

preco = 0
if bebida != 'inválida':
    tamanho = input('Qual o tamanho? P - M - G: ')
    if tamanho.upper() == 'P':
        preco = 3.00
    elif tamanho.upper() == 'M':
        preco = 5.00
    elif tamanho.upper() == 'G':
        preco = 7.00
    else:
        bebida = 'inválida'
total = 0

if bebida == 'inválida':
    print('Opção inválida')
else:
    qtde = int(input('Quantas unidades? '))
    total = preco * qtde
    print(
        f'Você escolheu {bebida} tamanho {tamanho.upper()} - Total: R$ {total:.2f}')
