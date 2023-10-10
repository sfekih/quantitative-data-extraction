import streamlit as st
from utils import _get_page_output_one_project

st.set_page_config(
    page_title="Turkey Syria Earthquake Human & Material Casualties",
    layout="wide",
    page_icon="img/Logo-16x16-01.png",
)

_get_page_output_one_project("turkey_syria_earthquake")
