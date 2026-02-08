import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="For Pari 💖",
    page_icon="💘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide sidebar safely
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

# Title
st.markdown(
    """
    <div style="text-align:center;">
        <h1 style="color:#ff4b7d;">Hey Pari Baby my chottu baby💖✨</h1>
        <h2>Will you be my Valentine cutie?</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# YES button (normal Streamlit)
col1, col2 = st.columns(2)

with col1:
    if st.button("Yes 💕"):
        st.switch_page("pages/yes.py")

# NO button (HTML + JS hover dodge)
with col2:
    components.html(
        """
        <div id="container" style="height:200px; position:relative;">
            <button id="noBtn"
                style="
                    position:absolute;
                    padding:10px 18px;
                    font-size:16px;
                    border-radius:8px;
                    border:1px solid #555;
                    background:#111;
                    color:white;
                    cursor:pointer;
                ">
                No 😝
            </button>
        </div>

        <script>
            const btn = document.getElementById("noBtn");
            const container = document.getElementById("container");

            btn.addEventListener("mouseover", () => {
                const maxX = container.clientWidth - btn.offsetWidth;
                const maxY = container.clientHeight - btn.offsetHeight;

                const x = Math.random() * maxX;
                const y = Math.random() * maxY;

                btn.style.left = x + "px";
                btn.style.top = y + "px";
            });
        </script>
        """,
        height=220
    )
