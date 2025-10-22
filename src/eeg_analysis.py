import pandas as pd

def analiz_yap(csv_yolu):
    df = pd.read_csv(csv_yolu)
    ortalama = df.iloc[:, 1:].mean()

    if ortalama.mean() > 420:
        return "Calm"
    elif ortalama.mean() > 390:
        return "Focused"
    else:
        return "Stressed"
