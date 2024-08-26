Iimport streamlit as st

# Page configuration
st.set_page_config(page_title="Video Annotation App", layout="wide")

# Main Page Content
st.title("Advanced AI Check")

# Single video uploader
st.subheader("Upload Video")
uploaded_video = st.file_uploader("Drag and drop a video file here or click", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    st.video(uploaded_video)

# Upload Button
if st.button('Upload'):
    st.write("Video uploaded successfully!")
