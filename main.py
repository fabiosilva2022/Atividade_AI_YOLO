from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
from ultralytics import YOLO
from io import BytesIO
from PIL import Image
import uvicorn
from fastapi.responses import StreamingResponse

# Inicializa o modelo YOLOv8
model = YOLO("yolov8n.pt")

# Inicializa a API FastAPI
app = FastAPI()

@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    
    # Lê a imagem enviada
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("RGB")
    image_np = np.array(image)

    # Converte para formato OpenCV (BGR)
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Executa a detecção
    results = model(image_cv)

    # Processa os resultados
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0].item()
            label = result.names[int(box.cls[0])]
            
            # Desenha a bounding box
            cv2.rectangle(image_cv, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image_cv, f"{label} {conf:.2f}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Converte a imagem processada para formato de resposta
    _, encoded_image = cv2.imencode(".jpg", image_cv)
    return StreamingResponse(BytesIO(encoded_image.tobytes()), media_type="image/jpeg")

# Endpoint raiz para verificar se a API está rodando
@app.get("/")
def home():
    return {"message": "API YOLOv8 FastAPI rodando!"}

# Para rodar a API
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
