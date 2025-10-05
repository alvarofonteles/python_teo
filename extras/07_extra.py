# %%
def par_impar_3(numero:int)->str:
    return 'par' if (numero % 2) == 0 else 'impar'  
print(par_impar_3(10))
print(par_impar_3(7))

# %%
# *args = parâmetro não obrigatório
def soma_2(a:float, b:float, *args)->float: # args = tupla ()
    vl = [a, b] + list(args) # transforma em lista e junta a lista com o args | [list() # converte]
    return sum(vl)
    
def media_2(*args)->float:
    vlr_fixo = 3 # passando com argumento para o *arg da soma
    return round(soma_2(*args, vlr_fixo) / len(args), 2)

vlr_2: list[float] = []
for x in range(1, 3): vlr_2.append(float(input(f'entre com um valor: ')))    

# print(f'Média 2: {media_2(vlr_2[0], vlr_2[1])}')
print(f'Média 2: {media_2(*vlr_2)}')


# %%
def soma(a:float, b:float, *args) ->float:
    vlr = [a, b] + list(args) 
    return sum(vlr) 

vls = soma(2, 5, 7)
print(vls)

# %%
def soma(a:float, b:float, **kwargs)->float:
    vlr = [a, b] + list(kwargs.values())  # pega só os valores
    return sum(vlr)

# Agora funciona:
vls = soma(2, 5, c=7, d=10)  # 24
print(vls)

# %%
# *args → TUPLA de valores
def com_args(*args):
    print(args)  # (2, 5, 7, 10) - SÓ VALORES

com_args(2, 5, 7, 10)

# %%
# **kwargs → DICIONÁRIO chave:valor  
def com_kwargs(**kwargs):
    print(kwargs)  # {'c': 7, 'd': 10} - CHAVES E VALORES
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs.items())

com_kwargs(c=3, d=10)   

# %% Transforma em Lista
def com_kwargs_2(**kwargs):
    valores = list(kwargs.values())  # [7, 10] - LISTA
    chaves = list(kwargs.keys())     # ['c', 'd'] - LISTA  
    itens = list(kwargs.items())     # [('c', 7), ('d', 10)] - LISTA
    
    for chave, valor in kwargs.items():
        print(f"{chave} = {valor}")
    # c = 7
    # d = 10
    print(valores)
    print(chaves)
    print(itens)

com_kwargs_2(c=3, d=10)

# %%
