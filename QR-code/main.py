import streamlit as st
import qrcode
from PIL import Image
import io
import cv2
import numpy as np

# Page Config
st.set_page_config(page_title="QR Code Encoder & Decoder", page_icon="📱")

st.title("📱 QR Code Encoder & Decoder 🔄")

# Tabs for Encoding & Decoding
tab1, tab2 = st.tabs(["Generate QR Code", "Decode QR Code"])

# QR Code Generator
with tab1:
    st.header("Generate QR Code 🖨️")
    qr_text = st.text_input("Enter text or URL for QR Code:")

    if st.button("Generate QR Code"):
        if qr_text:
            qr = qrcode.make(qr_text)  # Generate QR Code

            # Convert QR Code to Bytes
            img_bytes = io.BytesIO()
            qr.save(img_bytes, format="PNG")
            img_bytes.seek(0)

            st.image(img_bytes, caption="Generated QR Code")  # Show QR Code
            st.download_button("Download QR Code", img_bytes, "qr_code.png", "image/png")
        else:
            st.warning("⚠️ Please enter some text to generate a QR Code.")

# QR Code Decoder
with tab2:
    st.header("Decode QR Code 📸")
    uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

        detector = cv2.QRCodeDetector()
        decoded_text, _, _ = detector.detectAndDecode(gray)

        if decoded_text:
            st.success(f"✅ Decoded Text: {decoded_text}")
        else:
            st.error("❌ No QR code detected. Try another image!")

st.markdown("---")
st.write("Made with ❤️ using **Streamlit & OpenCV**")
