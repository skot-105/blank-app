import streamlit as st

st.set_page_config(page_title="Video Annotation App", layout="wide")
st.title("Video Uploader")

col1 = st.columns(1)
with col1:
    st.subheader("Upload Video")
    uploaded_video = st.file_uploader("Drag and drop a video file here or click", type=["mp4", "mov", "avi"])
    
    if uploaded_video is not None:
        st.video(uploaded_video)

if st.button('Upload'):
    st.write("Files uploaded successfully!")
