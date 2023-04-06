import streamlit as st


def main():

    st.set_page_config(
        page_title="ERNI Data & AI Community Lab",
        page_icon="🐦",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Report a bug": "https://github.com/enricd",
            "About": """This is a demo Streamlit app made by Enric Domingo for the ERNI's Data and AI Community.
                        \nCode: https://github.com/enricd/erni_data_ai_community_lab/"""
        }
    )

    st.header("🐦 Tweets Sentiment Analysis")

    st.subheader("(🚧 Under Construction... 🚧)")



if __name__ == "__main__":

    main()