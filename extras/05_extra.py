# %%
# Revisando ordenação de listas

dados = {
    "Olá": 3,
    "Python é legal": 5,
    "Dicionários são úteis": 1,
    "Exercícios são importantes": 4,
    "Vamos aprender juntos": 2
}

itens2 = list(dados.items())
print(itens2)
itens2.sort(key=lambda item: item[1], reverse=True) # ordena por valor (contador) decrescente

# como comentar várias linhas de código no VSCode?
# selecione as linhas e use o atalho Ctrl + K + C (Windows) ou Cmd + K + C (Mac)
# para descomentar, use Ctrl + K + U (Windows) ou Cmd + K + U (Mac)

# for frase, contador in itens2:
#     print(f'{frase} : {contador} vezes.')

print(itens2)   