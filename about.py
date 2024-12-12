import streamlit as st

def app():
    st.markdown(
    "<h1 style='font-size: 5em;text-align: center; border: solid #2B1B3D; border-radius: 10px;'>About</h1>",
    unsafe_allow_html=True,
    )
    st.write("")
    st.write("---")
    st.write("")
    st.write("## 🛣️ BG Remover : ")
    st.write("##### The BG Remover is a powerful and intuitive tool designed to seamlessly remove or replace the background in images. Whether you're a professional graphic designer, content creator, or casual user, this app simplifies the process of isolating subjects in photos for diverse applications like social media posts, product photography, or personal projects.")
    st.write("#### 🗒️ Troubleshooting Common Issues :")
    st.write("##### 1 .Low-Quality Output ")
    st.write(" ##### Solution: Ensure the input image is of high resolution. Check export settings for the desired quality and format.")
    st.write("##### 2 .Slow Processing ")
    st.write(" ##### Solution: Reduce the image size before processing or use a device with higher specifications for smoother performance.")
    st.write("##### 3 .Background Replacement Not Appearing Properly ")
    st.write(" ##### Solution: Ensure the replacement background matches the resolution and aspect ratio of the subject for seamless blending.")
    st.write("---")
