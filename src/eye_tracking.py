import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import os

def heatmap_uret(csv_dosyasi, gorsel_dosyasi, kayit_yolu="outputs/heatmap.png"):
    # CSV dosyasını oku
    df = pd.read_csv(csv_dosyasi)
    print("👉 Sütunlar:", df.columns.tolist())  # Bunu ekle!

    df.columns = df.columns.str.strip()  # <- Bu satır kritik!
    x = df["x"]
    y = df["y"]

    # Görseli oku
    img = cv2.imread(gorsel_dosyasi)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    yukseklik = img.shape[0]

    # Grafik oluştur
    plt.figure(figsize=(10, 6))
    sns.kdeplot(x=x, y=yukseklik - y, cmap="Reds", fill=True, alpha=0.5)
    plt.imshow(img, alpha=0.4)
    plt.axis("off")

    # Klasör yoksa oluştur
    if not os.path.exists(os.path.dirname(kayit_yolu)):
        os.makedirs(os.path.dirname(kayit_yolu))

    # Dosyayı kaydet
    plt.savefig(kayit_yolu)
    plt.close()
    print("✅ Heatmap oluşturuldu:", kayit_yolu)

# Ana program
if __name__ == "__main__":
    heatmap_uret(
        csv_dosyasi="data/eyetracking/sample.csv",
        gorsel_dosyasi="data/images/ornek_gorsel.png"
    )
