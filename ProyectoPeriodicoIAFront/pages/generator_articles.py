# import streamlit as st

# # ===========================
# # Article Generation Agent
# # ===========================

# st.title("📝 Article Generation Agent")
# st.markdown("Simula la generación de artículos usando IA.")

# topic = st.text_input("Escribe el tema del artículo:", "")
# if st.button("Generar Artículo"):
#     st.subheader("Artículo Generado")
#     st.write(f"**Título:** {topic} en la actualidad\n")
#     st.write(f"**Contenido:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
#              f"Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua...")

import streamlit as st 
import os #Permite trabajar con archivos, rutas y variables de entorno.
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings #modelo de lenguaje (LLM) de Google (Gemini). , modelo para convertir texto en vectores.
from langchain_community.vectorstores import FAISS #Importa FAISS, que permite crear una base de datos vectorial para búsquedas semánticas.
from langchain_core.prompts import ChatPromptTemplate #Permite crear plantillas de prompts estructurados para el modelo.
from langchain_core.output_parsers import StrOutputParser #Convierte la salida del modelo en texto plano (str).
#from langchain_core.runnables import RunnablePassthrough, RunnableParallel

# --- 1. AUTENTICACIÓN ---
if os.path.exists("key.json"):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
else:
    st.error("⚠️ No se encontró el archivo key.json")

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Local Notice AI", layout="wide")
PROJECT_ID = "qwiklabs-gcp-03-ad3f242cd514"

@st.cache_resource #Define una función cacheada: Se ejecuta una vez y se reutiliza (mejora rendimiento).
def get_models():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        temperature=0.4,  
        vertexai=True,
        project=PROJECT_ID
    )
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        vertexai=True,
        project=PROJECT_ID
    )
    return llm, embeddings

def generate_article(topic, context_list):
    # --- LIMPIEZA DE DATOS (Crucial para evitar el ValueError anterior) ---
    context_list = [t.strip() for t in context_list if t.strip()]
    if not context_list:
        return "Error: No hay contexto suficiente.", ""

    llm, embeddings = get_models()
    vectorstore = FAISS.from_texts(context_list, embeddings)
    #retriever = vectorstore.as_retriever()
    # Aumentamos 'k' para que recupere más fragmentos de información y el artículo tenga "sustancia"
    retriever = vectorstore.as_retriever(search_kwargs={"k": 6})


    prompt_redaccion = ChatPromptTemplate.from_messages([
    ("system", """Eres el Redactor Jefe de un periódico digital de vanguardia. 
    Tu objetivo es transformar el CONTEXTO proporcionado en una noticia de alto impacto, veraz y actualizada.

    REGLAS CRÍTICAS DE REDACCIÓN:
    1. EXCLUSIVIDAD: Utiliza ÚNICAMENTE la información del contexto. No inventes datos, nombres o fechas.
    2. ACTUALIDAD: Identifica y destaca los eventos más recientes dentro del contexto. 
    3. CITACIÓN DE FUENTES: Siempre que menciones un dato clave, cifra o declaración, indica la fuente (ej: 'Según el informe municipal...', 'Como indica la nota de prensa...').
    4. TRANSPARENCIA: Si el usuario pide un dato que NO está en el contexto, escribe explícitamente: [Información no disponible en las fuentes actuales].
    5. ESTRUCTURA: Usa un titular SEO-friendly, una entradilla informativa y cuerpo con subtítulos.
    
    ESTILO: Profesional, neutral y directo."""),
    ("user", "CONTEXTO: {context}\n\nTEMA SUGERIDO: {question}")
    ])


    # --- FASE 2: FACT-CHECKING ---
    prompt_verificacion = ChatPromptTemplate.from_messages([
        ("system", "Eres un experto verificador de datos (Fact-checker). Compara el ARTÍCULO generado con el CONTEXTO original. "
                   "Busca discrepancias, datos inventados o nombres incorrectos."),
        ("user", "CONTEXTO ORIGINAL: {context}\n\nARTÍCULO A VERIFICAR: {article}\n\n"
                 "Enumera en una lista si hay errores o confirma que todo es correcto.")
    ])

    # Cadena de generación
    chain_redaccion = prompt_redaccion | llm | StrOutputParser()

    # Flujo RAG
    contexto_recuperado = retriever.invoke(topic)
    #contexto_recuperado = retriever.get_relevant_documents(topic)
    contexto_str = "\n".join([doc.page_content for doc in contexto_recuperado])

    # 1. Generamos el artículo
    articulo = chain_redaccion.invoke({"context": contexto_str, "question": topic})

    # 2. Verificamos el artículo
    verificacion = (prompt_verificacion | llm | StrOutputParser()).invoke({
        "context": contexto_str,
        "article": articulo
    })

    return articulo, verificacion

# --- INTERFAZ STREAMLIT ---
st.title("🗞️ Sistem Editorial")

col1, col2 = st.columns(2)
with col1:
    contexto_texto = st.text_area("Fuentes de información (una noticia por línea):", height=200)
    tema_noticia = st.text_input("Tema de la noticia:")
    
with col2:
    if st.button("Generar y Verificar"):
        if contexto_texto and tema_noticia:
            with st.spinner("Procesando..."):
                articulo, check = generate_article(tema_noticia, contexto_texto.split('\n'))
                
                st.subheader("📰 Artículo Generado")
                st.markdown(articulo)
                
                st.divider()
                
                with st.expander("🔍 Informe de Verificación de Datos"):
                    st.write(check)
        else:
            st.warning("Completa los campos.")