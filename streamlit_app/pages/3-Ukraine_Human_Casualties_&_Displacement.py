import streamlit as st
from utils import _get_page_output_one_project

st.set_page_config(
    page_title="Ukraine Human Casualties & Displacement",
    layout="wide",
    page_icon="img/Logo-16x16-01.png",
)

_get_page_output_one_project("ukraine_displacement", show_raw_results=False)
