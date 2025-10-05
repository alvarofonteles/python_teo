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
