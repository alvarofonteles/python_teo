# Exercício 3: Contador de Frases
# Crie um programa que leia várias frases do usuário até que ele digite uma frase vazia.
# Armazene cada frase em um dicionário, onde a chave é a frase e o valor é o número de vezes que a frase foi digitada.

# %%
dados = {}

while True:
    frase = input("Digite uma frase (ou '' para encerrar): ")
    if frase == "":
        break
    
    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

print(dados)

for frase, contador in dados.items():
    print(f"A frase '{frase}' foi digitada {contador} vezes.")

# %%

dados = {
    "Olá": 3,
    "Python é legal": 5,
    "Dicionários são úteis": 1,
    "Exercícios são importantes": 4,
    "Vamos aprender juntos": 2
}

print(dados)

itens = list(dados.items())
print(itens)   
print(itens.sort()) 

# %%
itens_ordenados = sorted(itens) # ordena por chave (frase)
print(itens_ordenados)

# %%
# Ordenando com sort()
# sort() é um método de listas que ordena a própria lista e não retorna nada.
# usando lambda para definir a chave de ordenação
itens = list(dados.items())
itens.sort(key=lambda item: item[1]) # ordena por valor (contador)
print(itens) # lista ordenada

# %%
# Ordenando com sorted()
# sorted() é uma função que cria uma nova lista ordenada a partir de qualquer iterável
itens_ordenados = sorted(dados.items()) # ordena por chave (frase)
itens_ordenados = sorted(dados.items(), key=lambda item: item[1]) # ordena por valor (contador)

print(itens_ordenados)
# %%
# Qual a diferença entre sort() e sorted()?
# sort() é um método de listas que ordena a própria lista e não retorna nada.
# sorted() é uma função que cria uma nova lista ordenada a partir de qualquer iterável
 