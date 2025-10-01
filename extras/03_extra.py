nova_lista = ['Alvaro', 42, True, 1.70, 'Eng. Dados', 8500.99, 
              ['PL/SQL', 'Delphi', 'Forms', 'APEX']] 

print(f'nova_lista - {nova_lista}')
print(f'1 - stack - {nova_lista[6][3]}') # APEX

stack_2 = nova_lista[6] # pegando a lista de stack
print(f'2 - stack - {stack_2[3]}') # APEX

lista_3 = nova_lista[len(nova_lista) - 1] # pegando a lista de stack
print(f'3 - stack - {lista_3[len(lista_3) - 1]}') # APEX

lista_3 = nova_lista[- 1] # pegando a lista de stack
print(f'4 - stack - {lista_3[-1]}') # APEX

# ou simplificado
print(f'5 - stack - {nova_lista[-1][-1]}') # APEX

# %% 
nova_lista = ['Alvaro', 42, True, 1.70, 'Eng. Dados', 8500.99, 
              ['PySpark', 'Delta Lake', ['Batch', 'Streaming', ['Bronze', 'Silver', 'Gold', 'Data Lake'], 'Databricks']], 
              ['PL/SQL', 'Delphi', 'Forms', 'APEX']]


# Acessando 'Eng. Dados'
print(nova_lista[4])  # 'Eng. Dados'

# Acessando 'Delta Lake'
print(nova_lista[6][1])  # 'Delta Lake'

# Acessando 'Gold'
print(nova_lista[6][2][2][2])  # 'Gold'

# Acessando Databricks
print(nova_lista[6][2][3])  # 'Databricks'

# Acessando Delphi  
print(nova_lista[7][1])  # 'Delphi'


# %%
nova_lista = ['Alvaro', 42, True, 1.70, 'Eng. Dados', 8500.99, 
              ['PL/SQL', 'Delphi', 'Forms', 'APEX', 
               ['PySpark', 'Delta Lake', 'Databricks', 'Medallion Architecture', 'AWS Moderno (S3, Glue, EMR)']]]

print(f'nova_lista - {nova_lista}')

print(f'nova_lista[0:3] {nova_lista[0:3]}') # do 0 ao 2 - 3 elementos
print(f'nova_lista[3:] {nova_lista[3:]}') # do 3 até o final - 3 elementos
print(f'nova_lista[:3] {nova_lista[:3]}') # do início até o 2 - 3 elementos
print(f'nova_lista[1:5] {nova_lista[1:5]}') # do 1 ao 4 - 4 elementos
print(f'nova_lista[1:-1] {nova_lista[1:-1]}') # do 1 ao penúltimo - 5 elementos
print(f'nova_lista[-3:-1] {nova_lista[-3:-1]}') # do antepenúltimo ao penúltimo - 2 elementos
print(f'nova_lista[-3:] {nova_lista[-3:]}') # do antepenúltimo até o final - 3 elementos
print(f'nova_lista[:-3] {nova_lista[:-3]}') # do início até o antepenúltimo - 4 elementos
print(f'nova_lista[::2] {nova_lista[::2]}') # do início ao final, pulando de 2 em 2 - 4 elementos
print(f'nova_lista[1::2] {nova_lista[1::2]}') # do 1 ao final, pulando de 2 em 2 - 3 elementos
print(f'nova_lista[::-1] {nova_lista[::-1]}') # do final ao início, invertendo a lista - 7 elementos
print(f'nova_lista[-1::-1] {nova_lista[-1::-1]}') # do final ao início, invertendo a lista - 7 elementos
print(f'nova_lista[-1:0:-1] {nova_lista[-1:0:-1]}') # do final ao 1, invertendo a lista - 6 elementos
print(f'nova_lista[-1:1:-1] {nova_lista[-1:1:-1]}') # do final ao 2, invertendo a lista - 5 elementos
print(f'nova_lista[-1:2:-1] {nova_lista[-1:2:-1]}') # do final ao 3, invertendo a lista - 4 elementos


# %%
nova_lista = ['Alvaro', 42, True, 1.70, 'Eng. Dados', 8500.99, 
              ['PySpark', 'Delta Lake', ['Batch', 'Streaming', ['Bronze', 'Silver', 'Gold', 'Data Lake'], 'Databricks']], 
              ['PL/SQL', 'Delphi', 'Forms', 'APEX']]


# Acessando 'Eng. Dados'
print(nova_lista[4])  # 'Eng. Dados'

# Acessando 'Delta Lake'
print(nova_lista[6][1])  # 'Delta Lake'

# Acessando 'Gold'
print(nova_lista[6][2][2][2])  # 'Gold'

# Acessando Databricks
print(nova_lista[6][2][3])  # 'Databricks'

# Acessando Delphi  
print(nova_lista[7][1])  # 'Delphi'