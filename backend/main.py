from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import logging


logging.basicConfig(level=logging.DEBUG)

app = FastAPI()


origins = [
    "http://localhost:3000", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  # 
)


model_path = "./model/potato_disease_model.keras"


try:
    MODEL = tf.keras.models.load_model(model_path)
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    MODEL = None

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

def read_file_as_image(data) -> np.ndarray:
    try:
        image = Image.open(BytesIO(data)).convert("RGB")  
        logging.debug(f"Image size: {image.size}")
        return np.array(image)
    except Exception as e:
        logging.error("Error reading image file: %s", str(e))
        raise ValueError("Invalid image data")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if MODEL is None:
        return {"error": "Model is not loaded properly."}

    try:
        image_data = await file.read()
        image = read_file_as_image(image_data)
        img_batch = np.expand_dims(image, 0)

        logging.debug(f"Image batch shape: {img_batch.shape}")
        
      
        predictions = MODEL.predict(img_batch)
        logging.debug(f"Predictions: {predictions}")

        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])
        
        return {
            'class': predicted_class,
            'confidence': float(confidence)
        }
    except Exception as e:
        logging.error("Error during prediction: %s", str(e))
        return {"error": "An error occurred while processing the image."}

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
