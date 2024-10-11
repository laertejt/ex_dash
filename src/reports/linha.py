from my_dataframe import get_data
dic = get_data()
grafico2 = dic["grafico2"]
import streamlit as st
import matplotlib.pyplot as plt

# Gráfico de evolução de medalhas do Brasil
st.title('Evolução de Medalhas do Brasil')
# Criar a figura explicitamente para o gráfico
fig, ax = plt.subplots()
# Criar o gráfico de linha com Matplotlib
ax.plot(grafico2['Year'], grafico2['Medal'], color='red', marker='o')
ax.set_xlabel('Ano')
ax.set_ylabel('Número de Medalhas')
ax.set_title('Evolução de Medalhas do Brasil')
# Renderizar o gráfico no Streamlit
st.pyplot(fig)