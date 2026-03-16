import streamlit as st
from PIL import Image
#import io
import json
from recomendaciones_json import cargar_recomendaciones

import test_modelos
from test_modelos import analizar_frigorifico, obtener_ingredientes_ingles

# Configuration of the page
st.set_page_config(
    page_title="The Fridge Survival",
    page_icon="🥗",
    layout="wide"
)

#------------------------------TITLE AND DESCRIPTION--------------------------------
st.markdown("""
<style>
@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}
.fancy-title {
    font-weight: 700;
    color: #000; /* puedes usar var(--text-primary) si defines la variable */
    line-height: 1.07;
    letter-spacing: -0.025em;
    margin-bottom: 1.25rem;
}
.fancy-title span {
    display: inline-block;
    animation: float 3s ease-in-out infinite;
}
</style>

<h1 class="fancy-title" style='text-align: center; font-size: 5rem'>
<span>📸</span> The fridge Survival. <span>🥗</span>
</h1>
<h4 class="fancy-title" style='text-align: center; font-size: 2rem;'>Upload a picture of your refrigerator and we'll suggest recipes.</h4>
<br><br><br>
""", unsafe_allow_html=True)

# -------------------------------COLUMN LAYOUT--------------------------------
col1, col2 = st.columns(2, border=True)  # Creamos dos columnas

with col1:
    # -------------------------------Subir imagen(columna 1)--------------------------------
    uploaded_file = st.file_uploader("Upload an image to get started", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file).convert("RGB")
        #centrar imagen
        c1, c2, c3 = st.columns([1, 7, 1])
        with c2:
            st.image(img, caption="Uploaded Image", width=600)

with col2:
    #cargar y mostrar los ingredientes detectados
    if 'img' in locals():  # Solo mostramos info si se subió una imagen
        with st.spinner("Detecting ingredients..."):
            resultado = analizar_frigorifico(img)

            # Verificamos si detecto ingredientes
            if resultado and obtener_ingredientes_ingles(resultado):
                st.success("Ingredients detected successfully!")
                
                # Mostrar ingredientes
                st.write("## Found ingredients:")
                ingredientes_ingles = obtener_ingredientes_ingles(resultado)
                
                response_json = {
                    "ingredients": ingredientes_ingles
                }

                #st.write(", ".join(ingredientes_ingles))
                #Dando estilo
                html_badges = ""
                for ing in ingredientes_ingles:
                    html_badges += f'<span style="display:inline-block; background-color:#d4edda; color:#000; padding:6px 12px; margin:6px; border-radius:7px; font-weight:bold;">{ing}</span>'
                
                st.markdown(html_badges, unsafe_allow_html=True)
                st.write("---")   


                # -------------------- Recomendaciones --------------------
                st.write("## Recommended recipes:")

                # 🔹 Asumiendo que tu motor de recomendación ya generó un JSON llamado 'recomendaciones.json'
                recipes = cargar_recomendaciones("recipe_suggestions.json")

                if recipes:
                    for receta in recipes:
                        st.markdown(f"### 🍽️ {receta['title']}")
                        # Mostrar instrucciones paso a paso
                        directions = json.loads(receta["directions"])  # tu JSON las guarda como string de lista
                        for idx, step in enumerate(directions, 1):
                            st.write(f"{idx}. {step}")
                        # Link a la receta original
                        st.markdown(f"[Ver receta completa]({receta['link']})")
                        # Mostrar score opcional
                        st.write(f"**Similarity score:** {receta['similarity_score']:.2f}")
                        st.write("---")
                else:
                    st.info("No hay recetas recomendadas para los ingredientes detectados.")





            else:
                st.error("No se encontro ningun ingrediente. Por favor, intenta con otra imagen.")


