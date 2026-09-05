from pathlib import Path
import pandas as pd, joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data/sample_sensor_data.csv')
features=['vibration','strain','temperature','wind_speed','water_pressure','corrosion_index']
X=df[features]; y=df['hazard']
enc=LabelEncoder(); yy=enc.fit_transform(y)
Xtr,Xte,ytr,yte=train_test_split(X,yy,test_size=.2,random_state=42,stratify=yy)
model=RandomForestClassifier(n_estimators=160,max_depth=10,random_state=42,class_weight='balanced')
model.fit(Xtr,ytr)
print('Demo accuracy:',accuracy_score(yte,model.predict(Xte)))
print(classification_report(yte,model.predict(Xte),target_names=enc.classes_))
joblib.dump({'model':model,'encoder':enc,'features':features},ROOT/'models/demo_model.joblib')
