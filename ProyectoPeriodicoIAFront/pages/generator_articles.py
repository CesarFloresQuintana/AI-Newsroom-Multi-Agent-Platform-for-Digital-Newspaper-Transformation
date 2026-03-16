import streamlit as st

# ===========================
# Article Generation Agent
# ===========================

st.title("📝 Article Generation Agent")
st.markdown("Simula la generación de artículos usando IA.")

topic = st.text_input("Escribe el tema del artículo:", "")
if st.button("Generar Artículo"):
    st.subheader("Artículo Generado")
    st.write(f"**Título:** {topic} en la actualidad\n")
    st.write(f"**Contenido:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
             f"Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua...")