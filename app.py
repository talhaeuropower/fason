import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Fason Takip Sistemi", layout="wide")

# Sol Menü Tasarımı
st.sidebar.title("📌 Fason Takip Menüsü")
menu = st.sidebar.radio("Ekran Seçin:", ["📊 Ana Panel", "📦 Ürün & Sipariş Listesi", "➕ Yeni Sipariş Ekle"])

if menu == "📊 Ana Panel":
    try:
        with open("dashboard.html", "r", encoding="utf-8") as f:
            html_code = f.read()
        components.html(html_code, height=900, scrolling=True)
    except FileNotFoundError:
        st.warning("`dashboard.html` dosyası henüz GitHub'a yüklenmedi.")

elif menu == "📦 Ürün & Sipariş Listesi":
    try:
        with open("order_list.html", "r", encoding="utf-8") as f:
            html_code = f.read()
        components.html(html_code, height=900, scrolling=True)
    except FileNotFoundError:
        st.warning("`order_list.html` dosyası henüz GitHub'a yüklenmedi.")

elif menu == "➕ Yeni Sipariş Ekle":
    try:
        with open("add_order.html", "r", encoding="utf-8") as f:
            html_code = f.read()
        components.html(html_code, height=900, scrolling=True)
    except FileNotFoundError:
        st.warning("`add_order.html` dosyası henüz GitHub'a yüklenmedi.")
