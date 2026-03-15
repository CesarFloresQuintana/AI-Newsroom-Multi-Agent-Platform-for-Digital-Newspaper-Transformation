import streamlit as st

def show():
    st.title("📊 Dashboard Principal")
    st.markdown("""
    Bienvenido al panel del periódico. Aquí puedes ver métricas simuladas
    sobre audiencia, artículos y engagement digital.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Suscriptores", "1,245", "+5%")
    col2.metric("Visitas Hoy", "3,212", "-2%")
    col3.metric("Artículos Generados", "58", "+8%")

    st.subheader("Artículos Recientes")
    st.table([
        {"Título": "Innovaciones en IA", "Autor": "Laura Pérez", "Fecha": "2026-03-09"},
        {"Título": "Economía Local", "Autor": "Carlos Ruiz", "Fecha": "2026-03-08"},
        {"Título": "Deportes Regionales", "Autor": "Ana Gómez", "Fecha": "2026-03-07"},
    ])