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
        .stApp {
            background-color: #ffe6f0;
        }

        [data-testid="stSidebar"],
        section[data-testid="stSidebarNav"] {
            display: none;
        }

        img {
            border-radius: 18px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TEXT ----------------
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
    "assets/photos/photo2.JPG",
    "assets/photos/photo3.JPG",
    "assets/photos/photo4.jpeg",
]

image_placeholder = st.empty()

# Number of slideshow rounds (change to 2 or 3 if you want)
ROUNDS = 1

for _ in range(ROUNDS):
    for photo in photos:
        st.balloons()  # 🎈 Balloons for EVERY photo
        image_placeholder.image(photo, use_container_width=True)
        time.sleep(2.5)

# Final photo stays
image_placeholder.image(photos[-1], use_container_width=True)
