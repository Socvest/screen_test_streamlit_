import streamlit as st
from st_screen_stats import st_screen_data


st.write("Page 2")
new_screen_ = st_screen_data(key="page_2")
st.write(new_screen_)
