import math
num1 = input('digite um número: ')
num1 = int(num1)  # exunto e evita redundancia

# Opção 1: Expoente fracionário (sua correção)
raiz = num1 ** (1/2)
print('01 - A raiz quadrada de', num1, 'é', raiz)

# Opção 2: Usando math.sqrt()
raiz = math.sqrt(num1)
print('02 - A raiz quadrada de', num1, 'é', raiz)

# Opção 3: Expoente 0.5
raiz = num1 ** 0.5
raiz = round(raiz, 4)  # arredondamento
print('03 - A raiz quadrada de', num1, 'é', raiz, ' >> com arredondamento')
