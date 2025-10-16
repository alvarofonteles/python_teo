# %%
# API Via CEP


import sys
import json
import requests
from tqdm import tqdm  # progress bar

# spoiller
import pandas as pd

# cep = "01001000"
# url = f"https://viacep.com.br/ws/{cep}/json/"
# response = requests.get(url=url)
# print(type(response.text))
# print(type(response.json()))
# print(response.json())

ceps = [
    '01001000',
    '13600110',
    '19060100',
    '45124514',
    '13476863',
]


dados = []
# for cep in ceps:
for cep in tqdm(ceps):  # usando a barra de progresso
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        dado = response.json()
        if 'erro' not in dado:  # verifica se o CEP existe
            dados.append(dado)

print(dados)

# %%

df = pd.DataFrame(dados)
print(df)
df.to_csv("ceps.csv", sep=';')  # salva como csv

# %%
with open("cep.json", "w") as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)  # salva com json

# %%

# %%
print(sys.executable)
