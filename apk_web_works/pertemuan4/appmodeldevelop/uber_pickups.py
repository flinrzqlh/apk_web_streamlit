import streamlit as st
import pandas as pd
import numpy as np

# Atur Judul dan Jalankan
st.title("UBER PICKUPS DI NYC")

# Atur Constant
DATE_COLUMN = 'date/time'
DATA_URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

# Membuat Fungsi Data Loader (ditambahkan dekorator cache st.cache_data)
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    # Mentransformasi nama kolom menjadi lowercase
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # Mentransformasi data kolom ke dalam format datetime
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Menampilkan Data ke Streamlit
# Mengambil Data. Jalankan
data_load_state = st.text('Memuat data...')
data = load_data(10000)
data_load_state.text("Selesai! (menggunakan st.cache_data)")
# Memperlihatkan dan Menyembunyikan DataFrame. Jalankan
if st.checkbox('Menampilkan Data Mentah'):
    st.subheader('Data Mentah')
    st.write(data)

# Menambahkan Histogram. Jalankan
st.subheader('Jumlah Pickup per Jam')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Menambahkan Maps
# Filter-Filter Map Berdasarkan Filter On The Hour
# Nomor pada rentang 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == 
hour_to_filter]
# Perlihatkan Map. Jalankan
st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)