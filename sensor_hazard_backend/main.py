import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import SensorDataInput, PredictionOutput

# FastAPI app initialize karein
app = FastAPI(
    title="Sensor Hazard Detection API",
    description="API for predicting industrial sensor hazards using Random Forest Model",
    version="1.0.0"
)

# ----------------- CORS MIDDLEWARE ADD KAREIN -----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Frontend domain restrictions (Abhi ke liye sab allow hai)
    allow_credentials=True,
    allow_methods=["*"],            # GET, POST, OPTIONS sab allow karein
    allow_headers=["*"],            # Sabhi headers allow karein
)
# -------------------------------------------------------------

# Model Artifact Load Karein
try:
    artifact = joblib.load("demo_model.joblib")
    model = artifact["model"]
    encoder = artifact["encoder"]
    feature_names = artifact["features"]
    print("✅ Model, Encoder, aur Feature Names safaltapurvak load ho gaye hain!")
except Exception as e:
    raise RuntimeError(f"❌ demo_model.joblib load nahi ho paya: {e}")

# Root Endpoint
@app.get("/")
def read_root():
    return {"message": "Sensor Hazard Detection API active aur chal rahi hai!"}

# Prediction Endpoint
@app.post("/predict", response_model=PredictionOutput)
def predict_hazard(data: SensorDataInput):
    try:
        input_dict = data.dict()
        df_input = pd.DataFrame([input_dict])[feature_names]
        
        prediction_encoded = model.predict(df_input)
        hazard_label = encoder.inverse_transform(prediction_encoded)[0]
        
        return PredictionOutput(hazard_type=hazard_label, status="success")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction fail ho gaya: {str(e)}")