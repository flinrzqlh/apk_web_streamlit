import streamlit as st

#without any arguments (args,kwargs)
def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)
with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Iya atau Tidak', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)