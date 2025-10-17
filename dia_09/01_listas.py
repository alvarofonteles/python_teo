# %%
# listas nova maneira de lidar com elas

lista_1 = []
for i in range(1, 11):
    lista_1.append(i)
print(lista_1)

lista_2 = [i for i in range(11, 21)]
print(lista_2)


def pares(num):
    if num % 2 == 0:
        return True


if pares(4):
    print('Par')


def pares_2(num):
    return num % 2 == 0


print(pares_2(6))

par_impar = [pares_2(i) for i in range(1, 21)]
# print(type(par_impar))
print(par_impar)

par = [i for i in range(20, 31) if pares_2(i)]
print(f'Pares (20 até 30) -> {par}')

impar = [i for i in range(20, 31) if not pares_2(i)]
print(f'Impares (20 até 30) -> {impar}')
