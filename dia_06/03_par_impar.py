# %%
def par_impar(numero: int) -> str:
    if (numero % 2) == 0:
        return 'par'
    else:
        return 'impar'


numero = int(input(f'Digite um número: '))
resultado = par_impar(numero)
print(f'O valor {numero} é {resultado}')
print(type(resultado))
