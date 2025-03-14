# Atividade_AI_YOLO
* Atividade da Disciplina de IA 
- Docente: José Lucas Brandão.
- Discente: Fabio Silva.

## Objetivo: 

Desenvolver uma API utilizando o FastAPI que seja capaz de receber imagens, processá-las utilizando o modelo YOLO para detecção de objetos e retornar as imagens com as detecções destacadas, realizando a exibição realizada no Streamlit.

## Criar e ativar o ambiente virtual

python -m venv venv

### Ativar o ambiente virtual

* source venv/bin/activate  - Para Linux ou Mac

* venv\Scripts\activate  - Para Windows

### Instalar as dependências

pip install -r requirements.txt

### Rodar a API no terminal

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

## Visualizar no Swagger - navegador

* Abra no navegador: http://127.0.0.1:8000/docs

* Use o /detect/ para carregar uma imagem e ver os resultados

## Rodar o Streamlit 

### Em novo terminal - utlilizar no navegador

streamlit run app.py
