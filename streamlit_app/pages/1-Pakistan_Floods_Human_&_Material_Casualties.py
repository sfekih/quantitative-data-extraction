import streamlit as st
from utils import _get_page_output_one_project

st.set_page_config(
    page_title="Pakistan Floods Human & Material Casualties",
    layout="wide",
    page_icon="img/Logo-16x16-01.png",
)
_get_page_output_one_project("pakistan_floods")

# all_output_files = list(results.keys())
# no_extension_output_files = list(
#     set(
#         [
#             one_file.replace(".csv", "").replace(".png", "")
#             for one_file in all_output_files
#         ]
#     )
# )

# with st.sidebar:
#     st.write("Select Project")
#     # with st.expander("time slots"):
#     selected_project_names = st.multiselect(
#         f"Select one or many projects",
#         list(st.session_state["treated_projects_full_names2folder_names"].keys()),
#     )

#     st.write("Treated Topics")
#     # with st.expander("Select Topics"):
#     selected_project_names = st.multiselect(
#         f"Select one or many topics",
#         no_extension_output_files,
#     )


# #################################### PDF ########################################
# # st.write(f"## {time_period} PDF Summaries {summary_type}")

# # st.write(
# #     "### PDF file too large for rendering, please download it and review it on your local computer."
# # )

# country2overll_name = st.session_state["treated_projects_full_names2folder_names"]

# for one_project in selected_project_names:
#     st.write(f"## {country2overll_name[one_project]} Outputs")

#     for one_output_file in no_extension_output_files:
#         img_file = f"{one_output_file}.png"
#         # if img_file in all_output_files:
#         #     _visualize_img(results[img_file])  # variable here

#         df_file = f"{one_output_file}.csv"
#         if df_file in all_output_files:
#             _visualize_df(results[df_file])
