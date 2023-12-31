import streamlit as st
import os
from utils import _load_results_dataset, _get_page_output_one_project

st.set_page_config(
    page_title="Home",
    layout="wide",
    page_icon="img/Logo-16x16-01.png",
)

st.session_state["results"] = _load_results_dataset()


# Define functions for each page


def home_page():
    st.markdown("# Disaster Impact: Complete Events (DI: CE) Proof of Concept")
    # st.sidebar.success("Select a demo above.")
    st.markdown(
        """ 
    ### I. Application Struture
    This application encapsulates the unadulterated results pertaining to the devastating disasters of the 2022 Pakistan Floods, 
    the 2023 Turkey and Syria earthquakes and the displacement issued from the 2022 Ukraine war. 
    Each disaster was treated separately and results are given in the following pages (on the sidebar to the left).
    We sourced our work directly from data published on ReliefWeb. 

    ### II. Pages structure
    In each page, you will find organized data that has been both extracted and processed. Specifically, within each folder, we provide two key sets of results:

        1. All Extracted Numerical Data Results: 
            This section presents a comprehensive compilation of all numerical data that has been extracted. 
            It offers a detailed view of the quantitative information gathered, allowing for a thorough analysis and assessment of the dataset.
        
        2. Country Level Results and Visualizations: 
            In this section, you will find a more focused presentation of the data, organized at the country level. 
            This includes visual representations and numerical results that offer insights into the impact and trends specific to individual countries. 
            These visualizations enhance the accessibility and interpretation of the data for decision-makers and analysts. \n

        Together, these two result sets provide a complete and structured overview of the extracted numerical data, 
    facilitating both in-depth analysis and a broader understanding of the impact across countries.

    ### III. Treated Subjects
    To establish the robustness of our data extraction pipeline, we have applied it to address two distinct use cases across three separate projects. The first pipeline focuses on extracting critical data related to casualties resulting from natural disasters, while the second is specifically tailored to extract information pertaining to humanitarian displacement within war zones. 
    This comprehensive approach underscores the versatility and efficacy of our data extraction capabilities, 
    as they successfully tackle diverse scenarios and domains within these projects. 

        1. Casualties due to natural disasters: On the  the 2022 Pakistan Floods, the 2023 Turkey and Syria earthquakes
            a) Human Casualties: 
                A comprehensive account of the human toll exacted by these calamities, shedding light on the extent of the tragedy in terms of lives lost and affected. 
            b) Education, Health, and Livelihood Infrastructure Casualties: 
                A granular examination of the damage incurred by the educational, health, and livelihood infrastructure in the wake of these disasters, 
                providing insights into the scope of the impact on critical sectors. 
            c) Agricultural Casualties: 
                A detailed record of the losses experienced within the agricultural domain, offering a quantitative perspective on the agricultural devastation wrought by these events.
        
        2. Displacement due to war: on the 2022 Ukraine war, along with the different affected populations.
    It's crucial to underscore that all the results presented within this file are 100% reproducible and have undergone no manual data cleaning or manipulation. This commitment to data integrity ensures the accuracy and reliability of the information contained within, serving as a valuable resource for informed decision-making and humanitarian response efforts.

    For any further questions or inquieries, please contact us at `pc@okularanalytics.com`

    """
    )


def pakistan_page():
    # st.set_page_config(
    #     page_title="Pakistan Floods Human & Material Casualties",
    #     layout="wide",
    #     page_icon="img/Logo-16x16-01.png",
    # )
    _get_page_output_one_project("pakistan_floods")


def turkey_syria_page():
    # st.set_page_config(
    #     page_title="Turkey Syria Earthquake Human & Material Casualties",
    #     layout="wide",
    #     page_icon="img/Logo-16x16-01.png",
    # )

    _get_page_output_one_project("turkey_syria_earthquake")


def ukraine_page():
    # st.set_page_config(
    #     page_title="Ukraine Human Casualties & Displacement",
    #     layout="wide",
    #     page_icon="img/Logo-16x16-01.png",
    # )

    _get_page_output_one_project("ukraine_displacement", show_raw_results=False)


# Create a dictionary to map page names to functions
pages = {
    "Home": home_page,
    "Pakistan Floods Human & Material Casualties": pakistan_page,
    "Turkey Syria Earthquake Human & Material Casualties": turkey_syria_page,
    "Ukraine Human Casualties & Displacement": ukraine_page,
}

# Sidebar navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to:", list(pages.keys()))

# Display the selected page
selected_page_function = pages[selected_page]
selected_page_function()
