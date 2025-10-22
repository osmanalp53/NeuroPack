from PIL import Image
import streamlit as st
import os

def upload_image(save_dir="../data/images"):
    st.title("Ambalaj Görseli Yükleyici")

    uploaded_file = st.file_uploader("Bir ambalaj görseli yükleyin", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Görseli aç ve göster
        img = Image.open(uploaded_file)
        st.image(img, caption='Yüklenen Görsel', use_container_width=True)


        # Kayıt klasörü yoksa oluştur
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Görseli kaydet
        save_path = os.path.join(save_dir, uploaded_file.name)
        img.save(save_path)
        st.success(f"Görsel başarıyla kaydedildi: {save_path}")
        return save_path

    return None
# 🔽 Bu blok kritik! Tarayıcıda hiçbir şey gösterilmiyorsa eksiktir
if __name__ == "__main__":
    upload_image()