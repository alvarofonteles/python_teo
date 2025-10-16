'''
para instalar
pip install streamlit

para executar
entra na pasta do arquivo 'app_cep.py'
streamlit run .\app_cep.py
'''

# %%
import requests
import streamlit as st
import pandas as pd


cep = st.text_input('Digite seu CEP')

URL = f'https://viacep.com.br/ws/{cep}/json/'

st.title('Busca CEP')

resp = requests.get(URL)
if cep != '':
    try:
        if 'erro' not in resp.json():
            dados = pd.DataFrame([resp.json()])
            st.dataframe(dados)
        else:
            st.error('CEP não encontrado!')
    except Exception as err:
        st.error('Digite um CEP válido!')
