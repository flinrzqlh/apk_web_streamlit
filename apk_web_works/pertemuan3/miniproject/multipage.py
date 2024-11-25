# MULTIPAGE -----------------------------------------------------------------------------------------

import streamlit as st

# Multipages Apps dengan Function
def main_page():
    st.markdown("# Ini adalah Halaman Utama...")
    st.sidebar.markdown("# Main Page!")
    
def page2():
    st.markdown("# Ini adalah Halaman Kedua")
    st.sidebar.markdown("# Second Page!")

def page3():
    st.markdown("# Ini adalah Halaman Ketiga")
    st.sidebar.markdown("# Third Page!")

pageName = {
    "Go to Main Page": main_page,
    "Go to Second Page": page2,
    "Go to Thrid Page": page3,
}

pageTerpilih = st.sidebar.selectbox("Choose a page", pageName.keys())
pageName[pageTerpilih]()