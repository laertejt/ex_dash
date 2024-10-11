import streamlit as st
import pandas as pd

# Exemplo de DataFrames
df1 = pd.DataFrame({
    'Nome': ['João', 'Maria', 'Pedro'],
    'Idade': [23, 34, 19]
})

df2 = pd.DataFrame({
    'Produto': ['Produto A', 'Produto B', 'Produto C'],
    'Preço': [10, 20, 30]
})

# Criando abas
tab1, tab2 = st.tabs(["DataFrame 1", "DataFrame 2"])

# Exibindo DataFrame 1 na aba 1
with tab1:
    st.write("DataFrame 1:")
    st.dataframe(df1)

# Exibindo DataFrame 2 na aba 2
with tab2:
    st.write("DataFrame 2:")
    st.dataframe(df2)
