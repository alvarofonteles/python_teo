# %%
# API Via CEP

import json
import requests

cep = "01001000"
url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url=url)
print(type(response.text))
print(type(response.json()))
print(response.json())

# %%

ceps = [
    "01001000",
    "13600110",
    "19060100",
    "45124514",
    "13476863",
]

dados = []
for cep in ceps:  # Nome mais descritivo
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        dados.append(response.json())

print(dados)


# %%

with open("cep.json", "w") as open_file:
    json.dump(dados, open_file)
