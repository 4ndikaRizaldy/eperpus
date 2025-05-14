import streamlit as st
import os

# Menambahkan logo dan title yang lebih menarik
st.title("E-Perpus - Baca Buku Online")
st.image("D:/PROJECT/refrensi/eperpusv1/assets/logo.jpg", width=150)

# URL server Flask
FLASK_URL = "http://192.168.1.72:8000/books"

# Path ke folder buku
BOOKS_DIR = "books"

# Daftar buku otomatis
books = [f for f in os.listdir(BOOKS_DIR) if f.endswith(".pdf")]

# Sidebar untuk navigasi
st.sidebar.header("Navigasi")
st.sidebar.text("Pilih buku dan baca langsung di sini.")
if books:
    selected_book = st.selectbox("Pilih Buku:", books)

    if selected_book:
        # URL PDF
        pdf_url = f"{FLASK_URL}/{selected_book}"
        
        # Menampilkan PDF menggunakan <object> dan jika tidak didukung, tampilkan link unduhan
        st.markdown(f"""
            <object data="{pdf_url}" type="application/pdf" width="100%" height="700px">
                <p>Browser Anda tidak mendukung PDF embed, silakan unduh file <a href="{pdf_url}">di sini</a>.</p>
            </object>
        """, unsafe_allow_html=True)
        
        # Menambahkan tombol unduh
        st.download_button(label="Unduh Buku", data=open(os.path.join(BOOKS_DIR, selected_book), "rb").read(), file_name=selected_book, mime="application/pdf")

else:
    st.warning("Tidak ada buku PDF yang tersedia.")
