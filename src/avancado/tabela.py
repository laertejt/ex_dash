import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
import os
from pathlib import Path
DATA_DIR = str(Path(os.path.dirname(__file__)).parent.parent) + '/data'
LOG_DIR = str(Path(os.path.dirname(__file__)).parent.parent) 
# Criando um DataFrame de exemplo
df = pd.read_csv(DATA_DIR +'/planilhao.csv').iloc[:,1:]


# Configurações interativas da tabela AgGrid
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True)  # Paginação automática
gb.configure_side_bar()  # Barra lateral para filtros
gb.configure_default_column(editable=True)  # Tornar células editáveis
gb.configure_grid_options(domLayout='autoSize')
gridOptions = gb.build()

# Exibindo a tabela interativa
AgGrid(
    df,
    gridOptions=gridOptions,
    height=800,         # Altura total do grid
    width='100%',       # Largura total do grid
    enable_enterprise_modules=False
)
