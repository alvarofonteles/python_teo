# %% Exercício 2: Dicionário de Preços de Frutas
# Crie um dicionário que mapeia nomes de frutas para seus preços.

fruta = input("Digite o nome de uma fruta: ")

frutas = {
    "banana": 2.5,
    "maçã": 3.0,
    "laranja": 1.8,
    "uva": 4.0
}

print(frutas[fruta])

# %% # Modifique o código para lidar com frutas que não estão no dicionário.
# Se a fruta não estiver no dicionário, imprima uma mensagem informando que o preço não está disponível.
fruta = input("Digite o nome de uma fruta: ")
if fruta in frutas:
    print(f"O preço da {fruta} é R$ {frutas[fruta]:.2f}")
else:
    print(f"Desculpe, não temos o preço da fruta '{fruta}'.")

# %% # Imprimindo todos os preços das frutas
# Use um loop para imprimir todas as frutas e seus preços formatados.
print("Lista de preços das frutas:")
for fruta, preco in frutas.items():
    print(f"A fruta {fruta} custa R$ {preco:.2f}")
# %%
