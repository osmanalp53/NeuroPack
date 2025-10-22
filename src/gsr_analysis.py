import pandas as pd

def gsr_analiz(csv_path):
    df = pd.read_csv(csv_path)
    arousal = df['arousal'].mean()

    if arousal > 0.7:
        return "Yüksek Uyarılma"
    elif arousal > 0.4:
        return "Orta Uyarılma"
    else:
        return "Düşük Uyarılma"
