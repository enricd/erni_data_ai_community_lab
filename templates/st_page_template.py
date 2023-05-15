"""
Take this tamplate as a starting point for your Streamlit app and adapt it to your needs.
"""

# --- Libraries ---

import streamlit as st
from projects.home.definitions import lab_contributors
from projects.home.utils import contributor_card
# import numpy as np
# import pandas as pd
# from pathlib import Path
# etc...


# --- Definitions ---

# DATA_PATH = Path("projects/titanic/data")


# --- Functions ---

""""
You can define here some basic functions or you can develop a more complex logic
into the projects/<your_project>/ folder, building there a package with the needed
modules and data.
"""


# --- Main ---

def main():

    st.set_page_config(
        page_title="ERNI Data & AI Community Lab",
        page_icon="🚢",  # TODO: add icon
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            # "Report a bug": "https://github.com/enricd",
            "About": """This is a demo Streamlit app made by the ERNI's Data and AI Community.
                        \nCode: https://github.com/enricd/erni_data_ai_community_lab/"""
        }
    )

    # --- Sidebar ---
    st.sidebar.markdown("Project description...")  # TODO: add description

    st.sidebar.markdown("## Project Contributors:")
    # Create a card for each contributor
    for contributor in []:  # TODO: add contributors keys/names
        st.sidebar.markdown(contributor_card(
            **lab_contributors[contributor],
            ), 
            unsafe_allow_html=True)

    # --- Main Page ---
    st.header("Project Title...")  # TODO: add title

    st.subheader("(🚧 Under Construction... 🚧)")



# --- Run ---

if __name__ == "__main__":

    main()