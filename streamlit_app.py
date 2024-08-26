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
        color: black;
        font-weight: bold;
    }

    /* Subheader and other text styling */
    .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header with logos
st.markdown(
    """
    <div class="header">
        <h1>Video Uploader</h1>
    </div>""",
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
