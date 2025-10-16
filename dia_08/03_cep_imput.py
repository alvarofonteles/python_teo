# %%
import requests

cep = int(input(f'Digite seu CEP: '))

url = f'https://viacep.com.br/ws/{cep}/json/'

dados = dict()
resp = requests.get(url)

if resp.ok and 'erro' not in resp.json():
    dados = resp.json()
    print(f'Seu CEP [{cep}], trouxe esse Json: {resp.json()}')
else:
    print(f'CEP Inválido')

for chave, valor in dados.items():
    print(f'{chave} -> {valor}')
