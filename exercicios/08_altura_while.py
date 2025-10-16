# %%
# Programa que lê 4 alturas usando um laço de repetição e
# mostre a soma das delas.

soma = 0
cont = 4
# while cont <= 4:
while cont > 0:
    altura = float(input(f'Digite a {cont}ª altura: '))
    soma += altura
    # cont += 1
    cont -= 1
print(f'A soma das alturas é: {soma}')
# %%
