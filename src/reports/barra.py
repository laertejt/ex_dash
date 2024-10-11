from my_dataframe import get_data
dic = get_data()
grafico = dic["grafico"]

import streamlit as st
import seaborn as sns
st.set_page_config(layout="centered")
st.title('5 maiores vencedores de medalhas nas Olimpíadas')
# seaborn Grouped barplots
sns.set_theme(style='whitegrid')
g = sns.catplot(
    data=grafico, kind='bar',
    x='NOC', y='count', hue='Medal',
    errorbar='sd', palette='dark', alpha=1, height=6
)
g.despine(left=True)
g.set_axis_labels('', 'No. de medalhas')
g.legend.set_title('')
st.pyplot(g)