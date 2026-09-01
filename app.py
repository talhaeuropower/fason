import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Fason Takip Sistemi", layout="wide")

st.title("📊 Fason Takip Paneliniz")

try:
    with open("dashboard.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    # Google Stitch tasarımını ekrana basıyoruz
    components.html(html_code, height=900, scrolling=True)
except FileNotFoundError:
    st.info("Lütfen GitHub deponuza 'dashboard.html' dosyasını yükleyin.")
