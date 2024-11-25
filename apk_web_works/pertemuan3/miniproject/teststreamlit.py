import streamlit as st
import pandas as pd
from PIL import Image

# LIBRARY STREAMLIT (TEXT ELEMENTS) 
# DISPLAY TEXT ------------------------------------------------------------------------------------

# st.markdown() 
# st.markdown() heading (Menggunakan simbol #)
st.markdown("# Ini Heading 1")
st.markdown("## Ini Heading 2")
st.markdown("### Ini Heading 3")

# st.markdown() Bold Text (Menggunakan simbol ** di awal dan di akhir teks)
st.markdown("** Ini adalah teks Bold")

# st.markdown() Italicised Text (Menggunakan simbol * di awal dan di akhir teks)
st.markdown("* Ini adalah teks teritalisiasi")

# st.markdown() Blockquote (Menggunakan simbol >)
st.markdown("> ini adalah Blockquote")

# st.markdown() Ordered List
st.markdown("1. Ini item ordered list 1")
st.markdown("2. Ini item ordered list 2")
st.markdown("3. Ini item ordered list 3")

# st.markdown() Unordered List
st.markdown("- Ini item unordered list a")
st.markdown("- Ini item unordered list b")

# st.markdown() Code
st.markdown("'Ini adalah Code")

# st.markdown() Horizontal Rule
st.markdown("---")

# st.title() 
# Menampilkan teks dengan format title
st.title("Ini adalah Title dengan st.title()")

# st.header() 
# Menampilkan teks dengan format header
st.header("Ini adalah header dengan st.header()")

# st.subheader() 
# Menampilkan teks dengan format subheader
st.subheader("Ini adalah header dengan st.subheader()")

# st.caption() 
# Menampilkan text dengan format font ukuran kecil (small font)
# biasa dugunakan untuk catatan kaki, caption, dan penjelasan tambahan
st.caption("Ini adalah Caption menggunakan st.caption()")

# st.text() 
# Menampilkan text dengan format fix width dan preformatted text
st.text("Ini adalah text menggunakan st.text()")

# METRIC AND COLUMNS ------------------------------------------------------------------------------
# st.metric()
# Menampilkan text dengan format metric dalam huruf besar, tebal, dan indikator perubahan
st.metric(label="Harga Iphone 12", value = 5000000, delta = -500000)
st.metric(label="Harga Iphone 13", value = 8000000, delta = 2500000)
st.metric(label="Harga Iphone 15", value = 20000000, delta = 0, delta_color="off")

# st.columns()
# st.metric() juga dapat dikombinasikan dengan st.columns()
kol1, kol2, kol3, kol4 = st.columns(4)
kol1.metric("Suhu", "30 C", "1.2 C")
kol2.metric("Angin", "10 kph", "-9%")
kol3.metric("Kelembapan", "78%", "4%")
kol4.metric("Curah Hujan", "2.0mm")

st.markdown("---")

# DISPLAY STYLE
# MAGIC --------------------------------------------------------------------------------------------

dataFrame = pd.DataFrame({
    'id barang': ['001', '002', '003', '004', '005', '006'],
    'nama barang': ['Pringles', 'Coca Cola', 'Sosis Sonice', 'Kecap Bango', 'Sambal Indofood', 'Royco'],
    'harga': [200000, 5000, 10000, 20000, 15000, 7000],
    'stock barang': [20, 30, 10, 15, 30, 50]
})
dataFrame

st.markdown("---")

# MEDIA ELEMENTS
# IMAGE, AUDIO, & VIDEO ----------------------------------------------------------------------------
# st.image()
gambar = Image.open('F:\EFFLIN THINGS\Materi Kuliah\Semester_5\Aplikasi_Web\Pertemuan3\SS\Screenshot_1.png')
st.image(gambar, caption="POV: Dapat 3 Praktikum di hari yang sama")

# st.audio()
bcksnd_file = open('F:\EFFLIN THINGS\Materi Kuliah\Semester_5\Aplikasi_Web\Pertemuan3\kitsch.mp3', 'rb')
bcksnd_bytes = bcksnd_file.read()
st.audio(bcksnd_bytes, format='audio/mp3')

# st.video()
vid_file = open('F:\EFFLIN THINGS\Materi Kuliah\Semester_5\Aplikasi_Web\Pertemuan3\JogedAsma.mp4', 'rb')
vid_bytes = vid_file.read()
st.video(vid_bytes)
