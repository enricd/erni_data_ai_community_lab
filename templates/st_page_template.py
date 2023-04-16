"""
Take this tamplate as a starting point for your Streamlit app and adapt it to your needs.
"""

# --- Libraries ---

import streamlit as st
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
        page_icon="🚢",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            # "Report a bug": "https://github.com/enricd",
            "About": """This is a demo Streamlit app made by Enric Domingo for the ERNI's Data and AI Community.
                        \nCode: https://github.com/enricd/erni_data_ai_community_lab/"""
        }
    )

    st.sidebar.markdown("_(Project Description)_")

    st.sidebar.markdown("## Contributors:")



# --- Run ---

if __name__ == "__main__":

    main()