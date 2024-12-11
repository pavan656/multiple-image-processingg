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
    st.write("## 🌄 IMG Compressor : ")
    st.write("##### The IMG Compressor is a versatile tool designed to reduce image file sizes while maintaining optimal quality. Whether you're looking to optimize photos for websites, emails, or social media, this app helps you save storage space, reduce loading times, and ensure seamless sharing without sacrificing clarity.")
    st.write("#### 🗒️ Troubleshooting Common Issues :")
    st.write("##### 1 .File Not Compressing as Expected ")
    st.write(" ##### Solution: Ensure the input file format is supported. If issues persist, try converting the file format before compression.")
    st.write("##### 2 .Batch Compression Fails ")
    st.write(" ##### Solution: Ensure all selected files are valid and supported formats. Compress in smaller batches if handling a large number of images.")
    st.write("##### 3 .File Not Saving After Compression ")
    st.write(" ##### Solution: Ensure you have sufficient storage space and the app has proper file-saving permissions.")
    st.write("---")