from fastapi import FastAPI
import joblib
from pydantic import BaseModel 
import numpy as np
from fastapi.middleware.cors import CORSMiddleware  # 👈 ADD THIS

# Load trained model
model = joblib.load("student.pkl")

# Initialize FastAPI 
app = FastAPI(
    title="Student Performance API",
    description="API for predicting student performance",
    version="1.0"
)

# 👇 ADD THIS BLOCK (CORS FIX)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow frontend requests
    allow_credentials=True,
    allow_methods=["*"],        # allow POST, OPTIONS, etc.
    allow_headers=["*"],
)

# Define Input schema
class Student(BaseModel):
    features: list[float]

# API Endpoints
@app.get("/")
def home():
    return {"message": "Model API is running 🚀"}

@app.post("/predict")
def predict(data: Student):
    X = np.array(data.features).reshape(1, -1)
    prediction = model.predict(X)
    return {
        "prediction": float(prediction[0])
    }
