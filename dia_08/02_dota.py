# %%
import requests
import pandas as pd

url = 'https://api.opendota.com/api/heroes'

resp = requests.get(url)
print(resp.json())

df = pd.DataFrame(resp.json())
print(df)


df.to_csv('dota.csv', sep=';', index=False)
