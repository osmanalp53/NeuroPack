import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Eğitimde kullanılan model dosyasını yükle (daha önce oluşturulmuş olmalı)
MODEL_PATH = "model/combined_model.pkl"

def tahmin_yap(csv_path):
    # CSV'den veri oku
    df = pd.read_csv(csv_path)

    # Eğitimde kullanılan aynı özellikleri kullan (örnek: 'mean_eeg', 'gsr', 'face_emotion_score')
    if not all(col in df.columns for col in ["mean_eeg", "gsr", "face_emotion_score"]):
        raise ValueError("CSV dosyasında gerekli sütunlar yok. 'mean_eeg', 'gsr', 'face_emotion_score' gerekli.")

    # Modeli yükle
    model = joblib.load(MODEL_PATH)

    # Tahmin yap
    X = df[["mean_eeg", "gsr", "face_emotion_score"]]
    y_pred = model.predict(X)

    return y_pred[0]
