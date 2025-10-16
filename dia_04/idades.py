# %%
idades = [7, 15, 42, 73, 3]

print("Idades:", idades)

idades.append(18)
print("Idades após append:", idades)  # Adiciona 18 ao final, mutável.

# %%
idades = []

while True:
    idade = int(input("Digite uma idade (0 para sair): "))
    if idade == 0:
        break
    idades.append(idade)

print("Idades finais:", idades)

media = sum(idades) / len(idades)
max_idade = max(idades)
min_idade = min(idades)
qtde = len(idades)

print(f'Média: {media} '
      f'\nMáxima: {max_idade} '
      f'\nMínima: {min_idade} '
      f'\nQuantidade: {qtde}')
