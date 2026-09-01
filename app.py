import streamlit as st
import pandas as pd

# Sayfa Ayarları
st.set_page_config(page_title="Fason Takip Sistemi", layout="wide", page_icon="🏭")

# Başlık
st.title("🏭 Fason Takip Sistemi")

# Sol Menü (Navigasyon)
menu = st.sidebar.selectbox(
    "Menü Seçin",
    ["📊 Ana Panel", "📦 Ürün & Sipariş Listesi", "➕ Yeni Sipariş Ekle"]
)

# 1. EKRAN: ANA PANEL
if menu == "📊 Ana Panel":
    st.header("Genel Durum Özetiniz")
    
    # İstatistik Kartları
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Toplama Alınan Ürün", value="1,250 Adet", delta="Toplam")
    col2.metric(label="Fasondaki Ürünler", value="450 Adet", delta="-50 İşleniyor")
    col3.metric(label="Tamamlanan Ürünler", value="800 Adet", delta="+120 Bu Hafta")
    
    st.markdown("---")
    st.subheader("Hızlı İşlemler")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("➕ Yeni Sipariş Oluştur", use_container_width=True):
            st.info("Sipariş ekleme ekranına geçmek için sol menüden 'Yeni Sipariş Ekle'yi seçebilirsiniz.")
    with col_btn2:
        if st.button("📥 Raporu İndir (Excel)", use_container_width=True):
            st.success("Rapor başarıyla indirildi!")

# 2. EKRAN: ÜRÜN VE SİPARİŞ LİSTESİ
elif menu == "📦 Ürün & Sipariş Listesi":
    st.header("Sipariş Listesi")
    
    # Arama Barı
    arama = st.text_input("🔍 Ürün Kodu Ara...", "")
    
    # Örnek Veri Tablosu
    data = {
        "Ürün Kodu": ["FS-2026-01", "FS-2026-02", "FS-2026-03"],
        "Adet": [250, 500, 150],
        "Durum": ["Fasonda", "Tamamlandı", "Hazırlanıyor"],
        "Tarih": ["2026-08-28", "2026-08-30", "2026-09-01"]
    }
    df = pd.DataFrame(data)
    
    if arama:
        df = df[df["Ürün Kodu"].str.contains(arama, case=False)]
        
    st.dataframe(df, use_container_width=True)

# 3. EKRAN: YENİ SİPARİŞ EKLE
elif menu == "➕ Yeni Sipariş Ekle":
    st.header("Yeni Sipariş Girişi")
    
    with st.form("siparis_formu"):
        urun_kodu = st.text_input("Ürün Kodu")
        adet = st.number_input("Adet", min_value=1, value=100)
        durum = st.selectbox("Durum", ["Fasonda", "Tamamlandı", "Hazırlanıyor"])
        
        kaydet = st.form_submit_button("Siparişi Kaydet")
        
        if kaydet:
            st.success(f"{urun_kodu} kodlu {adet} adet ürün başarıyla sisteme eklendi!")
