import streamlit as st

# ===========================
# Reader Interaction Agent
# ===========================

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