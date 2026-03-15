import streamlit as st
from datetime import datetime

# ===========================
# Configuración de la página
# ===========================
st.set_page_config(
    page_title="Periódico IA",
    page_icon="📰",
    layout="wide"
)

# ===========================
# Sidebar
# ===========================
st.sidebar.title("Periódico IA - Panel")
option = st.sidebar.radio(
    "Selecciona un módulo:",
    [
        "Dashboard",
        "News Research Agent",
        "Article Generation Agent",
        "Fact Checking Agent",
        "Reader Interaction Agent",
        "Social Media Agent"
    ]
)

# ===========================
# Dashboard Principal
# ===========================
if option == "Dashboard":
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

# ===========================
# News Research Agent
# ===========================
elif option == "News Research Agent":
    st.title("🔍 News Research Agent")
    st.markdown("Panel para investigar tendencias y sugerir ideas de artículos.")

    trends = [
        "IA en educación",
        "Energías renovables",
        "Deportes locales",
        "Política regional"
    ]
    st.subheader("Tendencias del momento")
    st.write(trends)

    st.subheader("Propuesta de artículo")
    idea = st.text_input("Escribe un tema y genera una idea de artículo", "")
    if st.button("Generar idea"):
        st.success(f"Idea de artículo generada para '{idea}': 'Cómo {idea} está cambiando nuestra región'")

# ===========================
# Article Generation Agent
# ===========================
elif option == "Article Generation Agent":
    st.title("📝 Article Generation Agent")
    st.markdown("Simula la generación de artículos usando IA.")

    topic = st.text_input("Escribe el tema del artículo:", "")
    if st.button("Generar Artículo"):
        st.subheader("Artículo Generado")
        st.write(f"**Título:** {topic} en la actualidad\n")
        st.write(f"**Contenido:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                 f"Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua...")

# ===========================
# Fact Checking Agent
# ===========================
elif option == "Fact Checking Agent":
    st.title("✅ Fact Checking Agent")
    st.markdown("Ingresa información para verificar su veracidad.")

    claim = st.text_area("Escribe la afirmación a verificar:", "")
    if st.button("Verificar"):
        st.success(f"La afirmación '{claim}' ha sido verificada. Fuente confiable: ✅")

# ===========================
# Reader Interaction Agent
# ===========================
elif option == "Reader Interaction Agent":
    st.title("💬 Reader Interaction Agent")
    st.markdown("Chat simulado con lectores.")

    if 'chat' not in st.session_state:
        st.session_state.chat = []

    user_input = st.text_input("Tu mensaje:", "")
    if st.button("Enviar"):
        if user_input:
            st.session_state.chat.append({"role": "Usuario", "message": user_input})
            # Respuesta simulada
            st.session_state.chat.append({"role": "Agente", "message": f"Respuesta a: {user_input}"})

    for chat in st.session_state.chat:
        if chat["role"] == "Usuario":
            st.markdown(f"**Tú:** {chat['message']}")
        else:
            st.markdown(f"**Agente:** {chat['message']}")

# ===========================
# Social Media Agent
# ===========================
elif option == "Social Media Agent":
    st.title("📱 Social Media Agent")
    st.markdown("Simula publicaciones para redes sociales.")

    article_title = st.text_input("Título del artículo:", "")
    if st.button("Generar Post"):
        st.subheader("Post para redes")
        st.write(f"🎯 Nuevo artículo: {article_title}.\nLee más en nuestro sitio web!")
