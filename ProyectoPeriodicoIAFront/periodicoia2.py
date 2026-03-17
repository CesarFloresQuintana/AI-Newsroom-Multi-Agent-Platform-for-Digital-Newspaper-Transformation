import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Periódico IA Avanzado", page_icon="📰", layout="wide")

# ===========================
# Sidebar
# ===========================
st.sidebar.title("Periódico IA")
menu = st.sidebar.radio(
    "Selecciona sección:",
    ["Dashboard", "News Research", "Article Generation", "Fact Checking", "Reader Interaction", "Social Media"]
)

# ===========================
# Dashboard Avanzado
# ===========================
if menu == "Dashboard":
    st.title("📊 Dashboard Principal Avanzado")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Suscriptores", "1,245", "+5%")
    col2.metric("Visitas Hoy", "3,212", "-2%")
    col3.metric("Artículos Generados", "58", "+8%")
    col4.metric("Interacciones Redes", "1,102", "+12%")

    # Gráfico de tendencias
    st.subheader("📈 Tendencias de Lectores")
    data = pd.DataFrame({
        'Día': pd.date_range(start='2026-03-01', periods=10),
        'Visitas': np.random.randint(2000, 4000, size=10),
        'Interacciones': np.random.randint(500, 1500, size=10)
    })
    st.line_chart(data.set_index('Día'))

    # Artículos recientes en tarjetas
    st.subheader("📰 Artículos Recientes")
    articles = [
        {"Título": "IA en Educación", "Autor": "Laura Pérez", "Fecha": "2026-03-09", "Resumen": "Cómo la inteligencia artificial transforma la educación en la región."},
        {"Título": "Energías Renovables", "Autor": "Carlos Ruiz", "Fecha": "2026-03-08", "Resumen": "El impacto de la energía solar y eólica en la economía local."},
        {"Título": "Deportes Locales", "Autor": "Ana Gómez", "Fecha": "2026-03-07", "Resumen": "Resumen de los eventos deportivos recientes y próximos."}
    ]
    for art in articles:
        st.markdown(f"""
        <div style="border:1px solid #ddd; padding:15px; margin-bottom:10px; border-radius:5px;">
        <h4>{art['Título']}</h4>
        <p><em>{art['Autor']} | {art['Fecha']}</em></p>
        <p>{art['Resumen']}</p>
        </div>
        """, unsafe_allow_html=True)

# ===========================
# News Research Agent
# ===========================
elif menu == "News Research":
    st.title("🔍 News Research Agent")
    st.markdown("Investiga tendencias y genera ideas de artículos.")
    trends = ["IA en educación", "Energías renovables", "Deportes locales", "Política regional"]
    st.subheader("Tendencias actuales")
    st.write(trends)
    idea = st.text_input("Escribe un tema para generar idea de artículo")
    if st.button("Generar idea"):
        st.success(f"Idea generada: 'Cómo {idea} está cambiando nuestra región'")

# ===========================
# Article Generation Agent
# ===========================
elif menu == "Article Generation":
    st.title("📝 Article Generation Agent")
    topic = st.text_input("Tema del artículo")
    if st.button("Generar Artículo"):
        st.subheader(f"Artículo: {topic}")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

# ===========================
# Fact Checking Agent
# ===========================
elif menu == "Fact Checking":
    st.title("✅ Fact Checking Agent")
    claim = st.text_area("Escribe afirmación a verificar")
    if st.button("Verificar"):
        st.success(f"La afirmación '{claim}' ha sido verificada. Fuente confiable: ✅")

# ===========================
# Reader Interaction Agent
# ===========================
elif menu == "Reader Interaction":
    st.title("💬 Reader Interaction Agent")
    if 'chat' not in st.session_state:
        st.session_state.chat = []

    user_input = st.text_input("Tu mensaje:")
    if st.button("Enviar"):
        if user_input:
            st.session_state.chat.append({"role": "Usuario", "message": user_input})
            st.session_state.chat.append({"role": "Agente", "message": f"Respuesta simulada a: {user_input}"})

    for msg in st.session_state.chat:
        if msg['role'] == 'Usuario':
            st.markdown(f"**Tú:** {msg['message']}")
        else:
            st.markdown(f"**Agente:** {msg['message']}")

# ===========================
# Social Media Agent
# ===========================
elif menu == "Social Media":
    st.title("📱 Social Media Agent")
    article_title = st.text_input("Título del artículo")
    if st.button("Generar Post"):
        st.subheader("Previsualización de publicación")
        st.markdown(f"""
        <div style="border:1px solid #1DA1F2; padding:10px; border-radius:10px; background-color:#E8F5FD;">
        <strong>🎯 Nuevo artículo:</strong> {article_title}<br>
        <em>Lee más en nuestro sitio web!</em>
        </div>
        """, unsafe_allow_html=True)