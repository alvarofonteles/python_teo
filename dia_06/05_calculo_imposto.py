# %%
def calc_imposto(preco:float, taxa_acre:float, **kwargs)->float:
    imposto = preco * taxa_acre
    
    for uf, uf_taxa in kwargs.items():
        print(uf, uf_taxa)
        imposto += preco * uf_taxa

    return imposto
    
# ---
impostos = {'ce': 0.01, 'pr': 0.005, 'rn': 0.001}

print(f'Com KwArgs - {calc_imposto(100, 0.03, **impostos, internacional=000.2)}')
print(f'Sem KwArgs - {calc_imposto(100, 0.03, ce=0.01, pr=0.005, rn=0.001)}')

# %%
