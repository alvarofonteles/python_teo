# %%
lista = [2, 36, 4, 57, 1, 69, 1, 36, 7, 1, 2, 45, 67, 14, 36, 4, 14, 2, 1, 0]

print(f'Lista original: {lista}')

numero = int(
    input('Digite um número para contar quantas vezes ele aparece na lista: '))

contador = 0
for i in lista:
    if i == numero:
        contador += 1

print(f'O número {numero} aparece {contador} vezes na lista.')
