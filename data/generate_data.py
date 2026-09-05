import numpy as np, pandas as pd
from pathlib import Path
rng=np.random.default_rng(42)
n=3000
hazards=rng.choice(['Normal','Earthquake','Wind','Flood','Corrosion','Fatigue','Thermal'],n,p=[.35,.12,.12,.10,.10,.11,.10])
base={'Normal':0,'Earthquake':2.8,'Wind':1.7,'Flood':1.4,'Corrosion':1.1,'Fatigue':1.5,'Thermal':1.0}
vib=np.abs(rng.normal(.25,.08,n)); strain=np.abs(rng.normal(120,25,n)); temp=rng.normal(28,5,n); wind=np.abs(rng.normal(5,3,n)); water=np.abs(rng.normal(2,1,n)); corr=np.clip(rng.normal(.18,.08,n),0,1)
for i,h in enumerate(hazards):
    b=base[h]; vib[i]+=b*.55; strain[i]+=b*22; wind[i]+=b*3; water[i]+=b*1.2; corr[i]+=b*.08; temp[i]+= (2 if h=='Thermal' else 0)
risk=np.clip(18*vib+0.018*strain+4*wind+5*water+18*corr+2*np.abs(temp-28),0,100)
severity=pd.cut(risk,[-1,30,60,80,101],labels=['Low','Moderate','High','Critical'])
df=pd.DataFrame({'timestamp':pd.date_range('2026-01-01',periods=n,freq='min'),'hazard':hazards,'vibration':vib,'strain':strain,'temperature':temp,'wind_speed':wind,'water_pressure':water,'corrosion_index':corr,'risk_score':risk,'severity':severity.astype(str)})
out=Path(__file__).parent/'sample_sensor_data.csv'; df.to_csv(out,index=False); print(out)




