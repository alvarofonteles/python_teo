# Tabuada de Soma
# %%
def tabuada_soma(numero, operador):
    operadores = ['+', '-', '/', '*']  # para algo escalável, futuro

    if operador not in operadores:
        return f'Operador ({operador}) Inválido'

    if operador == '+':
        if numero == 0:  # executa toda a tabela
            for soma in range(1, 11):
                print('')
                for num_soma in range(1, 11):
                    print(f'{soma} + {num_soma} = {soma + num_soma}')
        else:
            for num_soma in range(1, 11):
                print(f'{numero} + {num_soma} = {numero + num_soma}')

# Calculadora
# %%


def calculadora(num1, num2, operador):
    operadores = ['+', '-', '/', '*']

    if operador not in operadores:
        return f'Operador ({operador}) Inválido'

    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 == 0:
            return 'Erro: Divisão por zero'
        return num1 / num2


# Tabuada de Soma
# %%
numero = int(
    input(f'Digite um numero de 1 - 10 \ne 0 para Toda Tabuada de Soma: '))
operador = input(f'Digite Operador (+) Numérico: ')

tabuada_soma(numero, operador)

# %%
# Calculadora
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operador = input('Digite o operador (+, -, *, /): ')

resultado = calculadora(num1, num2, operador)
print(f'Resultado: {resultado}')
