import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Configuración de la página
# 'layout="wide"' aprovecha todo el ancho de la pantalla, ideal para blogs.
st.set_page_config(
    page_title="Exploraciones del Pensamiento",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Definir el nombre exacto de tu archivo HTML
# Asegúrate de que este nombre coincida EXACTAMENTE con el archivo en tu GitHub.
HTML_FILE_NAME = "BlogPostWriterRemixSaved.html"

def load_and_display_html():
    """Carga y muestra el archivo HTML local."""
    
    # Verificamos si el archivo existe en el entorno (útil para depurar en Cloud)
    if not os.path.exists(HTML_FILE_NAME):
        st.error(f"❌ Error: No se encuentra el archivo '{HTML_FILE_NAME}'.")
        st.info("Asegúrate de que el archivo HTML esté en la carpeta raíz de tu repositorio, junto a este script.")
        return

    # Leemos el contenido del archivo
    try:
        with open(HTML_FILE_NAME, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        # 3. Renderizar el HTML
        # height=1200: Una altura inicial alta para ver gran parte del blog.
        # scrolling=True: CRUCIAL para poder bajar y leer todo el contenido.
        components.html(html_content, height=1200, scrolling=True)
        
    except Exception as e:
        st.error(f"Ocurrió un error al leer el archivo: {e}")

# Ejecutamos la función
load_and_display_html()

# 4. (Opcional) Estilo CSS para ocultar la interfaz nativa de Streamlit
# Esto hace que parezca más una página web normal y menos una "app".
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    /* Eliminar el padding superior extra que pone Streamlit */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
