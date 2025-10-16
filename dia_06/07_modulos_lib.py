'''
# 🏭 Importar a FÁBRICA inteira
import fabrica_ferramentas as ff
martelo = ff.martelo()
chave = ff.chave_philips()

# 🔧 Importar só as FERRAMENTAS que preciso  
from fabrica_ferramentas import martelo, chave_philips
martelo = martelo()  # Direto, sem prefixo
chave = chave_philips()
'''

# %%
# BOM para funções muito usadas
# Se só quer datas:
from math import pi, e, sqrt
import math as mt
import datetime as dt
from datetime import date, datetime, timedelta
hoje_1 = date.today()  # Mais limpo que datetime.date.today()
agora_1 = datetime.now()
diferenca_1 = timedelta(days=7)
print(hoje_1)
print(agora_1)
print(diferenca_1)

print('')
# e/ou
#
# IDEAL (padrão mercado)
hoje_2 = dt.date.today()  # Limpo e consistente
agora_2 = dt.datetime.now()
diferenca_2 = dt.timedelta(days=7)
print(hoje_2)
print(agora_2)
print(diferenca_2)

# %%
print(mt.sqrt(9))
print(mt.pi)
print(mt.e)

# %%
print(sqrt(9))
print(pi)
print(e)
