# definição de tuplas e desempacotamento
# o que são tuplas?
# tuplas são estruturas de dados semelhantes às listas, porém são imutáveis.
# tuplas são representadas por parênteses () e os elementos são separados por vírgulas.
# tuplas podem conter elementos de tipos diferentes.
# tuplas podem ser aninhadas, ou seja, uma tupla pode conter outras tuplas.

# %%
# criando uma tupla
tupla1 = (1, 2, 3, 4, 5) # tupla de inteiros
print(tupla1)
print(type(tupla1))

# %%
# criando uma tupla com elementos de tipos diferentes
tupla2 = (1, "dois", 3.0, True) # tupla com elementos de tipos diferentes
print(tupla2)

# %%
# tupla com elementos de tipos diferentes, incluindo lista e outra tupla
tupla3 = (1, "dois", 3.0, True, [1, 2, 3], (4, 5, 6)) 
print(tupla3)

tupla3[4].append(4) # adicionando um elemento na lista dentro da tupla
print(tupla3)

