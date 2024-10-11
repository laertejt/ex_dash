from my_dataframe import get_data
dic = get_data()
grafico3 = dic["grafico3"]
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar o layout com colunas
col1, col2 = st.columns([1.5, 1])  # Aumentando a largura da primeira coluna
# Gráfico de pizza na primeira coluna (col1)
with col1:
    st.title('Medalhas do Brasil por modalidade')
    sns.set_style('darkgrid')
    # Aumentar o tamanho do gráfico
    fig, ax = plt.subplots(figsize=(16, 16))  # Tamanho ajustado
    ax.pie(grafico3['Medal'], labels=grafico3['sport'], autopct='%1.0f%%', startangle=140)
    ax.set_title('Distribuição de Medalhas por Modalidade')
    st.pyplot(fig)
# Tabela na segunda coluna (col2)
with col2:
    st.write("Tabela de medalhas por modalidade:")
    # Aumentar o tamanho da tabela
    st.dataframe(grafico3, height=900) 
