import streamlit as st
import requests
from PIL import Image
import io

# URL da API FastAPI
API_URL = "http://127.0.0.1:8000/detect/"  # Altere se estiver rodando em outro host ou porta

st.title("Detecção de Objetos utilizando o YOLOv8 🚀")
st.write("Faça upload de uma imagem para detectar objetos usando YOLO.")

# Upload de imagem
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem Original", use_container_width=True)
    
    # Envia a imagem para a API FastAPI
    with st.spinner("Detectando objetos..."):
        response = requests.post(
            API_URL, files={"file": uploaded_file.getvalue()}
        )
        
        if response.status_code == 200:
            image_bytes = io.BytesIO(response.content)
            detected_image = Image.open(image_bytes)
            st.image(detected_image, caption="Imagem Processada", use_container_width=True)
        else:
            st.error("Erro ao processar a imagem! Certifique-se de que a API está rodando.")