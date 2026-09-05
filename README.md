# StructAI — SIU Internal Hackathon MVP

## Goal
Demonstrate the end-to-end concept:
**Sensor/CSV data → preprocessing → hazard prediction → risk severity → early warning dashboard**.

## Important honesty rule
The dataset in `data/sample_sensor_data.csv` is **synthetic demo data**. The Random Forest model is a lightweight demo model for a reliable live presentation. The CNN-LSTM architecture and GA search are included as the intended research architecture. Do **not** present demo accuracy as experimental CNN-LSTM-GA performance.

## Run
```bash
pip install -r requirements.txt
python data/generate_data.py
python models/train_demo_model.py
streamlit run dashboard_app.py
```
Open the local Streamlit URL shown in the terminal.

## Demo
1. Open dashboard.
2. Move the time-point slider.
3. Show sensor readings and predicted hazard.
4. Select an abnormal/high-risk point and show the early-warning alert.
5. Explain that the live dashboard uses a lightweight baseline for demonstration; final validation will use CNN-LSTM-GA with real/public structural datasets.
