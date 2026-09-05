import streamlit as st, pandas as pd, requests
from pathlib import Path

ROOT = Path(__file__).parent

# 1. Page Config
st.set_page_config(page_title='StructAI | SHM 3D', layout='wide', initial_sidebar_state='collapsed')

# 2. Custom 3D & Glassmorphic CSS Injector
st.markdown("""
<style>
    /* Dark Futuristic Background */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #1e2640 0%, #0d111a 100%) !important;
        color: #e2e8f0;
    }
    
    /* Title Styling with Subtle Depth */
    h1 {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        text-shadow: 0px 10px 20px rgba(99, 102, 241, 0.3);
    }

    /* 3D Glassmorphic Metric Cards */
    div[data-testid="stMetric"] {
        background: rgba(30, 41, 59, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 16px !important;
        padding: 15px 20px !important;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5), 
                    0 8px 10px -6px rgba(0, 0, 0, 0.5),
                    inset 0 1px 1px 0 rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(12px) !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }

    /* 3D Lift Effect on Hover */
    div[data-testid="stMetric"]:hover {
        transform: translateY(-6px) rotateX(4deg) scale(1.02);
        box-shadow: 0 20px 35px -5px rgba(99, 102, 241, 0.4), 
                    0 10px 10px -5px rgba(0, 0, 0, 0.4) !important;
        border-color: rgba(168, 85, 247, 0.4) !important;
    }

    /* Metric Value Styling */
    div[data-testid="stMetricValue"] > div {
        color: #f8fafc !important;
        font-weight: 700 !important;
        text-shadow: 0 2px 8px rgba(0,0,0,0.6);
    }
    
    /* Slider Custom 3D Styling */
    .stSlider > div {
        background: rgba(30, 41, 59, 0.5);
        border-radius: 12px;
        padding: 10px 18px;
        box-shadow: inset 0 2px 6px rgba(0,0,0,0.6);
    }

    /* Divider Enhancement */
    hr {
        border-color: rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Main UI Code (Functionally Unchanged)
st.title('StructAI — Real-Time Multi-Hazard Risk Monitoring')
st.caption('Internal hackathon prototype • synthetic/demo sensor stream • not a validated field deployment')

features = ['vibration', 'strain', 'temperature', 'wind_speed', 'water_pressure', 'corrosion_index']
df = pd.read_csv(ROOT / 'data/sample_sensor_data.csv')

idx = st.slider('Select sensor time point', 0, len(df) - 1, 100)
row = df.iloc[idx]

cols = st.columns(6)
for c, f in zip(cols, features):
    c.metric(f.replace('_', ' ').title(), f'{row[f]:.2f}')

# FastAPI Backend Integration
api_url = "https://sensor-hazard-monitoring.onrender.com/predict"
payload = {f: float(row[f]) for f in features}

try:
    res = requests.post(api_url, json=payload).json()
    pred = res.get('hazard_type', 'Error')
except Exception:
    pred = 'Backend Offline'

confidence = 0.95
risk = float(row['risk_score'])
severity = 'Critical' if risk >= 80 else 'High' if risk >= 60 else 'Moderate' if risk >= 30 else 'Low'

st.divider()
a, b, c = st.columns(3)
a.metric('Detected Hazard', pred)
b.metric('Risk Level', severity)
c.metric('Demo Confidence', f'{confidence * 100:.1f}%')

if severity in ['High', 'Critical']:
    st.error(f'⚠️ EARLY WARNING: abnormal structural response detected — {pred} / {severity} risk')
else:
    st.success('✓ Structural response currently within the demo safe range')

st.subheader('Sensor Trend')
chart = df.set_index('timestamp')[['vibration', 'strain', 'wind_speed', 'water_pressure', 'corrosion_index']].tail(180)
st.line_chart(chart)

st.info('Demo note: the displayed prediction is served live from the FastAPI Machine Learning Backend service.')