import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Crear Cuenta - Premium UI", page_icon="👤", layout="centered")

def carga_login_css():
    with open("registrate_styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

carga_login_css()

# --- LÓGICA DEL FORMULARIO ---
def registro():

    # Usamos un contenedor centrado
    with st.container():
        st.markdown("<h1>Crear Cuenta Nueva</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #7D7C7C; margin-bottom: 2rem;'>Únete a nuestra comunidad hoy mismo</p>", unsafe_allow_html=True)
        nombre = st.text_input("Nombre Completo", placeholder="Ej. Juan Pérez")
        email = st.text_input("Correo Electrónico", placeholder="ejemplo@email.com")


        col_pass1, col_pass2 = st.columns(2)
        with col_pass1:
            password = st.text_input("Contraseña", type="password", placeholder="••••••••")
        with col_pass2:
            confirm_password = st.text_input("Confirmar", type="password", placeholder="••••••••")

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("Registrarme"):
            if not nombre or not email or not password:
                st.warning("Por favor, rellena todos los campos obligatorios.")
            elif password != confirm_password:
                st.error("Las contraseñas no coinciden.")
            else:
                st.success(f"¡Cuenta creada con éxito para {nombre}!")
                st.snow()

        st.markdown("""
            <div style='text-align: center; margin-top: 1.5rem;'>
                <a href='#' style='color: #7D7C7C; text-decoration: underline; font-size: 0.9rem; opacity: 0.8;'>
                    ¿Ya tienes cuenta? Inicia sesión aquí
                </a>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    registro()