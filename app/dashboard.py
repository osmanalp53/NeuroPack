import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from PIL import Image
import tempfile

from src.eeg_analysis import analiz_yap
from src.gsr_analysis import gsr_analiz
from src.facial_analysis import ifade_analiz_yap

st.set_page_config(page_title="Analiz Dashboard", layout="wide")
st.title("📊 Bütünsel Biyoveri Analiz Paneli")

col1, col2 = st.columns(2)

# 🔴 1. Eye-Tracking + Heatmap
with col1:
    st.subheader("👁️ Eye-Tracking Isı Haritası")
    image_file = st.file_uploader("Ambalaj görseli", type=["png", "jpg", "jpeg"], key="heatmap_img")
    csv_file = st.file_uploader("Eye-tracking CSV", type=["csv"], key="heatmap_csv")

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

        plt.figure(figsize=(8, 5))
        sns.kdeplot(x=x, y=h - y, cmap="Reds", fill=True, alpha=0.6, bw_adjust=0.4)
        plt.imshow(img_cv, alpha=0.4)
        plt.axis("off")
        st.pyplot(plt)

# 🧠 2. EEG Analizi
with col2:
    st.subheader("🧠 EEG Verisi ile Duygu Analizi")
    eeg_file = st.file_uploader("EEG CSV", type=["csv"], key="eeg_dashboard")
    if eeg_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            eeg_path = tmp.name
            tmp.write(eeg_file.read())
        sonuc = analiz_yap(eeg_path)
        st.success(f"🧠 EEG Analiz Sonucu: {sonuc}")

# 💧 3. GSR Analizi
st.subheader("💧 GSR ile Uyarılma Seviyesi")
gsr_file = st.file_uploader("GSR CSV", type=["csv"], key="gsr_dashboard")
if gsr_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        gsr_path = tmp.name
        tmp.write(gsr_file.read())
    sonuc = gsr_analiz(gsr_path)
    st.success(f"💧 GSR Sonucu: {sonuc}")

# 📸 4. Yüz İfadesi Analizi
st.subheader("📸 Yüz İfadesiyle Duygu Analizi")
face_file = st.file_uploader("Yüz görseli", type=["jpg", "jpeg", "png"], key="face_dashboard")

if face_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        face_path = tmp.name
        img = Image.open(face_file)
        img.save(face_path)
    sonuc = ifade_analiz_yap(face_path)
    st.image(face_file, caption="Yüz Görseli", width=200)
    st.success(f"😀 Tahmini Duygu: {sonuc}")
