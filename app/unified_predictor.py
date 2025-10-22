import streamlit as st
import pandas as pd
import os
import sys
import tempfile

# src klasörünü modül yolu olarak tanıt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.combined_predict import tahmin_yap  # Bu dosyada tahmin_yap fonksiyonu olmalı

st.set_page_config(page_title="Birleşik Tahmin Paneli", layout="wide")

st.title("🧠 Birleşik Duygu ve Uyarılma Tahmin Paneli")

uploaded_file = st.file_uploader("📄 CSV dosyasını yükleyin (EEG + GSR + yüz verileri birleştirilmiş)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📊 Yüklenen Veri:")
    st.dataframe(df)

    if st.button("🧠 Tahmin Yap"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        try:
            prediction = tahmin_yap(tmp_path)
            st.success(f"📌 Tahmin Sonucu: {prediction}")
        except Exception as e:
            st.error(f"Hata oluştu: {str(e)}")
else:
    st.info("Lütfen bir .csv dosyası yükleyin.")
