import streamlit as st

st.set_page_config(
    page_title="For Pari 💖",
    page_icon="💘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide sidebar globally
st.markdown(
    """
    <style>
        [data-testid="stSidebar"],
        section[data-testid="stSidebarNav"] {
            display: none;
        }
        .stApp {
            pointer-events: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h2 style='text-align:center;'>💖 Welcome Pari 💖</h2>",
    unsafe_allow_html=True
)
