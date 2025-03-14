# Atividade_AI_YOLO

## Criar e ativar o ambiente virtual

python -m venv venv
source venv/bin/activate  # Para Linux ou Mac
venv\Scripts\activate  # Para Windows

## Instalar as dependências

pip install -r requirements.txt

## Rodar a API no terminal

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

### Em caso de erro instalar o python-multipart e rodar a API novamente

pip install python-multipart

## Rodar o Streamlit novo terminal e utlilizar no navegador

streamlit run app.py
