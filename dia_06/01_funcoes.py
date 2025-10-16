# Funções são blocos de código reutilizáveis que executam uma tarefa específica.
# Elas ajudam a organizar o código, tornando-o mais legível e modular.

# Definindo uma função simples que imprime uma mensagem de boas-vindas

# %%
def boas_vindas():
    print("Bem-vindo ao curso de Python!")


# Chamando a função
boas_vindas()
# Função com parâmetros


def saudacao(nome):
    print(f"Olá, {nome}! Como você está?")


# Chamando a função com um argumento
saudacao("Maria")

# Função Soma
# Na Função abaixo passa-se assinatura, existe um bloco que executa sem retorno
# e um retorno como positivo
# %%


def calc_soma(numero):
    if numero >= 10:
        return f'número {numero} inválido'

    for x in range(1, 11):
        print(f'{x} + {numero} = {x + numero}')

    return f'Parabéns, sucesso!'


# %%
valor = int(input(f'Digite um numero de 1 - 10: '))
resultado = calc_soma(valor)
print(resultado)
