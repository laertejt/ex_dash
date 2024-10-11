import streamlit as st
# Função que será chamada ao clicar no botão
def executar_script():
    st.write("O script foi acionado!")
    # Coloque aqui o código que você quer executar
    # Por exemplo: chamar uma função, rodar um subprocesso, etc.

# Botão para acionar o script
if st.button('Executar Script'):
    executar_script()