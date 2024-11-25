import streamlit as st
import time

st.markdown("# Progress Bar with st.progress() :smile:")
st.sidebar.markdown("st.progress() :smile:")

# Streamlit Progress Bar --------------------------------------------------------------------------
'Memulai Komputasi yang Lama'

# Menambahkan Placeholder
newest_Iteration = st.empty()
progBar = st.progress(0)

for i in range(100):
    # Mengupdate Progress Bar untuk setiap Iterasi
    newest_Iteration.text(f'Iteration {i+1}')
    progBar.progress(i + 1)
    time.sleep(0.1)
    
'Selesai!'