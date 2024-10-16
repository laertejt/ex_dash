import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
barra = st.Page("reports/barra.py", title="Gráfico de Barra", icon=":material/bar_chart:", default=True)
linha = st.Page("reports/linha.py", title="Gráfico de Linha", icon=":material/bug_report:")
pizza = st.Page("reports/pizza.py", title="Gráfico de Pizza", icon=":material/notification_important:")
search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")
scripts = st.Page("tools/scripts.py", title="Scripts", icon=":material/history:")
avancado = st.Page("avancado/tabela.py", title="Tabela", icon=":material/history:")
if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Reports": [barra, linha, pizza],
            "Tools": [search, history, scripts],
            "Tabelas": [avancado],
        }
    )
else:
    pg = st.navigation([login_page])
pg.run()