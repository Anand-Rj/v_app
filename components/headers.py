import streamlit as st

def center_text(text, size=2, color="#e91e63"):
    st.markdown(
        f"<h{size} style='text-align:center; color:{color};'>{text}</h{size}>",
        unsafe_allow_html=True
    )
