import importlib
db = importlib.import_module('01_bom_dia')

dia = input(f'Bom dia {db.nome}! ')
print(dia)
