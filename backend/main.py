from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib


# Create FastAPI application
app = FastAPI()


# Allow frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load the trained model
model = joblib.load("model.pkl")

# Load the TF-IDF vectorizer
vectorizer = joblib.load("vectorizer.pkl")


# Test route
@app.get("/")
def home():
    return {"message": "Sentiment Analysis API is running!"}


# Define the format of incoming data
class TextInput(BaseModel):
    text: str


# Prediction endpoint
@app.post("/predict")
def predict_sentiment(data: TextInput):

    # Convert input text into TF-IDF features
    text_vector = vectorizer.transform([data.text])

    # Predict sentiment
    prediction = model.predict(text_vector)[0]

    # Return prediction
    return {
        "text": data.text,
        "sentiment": prediction
    }