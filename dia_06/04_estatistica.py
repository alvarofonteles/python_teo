# %%
def soma(a:float, b:float, c:float)->float:
    return a + b + c
    
def media(a:float, b:float, c:0.0)->float:
    return soma(a, b, c) / 3 # len(soma()) #3

valor = []    
for x in range(1, 4):
    valores = float(input(f'entre com um valor: '))
    valor.append(valores)

a = valor[0]
b = valor[1]
c = valor[2]

media = media(a, b, c)
print(f'Média: {media}')

# %%
def soma(vl)->float:
    return vl[0] + vl[1] + vl[2]
    
def media(vl)->float:
    # vl[2] = 7.0 # Caso precise alterar esse valor na lista
    return soma(vl) / len(vl)

valor = []    
for x in range(1, 4): valor.append(float(input(f'entre com um valor: ')))    

media = media(valor)
print(f'Média 2: {media}')

# %%
def soma_3(vl_2:list)->float:
    return sum(vl_2)
    
def media_3(vl_2:list)->float:
    return round(soma_3(vl_2) / len(vl_2),2)

vlr_2 = []
for x in range(1, 4): vlr_2.append(float(input(f'entre com um valor: ')))    

print(f'Média 2: {media_3(vlr_2)}')

# %%
def soma_3(a:float, b:float, *args)->float: # args = tupla ()
    vl_3 = [a, b] + list(args) # transforma em lista e junta a lista com o args | [list() # converte]
    return sum(vl_3)
    
def media_3(a:float, b:float, *args)->float:
    return round(soma_3(a, b, *args) / len(args), 2)

vlr_a = float(input(f'entre com um valor: '))
vlr_b = float(input(f'entre com um valor: '))
vlr_2: list[float] = []            

for x in range(1, 4): vlr_2.append(float(input(f'entre com um valor: ')))    

print(f'Média 2: {media_3(vlr_a, vlr_b, *vlr_2)}') # todos mais dois

# %%
