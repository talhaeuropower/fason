import streamlit as st
import pandas as pd
import sqlite3

# Sayfa Ayarları
st.set_page_config(page_title="Fason Takip Sistemi", layout="wide", page_icon="🏭")

# --- VERİTABANI BAĞLANTISI VE TABLO OLUŞTURMA ---
def init_db():
    conn = sqlite3.connect("fason_takip.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS siparisler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            urun_kodu TEXT NOT NULL,
            adet INTEGER NOT NULL,
            durum TEXT NOT NULL,
            eklenme_tarihi DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Veritabanını Başlat
init_db()

# Veri Ekleme Fonksiyonu
def siparis_ekle(urun_kodu, adet, durum):
    conn = sqlite3.connect("fason_takip.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO siparisler (urun_kodu, adet, durum) VALUES (?, ?, ?)", (urun_kodu, adet, durum))
    conn.commit()
    conn.close()

# Veri Çekme Fonksiyonu
def siparisleri_getir():
    conn = sqlite3.connect("fason_takip.db")
    df = pd.read_sql_query("SELECT id AS 'ID', urun_kodu AS 'Ürün Kodu', adet AS 'Adet', durum AS 'Durum', eklenme_tarihi AS 'Tarih' FROM siparisler ORDER BY id DESC", conn)
    conn.close()
    return df

# --- ARAYÜZ ---
st.title("🏭 Fason Takip Sistemi (SQLite Destekli)")

menu = st.sidebar.selectbox(
    "Menü Seçin",
    ["📊 Ana Panel", "📦 Ürün & Sipariş Listesi", "➕ Yeni Sipariş Ekle"]
)

# 1. EKRAN: ANA PANEL
if menu == "📊 Ana Panel":
    st.header("Genel Durum Özetiniz")
    
    df = siparisleri_getir()
    
    toplam_siparis = len(df)
    toplam_adet = df["Adet"].sum() if not df.empty else 0
    fasondakiler = df[df["Durum"] == "Fasonda"]["Adet"].sum() if not df.empty else 0
    tamamlananlar = df[df["Durum"] == "Tamamlandı"]["Adet"].sum() if not df.empty else 0

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Toplam Kayıtlı Ürün Adedi", value=f"{toplam_adet} Adet")
    col2.metric(label="Fasondaki Ürünler", value=f"{fasondakiler} Adet")
    col3.metric(label="Tamamlanan Ürünler", value=f"{tamamlananlar} Adet")
    
    st.markdown("---")
    st.subheader("Son Eklenen Siparişler")
    st.dataframe(df.head(5), use_container_width=True)

# 2. EKRAN: ÜRÜN VE SİPARİŞ LİSTESİ
elif menu == "📦 Ürün & Sipariş Listesi":
    st.header("Sipariş Listesi")
    
    df = siparisleri_getir()
    
    arama = st.text_input("🔍 Ürün Kodu Ara...", "")
    
    if arama and not df.empty:
        df = df[df["Ürün Kodu"].str.contains(arama, case=False)]
        
    st.dataframe(df, use_container_width=True)

# 3. EKRAN: YENİ SİPARİŞ EKLE
elif menu == "➕ Yeni Sipariş Ekle":
    st.header("Yeni Sipariş Girişi")
    
    with st.form("siparis_formu", clear_on_submit=True):
        urun_kodu = st.text_input("Ürün Kodu (Örn: FS-2026-01)")
        adet = st.number_input("Adet", min_value=1, value=100)
        durum = st.selectbox("Durum", ["Fasonda", "Tamamlandı", "Hazırlanıyor"])
        
        kaydet = st.form_submit_button("Siparişi Veritabanına Kaydet")
        
        if kaydet:
            if urun_kodu.strip() != "":
                siparis_ekle(urun_kodu, adet, durum)
                st.success(f"✅ '{urun_kodu}' kodlu {adet} adet ürün SQLite veritabanına başarıyla kaydedildi!")
            else:
                st.error("Lütfen geçerli bir ürün kodu girin.")
