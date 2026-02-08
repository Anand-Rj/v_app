import streamlit as st

st.set_page_config(
    page_title="For Pari 💖",
    page_icon="💘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---- BABY PINK BACKGROUND + HIDE SIDEBAR ----
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

        /* Base button style */
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

        /* Hover (optional subtle effect) */
        div.stButton > button:hover {
            background-color: #ff2f6d;
            color: white;
        }

        /* Active / Clicked state */
        div.stButton > button:active,
        div.stButton > button:focus {
            background-color: transparent !important;
            color: black !important;
            border: 2px solid #ff4b7d !important;
            outline: none !important;
            box-shadow: none !important;
        }

        /* Remove focus ring */
        div.stButton > button:focus-visible {
            outline: none !important;
        }

        /* Center vertically */
        .main {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- CONTENT ----
st.markdown(
    """
    <div style="text-align:center;">
        <h1 style="color:#ff4b7d;">💖 Wassup my baby girl 💖</h1>
        <p style="font-size:18px; color:#444;">
            Something special is waiting for you ✨
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---- CENTERED START BUTTON ----
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("Start 💕", use_container_width=True):
        st.switch_page("pages/valentine.py")

    st.write("")  # spacing

    # ---- GIF BELOW BUTTON ----
    st.image(
        "assets/gifs/Dog.gif",
        use_container_width=True
    )