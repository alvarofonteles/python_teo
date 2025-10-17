# %%
a = 1
b = 2

print('origem')
print(a)
print(b)

# %%
c = a
a = b
b = c

print('primeira tentativa')
print(a)
print(b)

# %%
a, b = b, a  # unpack

print('Unpack')
print(a)
print(b)

# %%
# tupla

novo = a, b
print(novo)

a, b = 'teo', [1, 2, 3]
print(a, b)

a, b, *resto = 'teo', [1, 2, 3], 125, 254, 365, 587, 14
print(a, b, resto)


def soma(a, *args):
    return a + sum(args)


values = [1, 2, 3, 4]
print(soma(*values))
