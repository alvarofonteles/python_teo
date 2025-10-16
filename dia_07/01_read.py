# %%
# Abertura e Leitura de um arquivo já existente e com Texto/Conteúdo.
import csv


nome_caminho_arquivo = 'arquivo.txt'

# primeira abordagem
arquivo = open(nome_caminho_arquivo)

conteudo = arquivo.read()
print(conteudo)

arquivo.close()

# %%
# segunda abordagem (mais usual)
nome_caminho_arquivo = 'arquivo.txt'

with open(nome_caminho_arquivo) as abrir_arquivo:
    leitura = abrir_arquivo.read()

print(leitura)

# %%
# Criação e Escrita de um novo arquivo, e com um novo Texto
txt = 'Tem interece, Ele te ama muito?\n'
nome_caminho_arquivo = 'arquivo_2.txt'

# 'w' sobre escreve e 'a' adiciona txt no ja existente
with open(nome_caminho_arquivo, 'a') as abrir_arquivo:

    exibir = abrir_arquivo.write(txt)

with open(nome_caminho_arquivo) as abrir_arquivo:
    leitura = abrir_arquivo.read()

print(leitura)

# %%
file = 'data.csv'

with open(file=file) as open_file:
    data = open_file.read()

print(data)

# %% varrendo as linhas de um csv
file = 'data.csv'
with open(file=file) as open_file:
    linhas = open_file.readlines()  # lista de linhas
print(data)
dados = dict()  # dicionário vazio
chaves_1 = linhas[0].strip('\n').split(';')  # lista de chaves
print(chaves_1)

for c in chaves_1:
    dados[c] = []

# %%
for l in linhas[1:]:
    valores_1 = l.strip('\n').split(';')  # lista de valores
    for i in range(len(valores_1)):
        dados[chaves_1[i]].append(valores_1[i])
print(dados)
