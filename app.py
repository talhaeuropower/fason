import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Fason Takip Sistemi", layout="wide")

st.title("📊 Fason Takip Paneliniz")

try:
    with open("dashboard.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    # Custom component kullanarak tıklama verilerini yakalıyoruz
    event_data = components.html(html_code, height=900, scrolling=True)

    # HTML'den gelen tıklama verilerini Python tarafında işleme:
    if event_data:
        st.write("Tıklanan İşlem:", event_data)

except FileNotFoundError:
    st.info("Lütfen GitHub deponuza 'dashboard.html' dosyasını yükleyin.")
