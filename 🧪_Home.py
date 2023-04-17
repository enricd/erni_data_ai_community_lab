import streamlit as st
from pathlib import Path

from projects.home.definitions import streamlit_description, lab_contributors
from projects.home.utils import contributor_card


def main():

    st.set_page_config(
        page_title="ERNI Data & AI Community Lab",
        page_icon="🧪",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Report a bug": "https://github.com/enricd",
            "About": """This is a demo Streamlit app made by Enric Domingo for the ERNI's Data and AI Community.
                        \nCode: https://github.com/enricd/erni_data_ai_community_lab/"""
        }
    )

    # --- Sidebar ---
    with st.sidebar:
        st.info("Check any of the projects above!", icon="⬆️")

    st.sidebar.markdown("## 🧑‍💻Lab Contributors:")
    # Create a card for each contributor
    for contributor in lab_contributors:
        st.sidebar.markdown(contributor_card(
            **lab_contributors[contributor],
            ), 
            unsafe_allow_html=True)

    # Using the README.md file as the main page intro
    st.markdown((Path(__file__).parents[0]/"readme.md").read_text("utf-8"),
        unsafe_allow_html=True
        )

    cols = st.columns((2, 1, 6))

    with cols[0]:
        st.markdown("#")
        st.markdown("#")
        st.image("projects/home/images/erni_logo.png",
                 use_column_width=True)    
        st.image("projects/home/images/data_ai_logo_light_blue.png", 
                 caption="ERNI Data & AI Community",
                 use_column_width=True)
        
    with cols[2]:
        st.markdown("#")
        st.markdown("#")
        st.write("We are building this project and apps using Streamlit:")
        st.image("projects/home/images/streamlit_logo.png",
                 )  
        
        st.subheader("A faster way to build and share data apps")

        with st.expander("Expand for more info..."):
            st.write(streamlit_description)

        st.write("Check it out: [Streamlit.io](https://streamlit.io)")



if __name__ == "__main__":

    main()


