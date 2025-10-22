import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import sys

# Argüman olarak veri yolu al
if len(sys.argv) != 2:
    print("Kullanım: python src/combined_model.py data/train_dataset.csv")
    sys.exit(1)

veri_yolu = sys.argv[1]

# CSV dosyasını oku
df = pd.read_csv(veri_yolu)

# Gerekli sütunlar kontrolü
gerekli_sutunlar = ["mean_eeg", "gsr", "face_emotion_score", "label"]
if not all(col in df.columns for col in gerekli_sutunlar):
    print(f"CSV dosyasında şu sütunlar eksik: {set(gerekli_sutunlar) - set(df.columns)}")
    sys.exit(1)

X = df[["mean_eeg", "gsr", "face_emotion_score"]]
y = df["label"]

# Modeli eğit
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Model klasörünü oluştur
os.makedirs("model", exist_ok=True)

# Kaydet
joblib.dump(model, "models/combined_model.pkl")
print("✅ Model başarıyla eğitildi ve kaydedildi.")
