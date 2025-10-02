# %%
# teste rapido N chaves
teste_rapido = {
    0: { 'titulo': 'Aprendendo Python','nome': 1, 'sobrenome': 2, 'idade': 3 },
    1: {'titulo': 'Aprendendo Pandas', 'nome': 4, 'sobrenome': 5, 'idade': 6 },
    2: {'cargos':[{'empresa': 'Empresa A', 'cargo': 'Desenvolvedor', 'anos': 3},
                  {'empresa': 'Empresa B', 'cargo': 'Analista de Software', 'anos': 5},
                  {'empresa': 'Empresa C', 'cargo': 'Engenheiro de Dados', 'anos': 2}]}
}

# acessando o segundo dicionario de teste_rapido nome
print(teste_rapido[1]['titulo']) # Aprendendo Pandas
print(teste_rapido[2]['cargos'][1]['cargo']) # Analista de Software
