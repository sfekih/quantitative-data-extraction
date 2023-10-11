import base64
import pandas as pd
import os
import streamlit as st
from typing import Dict, List
import matplotlib.image as mpimg
from const import (
    treated_projects_folder_names,
    results_types,
    treated_projects_full_names2folder_names,
)
from collections import defaultdict

# import plotly.graph_objects as go


# @st.cache_resource
def _load_results_one_project(one_project_name: str):
    dataset_path = os.path.join("DGIx Proof of Concept")
    data_results = defaultdict(lambda: defaultdict())

    for one_result_type in results_types:
        folder_path = os.path.join(dataset_path, one_project_name, one_result_type)
        if os.path.isdir(folder_path):
            files = os.listdir(folder_path)
            for one_file_name in files:
                if one_file_name.endswith(".csv") or one_file_name.endswith(".png"):
                    one_file_full_directory = os.path.join(folder_path, one_file_name)
                else:
                    raise Exception(
                        f"result has to be in '.csv' or '.png', file name is {one_project_name}/{one_result_type}/{one_file_name}"
                    )

                data_results[one_result_type][one_file_name] = one_file_full_directory

    return data_results


def convert_df(df):
    return df.to_csv(index=False, encoding="utf-8")  # .encode("utf-8")


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def add_logo(file):
    binary_string = get_base64_of_bin_file(file)

    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url("data:image/svg+xml;base64,%s");
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 10px;
            }
            [data-testid="stSidebarNav"]::before {
                margin-left: 20px;
                margin-top: 20px;
                margin-down: 50px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """
        % (binary_string),
        unsafe_allow_html=True,
    )


def _visualize_img(img_file_name: str, img_file_full_directory):
    img_file = mpimg.imread(img_file_full_directory)
    st.image(image=img_file, caption=img_file_name)
    # fig = go.Figure()
    # fig.add_trace(cv2.imshow("OpenCV Image", img_file))  # variable here


def _visualize_df(
    df_file_name: str, df_file_full_directory: pd.DataFrame, df_type: str
):
    df_file = pd.read_csv(df_file_full_directory)
    st.dataframe(df_file)

    csv = convert_df(df_file)
    st.download_button(
        label=f"Press to Download {df_file_name.replace('.csv', '').replace('_', ' ').title()} Numerical Results (csv)",
        data=csv,
        file_name=df_file_name,
        mime="text/csv",
        key=f"download-numerical-results-{df_file_name.replace('.csv', '')}-{df_type}-csv",
    )


def _get_page_output_one_project(
    project_short_name: str, show_raw_results: bool = True
):
    results_one_project = _load_results_one_project(project_short_name)
    project_extended_name = treated_projects_full_names2folder_names[project_short_name]

    st.write(f"# {project_extended_name} Country Level Results")

    ### COUNTRY LEVEL RESULTS (DF, VIZU)
    st.write("## Country Level Results and Visualizations")
    country_level_results_one_project = results_one_project[
        "Country Level Results and Visualizations"
    ]
    # st.write(f"country_level_results_one_project : {country_level_results_one_project}")
    output_files_one_country = list(country_level_results_one_project.keys())
    # st.write(f"output_files_one_country {output_files_one_country}")
    no_extension_output_files = list(
        set(
            [
                one_file.replace(".csv", "").replace(".png", "")
                for one_file in output_files_one_country
            ]
        )
    )

    for one_output_file in no_extension_output_files:
        st.write(f"### {one_output_file.replace('_', ' ').title()} Numerical Results")

        df_file_name = f"{one_output_file}.csv"
        if df_file_name in output_files_one_country:
            _visualize_df(
                df_file_name,
                country_level_results_one_project[df_file_name],
                df_type="country-level-results",
            )

        img_file = f"{one_output_file}.png"
        if img_file in output_files_one_country:
            _visualize_img(
                img_file, country_level_results_one_project[img_file]
            )  # variable here

    ### RAW RESULTS (DF)
    if show_raw_results:
        st.write("## All Extracted Numerical data Results")
        raw_results_one_project = results_one_project[
            "All Extracted Numerical data Results"
        ]
        for one_output_file, one_output_df in raw_results_one_project.items():
            one_output_file_clean = (
                one_output_file.replace(".csv", "").replace("_", " ").title()
            )
            st.write(f"### {one_output_file_clean} Numerical Results")
            _visualize_df(one_output_file_clean, one_output_df, df_type="all-results")
