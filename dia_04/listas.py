# %% listas assemelhas se a um molho de chaves.
# Podemos adicionar, remover e modificar elementos.
# Podemos acessar os elementos por sua posição (índice).

# Criando uma lista
idades = [7, 15, 42, 73, 3] # lista de inteiros
print(f'idades - {idades}')

alvaro = ["Alvaro", 42, True, 1.70, 
          "Eng. Dados", 8500.99] # lista heterogênea

# %%
type(alvaro)
type(idades)

# %%
print(f'tipo alvaro - {type(alvaro)}')
print(f'tipo idades - {type(idades)}')

# Acessando elementos da lista
# em Python, o index nas listas começa em 0
# já os elementos começam em 1

print(f'alvaro[0] {alvaro[0]} - é o indice 0 \ne primeiro elemento') # primeiro elemento')
print(f'alvaro[3] - {alvaro[3]} - quarto') # quarto elemento

#ultimo elemento
print(f'alvaro[-1] - {alvaro[-1]} - último') # último elemento
print(f'alvaro[-2] - {alvaro[-2]} - penúltimo') # penúltimo elemento

print(f'soma: {sum(idades)}') # soma dos elementos da lista
print(f'tamanho: {len(idades)}') # tamanho da lista, apenas para listas numéricas

# media das idades
print(f'média: {sum(idades) / len(idades)}')

print(f'máximo: {max(idades)}') # máximo das idades
print(f'mínimo: {min(idades)}') # mínimo das idades

# melhores práticas
soma = sum(idades)
tamanho = len(idades)
media = soma / tamanho
print(f'média: {media}')

# %%
nova_lista = ['Alvaro', 42, True, 1.70, 'Eng. Dados', 8500.99, 
              ['PL/SQL', 'Delphi', 'Forms', 'APEX']] 

print(f'nova_lista - {nova_lista}')
print(f'1 - stack - {nova_lista[6][3]}') # APEX

# ou simplificado dentre as opções acima
print(f'2 - stack - {nova_lista[-1][-1]}') # APEX

# %%
nova_lista = ['Alvaro', 42, True, 1.70, 'Eng. Dados', 8500.99, 
              ['PL/SQL', 'Delphi', 'Forms', 'APEX', 
               ['PySpark', 'Delta Lake', 'Databricks', 'Medallion Architecture', 'AWS Moderno (S3, Glue, EMR)']]]

print(nova_lista[6])

# %%
estudo = ['Maria', 28, False, 1.65, 'Arquiteta', 7200.50, 
         ['Maçã', 'Banana', 'Laranja', 'Uva'], 
         ['Cadeira', 'Mesa', 'Computador', 'Livro', 'Caneta']]

print(estudo[7][3:]) # ['Livro', 'Caneta']
print(estudo[-5:-3]) # [1.65, 'Arquiteta']
print(estudo[-2][:-1]) # ['Maçã', 'Banana', 'Laranja']
print(estudo[6][1:3]) # ['Banana', 'Laranja']

# %%
estudo = ['Maria', 28, False, 1.65, 'Arquiteta', 7200.50, 
          ['Maçã', 'Banana', 'Laranja', 'Uva'], 
          ['Cadeira', 'Mesa', 'Computador', 'Livro', 'Caneta', ['Azul', 'Vermelho', 'Verde']]] # 7 elementos e 3 listas

print(estudo[4]) # 'Arquiteta'
print(estudo[6][2]) # 'Laranja'
print(estudo[7][1]) # 'Mesa'
print(estudo[7][5][2]) # 'Verde'

# %%
estudo = ['Maria', 28, False, 1.65, 'Arquiteta', 7200.50, 
          ['Cadeira', 'Mesa', 'Computador', 'Livro', 'Caneta', ['Azul', 'Vermelho', 'Verde']],
          ['Maçã', 'Banana', 'Laranja', 'Uva']]

print(estudo[6][4]) # 'Caneta'
print(estudo[6][5][1]) # 'Vermelho'
print(estudo[7][1]) # 'Banana'

# %%
estudo = ['Maria', 28, False, 1.65, 'Arquiteta', 7200.50, 
          ['Cadeira', 'Mesa', 'Computador', 'Livro', 'Caneta', ['Azul', 'Vermelho', 'Verde'], ['Maçã', 'Banana', 'Laranja', 'Uva']]] # 7 elementos e 3 listas
            
print(estudo[6][5][1]) # 'Vermelho'
print(estudo[6][6][2]) # 'Laranja'

# %%