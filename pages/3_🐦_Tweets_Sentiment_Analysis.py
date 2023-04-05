import streamlit as st


def main():

    st.set_page_config(
        page_title="ERNI Data & AI Community Lab",
        page_icon="🐦",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Report a bug": "https://github.com/enricd",
            "About": "This is a Streamlit app made by the ERNI's Data & AI Community."
        }
    )

    st.header("🐦 Tweets Sentiment Analysis")

    st.subheader("(🚧 Under Construction... 🚧)")



if __name__ == "__main__":

    main()