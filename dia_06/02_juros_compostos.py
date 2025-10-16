# %%
def juros_comp(aporte, taxa, anos):
    return aporte * (1 + taxa) ** anos


juros_comp(1000, 0.13, 4)

# %%


def juros_comp_2(aporte, taxa, anos):
    return aporte * (1 + taxa) ** anos


juros_comp_2(taxa=0.13, aporte=1000, anos=4)

# %%


def juros_comp_3(aporte, taxa, anos) -> float:
    return aporte * (1 + taxa) ** anos


valor = juros_comp_3(taxa=13, aporte=1000, anos=4)
print(valor)
print(type(valor))
