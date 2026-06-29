from fastapi import FastAPI
import joblib
import os

app = FastAPI()

# Load the model and vectorizer from the model directory
model_path = os.path.join("model", "model.pkl")
vectorizer_path = os.path.join("model", "vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.get("/")
def read_root():
    return {"message": "Sentiment Analysis API is running"}

@app.post("/predict/")
def predict(text: str):
    # Vectorize the input
    text_vec = vectorizer.transform([text])
    # Predict
    prediction = model.predict(text_vec)
    return {"sentiment": str(prediction[0])}