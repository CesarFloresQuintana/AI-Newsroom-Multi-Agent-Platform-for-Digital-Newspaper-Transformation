import streamlit as st

# ===========================
# Social Media Agent
# ===========================

st.title("📱 Social Media Agent")
st.markdown("Simula publicaciones para redes sociales.")

article_title = st.text_input("Título del artículo:", "")
if st.button("Generar Post"):
    st.subheader("Post para redes")
    st.write(f"🎯 Nuevo artículo: {article_title}.\nLee más en nuestro sitio web!")