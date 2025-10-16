# %% Iterando strings com for

nome = 'Alvaro Fonteles'

for letra in nome:
    print(letra)

# taboada do 3
# %%
num = 2
max = 10
for i in range(1, max + 1):
    print(f'{num} x {i} = {num * i}')

# %%
for i in range(4, 101):  # de 4 até 100
    if i % 4 == 0:
        print(f'{i} é divisível por 4')
# %%
