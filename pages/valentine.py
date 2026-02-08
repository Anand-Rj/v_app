import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="For Pari 💖",
    page_icon="💘",
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

        /* Streamlit YES button styling */
        div.stButton > button {
            background-color: #ff4b7d;
            color: white;
            border: 2px solid #ff4b7d;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            font-size: 18px;
            font-weight: 600;
            transition: all 0.2s ease-in-out;
        }

        /* Hover */
        div.stButton > button:hover {
            background-color: #ff2f6d;
            color: white;
        }

        /* Pressed state */
        div.stButton > button:active,
        div.stButton > button:focus {
            background-color: transparent !important;
            color: #111 !important;
            border: 2px solid #ff4b7d !important;
            box-shadow: none !important;
        }

        /* GIF positioning */
        .gif-overlay {
            position: fixed;
            left: 50%;
            bottom: 40px;
            transform: translateX(-50%);
            z-index: 99999;
            pointer-events: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- LOAD GIFS ----------------
wait_gif = base64.b64encode(
    Path("assets/gifs/wait.gif").read_bytes()
).decode()

angry_gif = base64.b64encode(
    Path("assets/gifs/angry.gif").read_bytes()
).decode()

# ---------------- GLOBAL GIF OVERLAYS ----------------
st.markdown(
    f"""
    <img id="waitGif"
         class="gif-overlay"
         src="data:image/gif;base64,{wait_gif}"
         width="260"/>

    <img id="angryGif"
         class="gif-overlay"
         src="data:image/gif;base64,{angry_gif}"
         width="260"
         style="display:none;"/>
    """,
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.markdown(
    """
    <div style="text-align:center;">
        <h1 style="color:#ff4b7d;">Hey Pari Baby my chottu baby 💖✨</h1>
        <h2 style="color:#333;">Will you be my Valentine cutie?</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------- BUTTONS ----------------
col1, col2 = st.columns(2)

# YES BUTTON
with col1:
    if st.button("Yes 💕"):
        st.switch_page("pages/yes.py")

# NO BUTTON (DODGING)
with col2:
    components.html(
        """
        <button id="noBtn"
            style="
                padding:10px 20px;
                font-size:16px;
                border-radius:10px;
                border:2px solid #ff4b7d;
                background:#ff4b7d;
                color:white;
                cursor:pointer;
                position:fixed;
                left:60%;
                top:55%;
                z-index:1000;
                transition: all 0.15s ease-in-out;
            ">
            No 😝
        </button>

        <script>
            const noBtn = document.getElementById("noBtn");
            const angry = window.parent.document.getElementById("angryGif");
            const wait = window.parent.document.getElementById("waitGif");

            function moveButton() {
                const maxX = window.innerWidth - noBtn.offsetWidth - 20;
                const maxY = window.innerHeight - noBtn.offsetHeight - 120;

                const x = Math.random() * maxX;
                const y = Math.random() * maxY;

                noBtn.style.left = x + "px";
                noBtn.style.top = y + "px";
            }

            function triggerAngry() {
                if (wait) wait.style.display = "none";
                if (angry) angry.style.display = "block";

                // Pressed style
                noBtn.style.background = "transparent";
                noBtn.style.color = "#111";

                moveButton();
            }

            // Desktop
            noBtn.addEventListener("mouseover", triggerAngry);

            // Mobile
            noBtn.addEventListener("touchstart", triggerAngry);
        </script>
        """,
        height=200
    )
