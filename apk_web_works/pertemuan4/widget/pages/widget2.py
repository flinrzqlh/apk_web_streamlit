import streamlit as st
import time

st.markdown("# Spinner Widget with st.spinner() :alien:")
st.sidebar.markdown("st.spinner :alien:")

# Streamlit st.spinner() 
with st.spinner('Tunggu sebentar...'):
    time.sleep(5)
st.success("Selesai!")