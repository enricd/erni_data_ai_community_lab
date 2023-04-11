import streamlit as st
from projects.sentiment_analysis.utilities.definitions import *
from projects.sentiment_analysis.models.twitter_sentiment_model import TwitterSentimentAnalyzer as TSA


def main():

    st.set_page_config(
        page_title="ERNI Data & AI Community Lab",
        page_icon="🐦",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Report a bug": "https://github.com/enricd",
            "About": """This is a demo Streamlit app made by Enric Domingo, Marc Gonzalez and David Correa for the ERNI's Data and AI Community.
                        \nCode: https://github.com/enricd/erni_data_ai_community_lab/"""
        }
    )

    st.header("🐦 Tweets Sentiment Analysis")

    st.subheader("(🚧 Under Construction... 🚧)")

    tabs = st.tabs(["📄 Info", "🤖 Model", "📊 EDA"])

    # --- 1. Info ---
    with tabs[0]:
        st.subheader("Project Info:")

        intro_cols = st.columns((1))
        with intro_cols[0]:
            st.markdown(project_description)

        img_cols = st.columns((3))
        with img_cols[1]:
            st.image("projects/sentiment_analysis/images/static/sentiment_home.png")

        info_cols = st.columns((1))
        with info_cols[0]:
            st.markdown(sentiment_info)

        more_cols = st.columns((1))
        with more_cols[0]:
            st.markdown(more_info)
            st.video("https://www.youtube.com/watch?v=i4D5DZ5ZG-0")

    # --- 2. Model ---
    with tabs[1]:
        st.subheader("Sentiment Analysis:")
        model_cols = st.columns(3)
        with model_cols[0]:
            with st.form("Enter the data and click submit to start the analysis"):
                hashtag = st.text_input("Hashtag")
                number_of_tweets = st.number_input("Number of tweets", min_value=1, max_value=1000, value=10, step=1)

                submitted = st.form_submit_button("Submit")
            
            if submitted:
                st.write(hashtag, number_of_tweets)

if __name__ == "__main__":

    main()