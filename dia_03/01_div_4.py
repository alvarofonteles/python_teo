# %% 
# Quais numeros são divisíveis por 4
# 12 % 4 == 0 -> True (Se o resto da divisão é 0, então é divisível)

count = 0
num = 3 # número que quero saber se é divisível
while count <= 100 :
    resto = count % num
    if resto == 0:
        print(f'{count} é divisível por {num}')
    count += 1
print('Fim')
# %%
