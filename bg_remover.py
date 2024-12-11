import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO


def app():
    st.markdown(
    "<h1 style='font-size: 5em;text-align: center; border: solid #2B1B3D; border-radius: 10px;'>BG Remover</h1>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    st.write(
        """	🖼️ Welcome to BG Remover.The Background Remover tool is your ultimate solution for effortlessly erasing backgrounds from images. Powered by advanced AI, it delivers precise results, even with intricate details like hair, edges, and semi-transparent objects. Whether you're a designer, marketer, or content creator, this tool helps you create professional-grade visuals in seconds. Perfect for e-commerce, social media, presentations, or personal projects—make your images stand out with clean, crisp cuts and a polished finish."""
    )

    st.write("---")

    st.write("## 📂 Choose an image  file")

    MAX_FILE_SIZE = 20 * 1024 * 1024  


    def convert_image(img):
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        return byte_im


    def fix_image(upload):
        image = Image.open(upload)
        col1.write("Original Image :camera:")
        col1.image(image)

        fixed = remove(image)
        col2.write("Fixed Image :wrench:")
        col2.image(fixed)
        st.markdown("\n")
        st.write("## 🪛 Download your fixed image")
        st.write("")
        st.write("")
        st.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")


    col1, col2 = st.columns(2)
    my_upload = st.file_uploader("", type=["png", "jpg", "jpeg"])

    st.write("---")

    if my_upload is not None:
        if my_upload.size > MAX_FILE_SIZE:
            st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
        else:
            fix_image(upload=my_upload)
