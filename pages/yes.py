import streamlit as st
import time

st.set_page_config(
    page_title="She Said YES 💖",
    page_icon="🎉",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- GLOBAL STYLES ----------------
st.markdown(
    """
    <style>
        /* Baby pink background */
        .stApp {
            background-color: #ffe6f0;
        }

        /* Hide sidebar */
        [data-testid="stSidebar"],
        section[data-testid="stSidebarNav"] {
            display: none;
        }

        /* Image styling */
        img {
            border-radius: 18px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- CELEBRATION ----------------
st.balloons()

st.markdown(
    """
    <div style="text-align:center; color:#ff4b7d;">
        <h1>YAY!! 💕🎉</h1>
        <h2>I knew it 😘</h2>
        <h2>I’m so lucky to have you, Pari 💖</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ---------------- SLIDESHOW ----------------
photos = [
    "assets/photos/photo1.jpg",
    "assets/photos/photo2.jpg",
    "assets/photos/photo3.jpg",
    "assets/photos/photo4.jpeg",
]

if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

image_placeholder = st.empty()

# Show current image
image_placeholder.image(
    photos[st.session_state.slide_index],
    use_container_width=True
)

# Wait before next slide
time.sleep(2.5)

# Move to next image (loop infinitely)
st.session_state.slide_index = (
    st.session_state.slide_index + 1
) % len(photos)

# Rerun app to simulate infinite slideshow
st.rerun()

