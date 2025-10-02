# %% Dicionários em Python
# Dicionários são estruturas de dados que armazenam pares de chave-valor.
# Eles são mutáveis e permitem acesso rápido aos valores através das chaves.
# Os dicionários são definidos usando chaves {} e os pares (chave: valor) são separados por vírgulas.

# %% Exemplo 1
# Criando um dicionário

dados_alvaro = {
    'nome': 'João',
    'idade': 42,
    'cidade': 'Curitiba',
    'nome': 'Alvaro',  # Chave duplicada, o último valor sobrescreve o anterior
    'formacao': ['Desenvolvedor', 'Analista de Software', 'Engenheiro de Dados', 
                 ['Big Data', 'Machine Learning']],
    'cargos':[{'empresa': 'Empresa A', 'cargo': 'Desenvolvedor', 'anos': 3},
              {'empresa': 'Empresa B', 'cargo': 'Analista de Software', 'anos': 5},
              {'empresa': 'Empresa C', 'cargo': 'Engenheiro de Dados', 'anos': 2}]
}

print(dados_alvaro)
print(type(dados_alvaro))

print(dados_alvaro['nome'])  # Acessando valor pela chave

# %% Exemplo 2

# exibir Engenheiro de Dados da chave formacao
print(f'''{dados_alvaro['formacao'][1]} \n'''
      f'''especializado em {dados_alvaro['formacao'][3][0]}''')

# %%

# Cargos
# ['cargos'][1]['cargo']
# o primeiro acessa o 'dicionário {}' de cargos
# o segundo acessa a 'lista []' de cargos
# o terceiro acessa o 'dicionário {}' do cargo específico
print(dados_alvaro['cargos'][1]['cargo']) # Acessando o cargo do segundo emprego

# %% Exemplo 3

dados_alvaro = {
    'nome': 'João',
    'idade': 42,
    'cidade': 'Curitiba',
    'cargos':[{'empresa': 'A', 'cargo': 'Desenvolvedor', 'anos': 3}]
}

print(dados_alvaro)

print(dados_alvaro.keys())  # Retorna as chaves do dicionário
print(dados_alvaro.values())  # Retorna os valores do dicionário
print(dados_alvaro.items())  # Retorna os pares chave-valor do dicionário

dados_alvaro['idade'] = 43 # Atualizando valor
dados_alvaro['profissao'] = 'Engenheiro de Dados'  # Adicionando nova chave-valor

dados_alvaro['cargos'] = 'teste' # Substituindo lista por string
dados_alvaro['cargos'] = [{'empresa': 'C', 'cargo': 'Desenvolvedor', 'anos': 3}] # Restaurando lista
dados_alvaro['cargos'].append({'empresa': 'D', 'cargo': 'Analista de Software', 'anos': 5}) # Adicionando novo dicionário na lista

# %% laço for para iterar sobre chaves e valores
# o i acessa as chaves do dicionário
for i in dados_alvaro:
    print(f'{i}: {dados_alvaro[i]}')

# %% laço for usando items() para iterar sobre chaves e valores

# Retorna os pares chave-valor do dicionário [('nome', 'João'), ...]
print(dados_alvaro.items()) 

for item in dados_alvaro.items():
    print(item)

# o i acessa as chaves do dicionário e o y os valores
for chave, valor in dados_alvaro.items():
    print(f'{chave}: {valor}')
# %%
