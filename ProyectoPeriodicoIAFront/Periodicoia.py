import streamlit as st
from pages.generator_articles import generator_articles

st.set_page_config(
    page_title="Periódic.IA",
    page_icon="📰",
    layout="wide"
)

st.markdown("""
<div style="display: flex; gap: 10px;">
  <div style="flex: 1; background-color:#f0f0f0; padding:5px; text-align:center;">
    <h1>Noticias Flash</h1>
    <h4>Sistema Automatizado de redaccion y analisis</h4>
  </div>

  <div style="flex: 1; background-color:#d0d0d0; padding:20px; text-align:center;">
    <button>Comprobar informacion</button>
    <button>Generar Ediciones expres</button>
  </div>
</div>
""", unsafe_allow_html=True)


st.title("📰 Periódic.IA")

st.markdown("""
Bienvenido al panel del periódico.

### Navegación
- 📊 Dashboard
- 🔍 News Research Agent
- 💬 Reader Interaction Agent
- 📱 Social Media Agent
- 📝 Article Generation Agent            

Usa el menú lateral para acceder a cada módulo.
""")

# -------------------------------COLUMN LAYOUT--------------------------------
col1, col2 = st.columns(2)
with col1:
    col1, col2, col3 = st.columns([1,7,1])
    with col2:
        st.image("images/logo.jpeg", use_container_width=True)
    
with col2:
    st.write("soy la primera box baja")


col11, col22 = st.columns(2, border=True)  # Creamos dos columnas
with col11:
    st.write("soy la primera box baja")

with col22:
    st.write("soy la segunda baja")


