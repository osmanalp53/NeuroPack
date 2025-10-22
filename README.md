# 🤖 Neuropack: AI-Powered Neuromarketing Project

## Project Overview
Neuropack is an **AI-powered neuromarketing analysis dashboard** that enables users to analyze multiple biometric signals and obtain combined emotion and arousal predictions from a single platform. Supported modalities include eye-tracking data, EEG signals, GSR (Galvanic Skin Response), and facial expressions. The platform integrates these signals to provide a holistic understanding of user emotional and cognitive states.

## Features

### 1️⃣ Eye-Tracking Heatmap
Visualize gaze distribution over images such as product packaging or advertisements. Heatmaps are generated using uploaded CSV coordinates and overlaid on the original image. Users can identify which areas attract more attention.

### 2️⃣ EEG Analysis
Predict emotional states based on EEG signals. Output classes include: `Calm`, `Focused`, `Stressed`. This module helps to understand cognitive engagement and emotional responses during stimuli exposure.

### 3️⃣ GSR Analysis
Estimate arousal levels from galvanic skin response. Output classes: `Low`, `Medium`, `High`. This provides insights into physiological arousal and stress levels.

### 4️⃣ Facial Expression Analysis
Analyze facial images using **DeepFace** to detect dominant emotions. Example outputs: `Happy`, `Sad`, `Angry`, `Surprised`. This module complements EEG and GSR data to provide a more complete emotional profile.

### 5️⃣ Unified Prediction Panel
Combine EEG, GSR, and facial features to predict overall emotional and arousal states using a **Random Forest** model. This produces a single, interpretable output for integrated neuromarketing insights.

## Installation

```bash
# Clone the repository
git clone https://github.com/osmanalp53/neuropack.git
cd neuropack

# Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Train the combined model
python src/combined_model.py data/train_dataset.csv

# Launch Streamlit app
streamlit run app.py
neuropack/

Project Structure
│
├─ src/
│   ├─ eeg_analysis.py       # EEG analysis
│   ├─ gsr_analysis.py       # GSR analysis
│   ├─ facial_analysis.py    # Facial expression analysis
│   ├─ combined_model.py     # Random Forest training
│   └─ combined_predict.py   # Unified prediction function
│
├─ data/
│   ├─ images/               # Images for eye-tracking and face
│   └─ eyetracking/          # Eye-tracking CSV files
│
├─ model/
│   └─ combined_model.pkl    # Trained model
│
├─ app.py                    # Main Streamlit app
└─ requirements.txt          # Python dependencies
 
Notes

Required CSV columns: mean_eeg, gsr, face_emotion_score, label

Image formats: jpg, jpeg, png

Unified prediction requires a single CSV combining all features
 
---

# 🤖 Neuropack: AI ile Nöropazarlama Projesi

## Proje Hakkında
Neuropack, bir **yapay zeka destekli nöropazarlama analiz panelidir**. Kullanıcılar tek bir platform üzerinden birden fazla biyoveri sinyali analiz edebilir ve **birleşik duygu ve uyarılma tahminleri** alabilir. Desteklenen veri türleri eye-tracking (göz hareketi verileri), EEG (beyin dalgaları), GSR (deri iletkenliği) ve yüz ifadeleridir. Tüm bu veriler birleştirilerek kullanıcıların duygusal ve bilişsel durumları bütünsel şekilde analiz edilir.

## Özellikler

### 1️⃣ Eye-Tracking Isı Haritası
Ambalaj veya reklam görselleri üzerinde kullanıcı bakış dağılımını görselleştirir. CSV koordinat verileri ile ısı haritaları oluşturulur ve orijinal görsel üzerine bindirilir. Kullanıcılar hangi alanların daha fazla dikkat çektiğini görebilir.

### 2️⃣ EEG Analizi
EEG verileri kullanılarak duygusal durumu tahmin eder. Çıktı sınıfları: `Calm`, `Focused`, `Stressed`. Bu modül, uyarana verilen bilişsel ve duygusal tepkileri anlamaya yardımcı olur.

### 3️⃣ GSR Analizi
Galvanik deri tepkisi kullanılarak uyarılma seviyesi tahmin edilir. Çıktı sınıfları: `Düşük`, `Orta`, `Yüksek`. Bu modül, fizyolojik uyarılma ve stres seviyeleri hakkında bilgi verir.

### 4️⃣ Yüz İfadesi Analizi
**DeepFace** kütüphanesi kullanılarak yüz görsellerinden baskın duygu analizi yapılır. Örnek çıktılar: `Mutlu`, `Üzgün`, `Kızgın`, `Şaşkın`. Bu modül EEG ve GSR verilerini tamamlayarak daha eksiksiz bir duygusal profil sunar.

### 5️⃣ Birleşik Tahmin Paneli
EEG, GSR ve yüz verilerini birleştirerek genel duygu ve uyarılma durumu **Random Forest** modeli ile tahmin edilir. Bu sayede tek ve yorumlanabilir bir çıktı elde edilir.

## Kurulum

```bash
# Depoyu klonlayın
git clone https://github.com/osmanalp53/neuropack.git
cd neuropack

# Sanal ortam oluşturup bağımlılıkları yükleyin
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Modeli eğitin
python src/combined_model.py data/train_dataset.csv

# Streamlit arayüzünü başlatın
streamlit run app.py
****
