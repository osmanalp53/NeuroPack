from deepface import DeepFace

def ifade_analiz_yap(image_path):
    try:
        result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=True)
        emotion = result[0]['dominant_emotion']
        return emotion.capitalize()
    except Exception as e:
        return f"Analiz başarısız: {str(e)}"
