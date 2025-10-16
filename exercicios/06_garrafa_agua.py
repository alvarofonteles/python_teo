texto = '''digite sua opção: 
1 - Água
2 - Refrigerante 
3 - Suco
'''
# texto = f'digite sua opção: \n 1 - Água \n 2 - Refrigerante \n 3 - Suco \n'
opcao = input(texto)
if opcao == '1':
    print('Você escolheu água')
    tamanho = input('Qual o tamanho? P - M - G: ')
    if tamanho == 'P':
        print('Você escolheu água pequena')
    elif tamanho == 'M':
        print('Você escolheu água média')
    elif tamanho == 'G':
        print('Você escolheu água grande')
    else:
        print('Tamanho inválido')
elif opcao == '2':
    print('Você escolheu refrigerante')
    tamanho = input('Qual o tamanho? P - M - G: ')
    if tamanho == 'P':
        print('Você escolheu refrigerante pequeno')
    elif tamanho == 'M':
        print('Você escolheu refrigerante médio')
    elif tamanho == 'G':
        print('Você escolheu refrigerante grande')
    else:
        print('Tamanho inválido')
elif opcao == '3':
    print('Você escolheu suco')
    tamanho = input('Qual o tamanho? P - M - G: ')
    if tamanho == 'P':
        print('Você escolheu suco pequeno')
    elif tamanho == 'M':
        print('Você escolheu suco médio')
    elif tamanho == 'G':
        print('Você escolheu suco grande')
    else:
        print('Tamanho inválido')
else:
    print('Opção inválida')
