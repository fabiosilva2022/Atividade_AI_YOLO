# Atividade_AI_YOLO

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
