# %%
def calc_imposto(preco: float, taxa: float, **kwargs) -> float:
    """
    Calcula imposto com taxa base + taxas adicionais por estado
    
    Args:
        preco: Valor base para cálculo
        taxa: Taxa base (ex: 0.03 para 3%)
        **kwargs: Taxas adicionais por estado (ex: ce=0.02)
    
    Returns:
        Valor total do imposto
    """
    imposto = preco * taxa
    
    for taxa_adicional in kwargs.values():
        imposto += preco * taxa_adicional

    return imposto

# --- CONFIGURAÇÃO ---
UF_TAXAS = {'ce': 0.02, 'pr': 0.04, 'rn': 0.01}
VALOR_BASE = 100
TAXA_BASE = 0.03
UF_ESCOLHIDO = 'ce'

# --- CÁLCULOS ---
tx_base_perc = TAXA_BASE * 100
tx_acrescimo = UF_TAXAS[UF_ESCOLHIDO]
tx_acrescimo_perc = tx_acrescimo * 100
tx_acrescimo_total = round(sum(UF_TAXAS.values()) * 100, 2)

# Caso individual
resultado_individual = calc_imposto(VALOR_BASE, TAXA_BASE, **{UF_ESCOLHIDO: tx_acrescimo})

# Caso todos estados (soma tudo)
resultado_total = calc_imposto(VALOR_BASE, TAXA_BASE, **UF_TAXAS)

# --- RESULTADOS ---
print(f'CASO INDIVIDUAL')
print(f'Para {UF_ESCOLHIDO.upper()} -> Taxa base: {tx_base_perc}% + Acrescimo: {tx_acrescimo_perc}% = Imposto: R${resultado_individual:.2f}')

print(f'\nCASO CONSOLIDADO')  
print(f'Para Todos -> Taxa base: {tx_base_perc}% + Acrescimo: {tx_acrescimo_total}% = Imposto Total: R${resultado_total:.2f}')

print(f'\nDETALHAMENTO POR ESTADO')
for estado, taxa in UF_TAXAS.items():
    resultado_uf = calc_imposto(VALOR_BASE, TAXA_BASE, **{estado: taxa})
    print(f'{estado.upper()} -> +{taxa * 100}% = R${resultado_uf:.2f}')