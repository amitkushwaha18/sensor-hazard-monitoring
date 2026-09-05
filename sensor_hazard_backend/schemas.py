from pydantic import BaseModel, Field

# Frontend se aane wale sensor values ka structure
class SensorDataInput(BaseModel):
    vibration: float = Field(..., description="Vibration level", example=0.45)
    strain: float = Field(..., description="Mechanical strain", example=120.5)
    temperature: float = Field(..., description="Temperature value", example=75.2)
    wind_speed: float = Field(..., description="Wind speed", example=15.0)
    water_pressure: float = Field(..., description="Water pressure", example=101.3)
    corrosion_index: float = Field(..., description="Corrosion level", example=0.12)

# Model prediction hone ke baad API se aane wala output structure
class PredictionOutput(BaseModel):
    hazard_type: str = Field(..., example="Overpressure")
    status: str = Field(default="success", example="success")