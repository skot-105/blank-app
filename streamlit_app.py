import streamlit as st

# Page configuration
st.set_page_config(page_title="Video Annotation App", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Main page background color */
    .stApp {
        background-color: #f5f7fa;
    }

    /* Header styling */
    .header {
        background-color: #004080;
        padding: 10px;
        color: white;
        text-align: center;
    }

    /* Company logo styling */
    .logo-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px;
    }

    .logo-container img {
        height: 60px;
    }

    /* Upload button styling */
    .stButton>button {
        background-color: #004080;
        color: white;
    }

    /* Video uploader styling */
    .stFileUploader label {
        color: #004080;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
