import streamlit as st
from utils import _load_results_dataset
from const import treated_projects_full_names2folder_names, results_types
import os

st.set_page_config(
    page_title="Numbers Extraction PoC",
    layout="wide",
    page_icon="img/Logo-16x16-01.png",
)
# add_logo("LOGOPATH")

RESULTS_FOLDER = os.path.join("DGIx Proof of Concept")

st.session_state["results"] = _load_results_dataset(RESULTS_FOLDER)
st.session_state[
    "treated_projects_full_names2folder_names"
] = treated_projects_full_names2folder_names
st.session_state["results_types"] = results_types

st.write("# Quantitative Data Extraction Proof of Concept")
# st.sidebar.success("Select a demo above.")
st.markdown(
    """ 
This page contains two pages . \n
........................................
"""
)
