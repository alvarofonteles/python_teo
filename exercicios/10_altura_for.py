# %%
# Programa que lê 4 alturas usando um laço de repetição e
# mostre a soma das delas.

soma = 0
cont = 4
for i in range(cont):
    altura = float(input(f'Digite a {i + 1}ª altura: '))
    soma += altura
print(f'A soma das alturas é: {soma}')
# %%
