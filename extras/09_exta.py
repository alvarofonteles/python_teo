# %%
import requests

ceps = [
    '01001000',
    '13600110',
    '19060100',
    '45124514',
    '13476863',
]

dados = []
for cep in ceps:
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if response.ok and not response.json().get('erro'):
        dados.append(response.json())

print(dados)
