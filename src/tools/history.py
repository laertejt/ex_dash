import streamlit as st
import pandas as pd

# Exemplo de DataFrame
df = pd.DataFrame({
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
    'Idade': [23, 34, 19, 22, 40],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'São Paulo', 'Curitiba']
})

# Filtrar por múltiplas cidades
cidades_selecionadas = st.multiselect("Selecione as Cidades", df['Cidade'].unique())

# Filtrar por faixa etária
idade_min, idade_max = st.slider("Selecione a Faixa Etária", int(df['Idade'].min()), int(df['Idade'].max()), (20, 35))

# Aplicando os filtros
df_filtrado = df[(df['Cidade'].isin(cidades_selecionadas)) & (df['Idade'].between(idade_min, idade_max))]

# Exibindo o DataFrame filtrado
st.dataframe(df_filtrado)
