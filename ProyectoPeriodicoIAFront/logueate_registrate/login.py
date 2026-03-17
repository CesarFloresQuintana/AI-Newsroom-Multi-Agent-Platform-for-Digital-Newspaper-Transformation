import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Login Elegante", layout="centered")

###
def carga_registrate_css():
    with open("login_styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

carga_registrate_css()

# --- INTERFAZ DE LOGIN ---
def main():
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # para centrar el formulario
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<h1>Acceder</h1>", unsafe_allow_html=True)
        st.write("---")
        usuario = st.text_input("Usuario", placeholder="Tu correo o username")
        password = st.text_input("Contraseña", type="password", placeholder="••••••••")

        st.write("") # Espaciador

        if st.button("Iniciar Sesión"):
            if usuario == "admin" and password == "1234":
                st.success(f"¡Bienvenido, {usuario}!")
                #st.balloons()
            else:
                st.error("Credenciales incorrectas. Inténtalo de nuevo.")

        st.markdown("<p style='text-align: center; color: white; font-size: 0.8rem;'>¿Olvidaste tu contraseña?</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()