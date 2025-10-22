# 🔧 src klasörünü import edilebilir hale getiriyoruz
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import tempfile
from PIL import Image
from src.eeg_analysis import analiz_yap
from src.gsr_analysis import gsr_analiz
from src.facial_analysis import ifade_analiz_yap

st.title("📍 Eye-Tracking & Biyoveri Analiz Paneli")

# ----- 1. HEATMAP -----
st.header("👁️‍🗨️ Heatmap Oluşturucu")

image_file = st.file_uploader("Ambalaj görselini yükleyin", type=["png", "jpg", "jpeg"])
csv_file = st.file_uploader("Eye-tracking CSV dosyasını yükleyin", type=["csv"])

if st.button("🔍 Heatmap Oluştur"):
    if image_file and csv_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_img:
            img_path = tmp_img.name
            img = Image.open(image_file)
            img.save(img_path)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp_csv:
            csv_path = tmp_csv.name
            tmp_csv.write(csv_file.read())

        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.strip()
        x = df["x"]
        y = df["y"]

        img_cv = cv2.imread(img_path)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        h = img_cv.shape[0]

        plt.figure(figsize=(10, 6))
        sns.kdeplot(x=x, y=h - y, cmap="Reds", fill=True, alpha=0.6, bw_adjust=0.4)
        plt.imshow(img_cv, alpha=0.4)
        plt.axis("off")

        st.subheader("🔥 Oluşturulan Isı Haritası")
        st.pyplot(plt)
    else:
        st.warning("Lütfen hem görsel hem CSV yükleyin.")

# ----- 2. EEG ANALİZİ -----
st.header("🧠 EEG Verisi ile Duygu Tahmini")

eeg_file = st.file_uploader("EEG verisi yükleyin", type=["csv"], key="eeg")

if st.button("🧠 EEG Analiz Et"):
    if eeg_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            eeg_path = tmp.name
            tmp.write(eeg_file.read())

        sonuc = analiz_yap(eeg_path)
        st.success(f"🧠 Tahmini Duygu Durumu: {sonuc}")
    else:
        st.warning("Lütfen bir EEG CSV dosyası yükleyin.")

# ----- 3. GSR ANALİZİ -----
st.header("💧 GSR Verisi ile Uyarılma Seviyesi Tahmini")

gsr_file = st.file_uploader("GSR verisi yükleyin", type=["csv"], key="gsr")

if st.button("💧 GSR Analiz Et"):
    if gsr_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            gsr_path = tmp.name
            tmp.write(gsr_file.read())

        sonuc = gsr_analiz(gsr_path)
        st.success(f"💧 Tahmini Uyarılma Seviyesi: {sonuc}")
    else:
        st.warning("Lütfen bir GSR CSV dosyası yükleyin.")

# ----- 4. YÜZ ANALİZİ (FACIAL CODING) -----
st.header("📸 Yüz İfadesiyle Duygu Analizi")

face_file = st.file_uploader("Yüz görseli yükleyin", type=["jpg", "jpeg", "png"], key="face")

if st.button("📸 Yüz Analiz Et"):
    if face_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            face_path = tmp.name
            img = Image.open(face_file)
            img.save(face_path)

        from src.facial_analysis import ifade_analiz_yap
        sonuc = ifade_analiz_yap(face_path)
        st.success(f"😀 Tahmini Duygu: {sonuc}")
    else:
        st.warning("Lütfen bir yüz görseli yükleyin.")
