# %%
# digita um valor e mostar a soma do saldo anterior com o valor digitado
saldo = 0
while True:  # laço infinito, só para quando der break (uma condição de parada)
    valor = float(input('Digite um valor para depósito (0 para sair): '))
    if valor == 0:
        break  # sai do laço
    saldo += valor

print(f'Seu saldo é R$ {saldo:.2f}')
# %%
