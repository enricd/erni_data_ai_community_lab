import streamlit as st
import matplotlib.pyplot as plt

from projects.home.definitions import lab_contributors
from projects.home.utils import contributor_card
from projects.sentiment_analysis.utilities.helpers import create_wordcloud, count_values_in_column
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

    # --- Sidebar ---
    st.sidebar.markdown("Text **Data Engineering** + **NLP** Sentiment Analysis Project.")

    st.sidebar.markdown("## Project Contributors:")
    # Create a card for each contributor
    for contributor in ["c0da8", "magopla"]:
        st.sidebar.markdown(contributor_card(
            **lab_contributors[contributor],
            ), 
            unsafe_allow_html=True)

    # --- Main Page ---
    st.header("🐦 Tweets Sentiment Analysis")

    st.subheader("(🚧 Under Construction... 🚧)")

    tabs = st.tabs(["📄 Info", "🤖 Model", "📊 EDA"])

    # --- 1. Info ---
    with tabs[0]:
        st.subheader("Project Info:")

        intro_cols = st.columns(1)
        with intro_cols[0]:
            st.markdown(project_description)

        img_cols = st.columns(3)
        with img_cols[1]:
            st.image("projects/sentiment_analysis/images/static/sentiment_home.png")

        info_cols = st.columns(1)
        with info_cols[0]:
            st.markdown(sentiment_info)

        video_cols = st.columns(3)
        with video_cols[1]:
            st.video("https://www.youtube.com/watch?v=i4D5DZ5ZG-0")
        
        more_cols = st.columns(1)
        with more_cols[0]:
            st.markdown(more_info)

    # --- 2. Model ---
    with tabs[1]:
        st.subheader("Sentiment Analysis:")
        model_cols = st.columns(3)

        with model_cols[0]:
            st.markdown("### How to")
            st.markdown(how_to)

        with model_cols[1]:
            st.markdown("#### Form")
            with st.form("Enter the data and click submit to start the analysis"):
                hashtag = st.text_input("Hashtag")
                number_of_tweets = st.number_input("Number of tweets", min_value=1, max_value=100, value=10, step=1)

                submitted = st.form_submit_button("Submit")
        
        with model_cols[2]:
            st.markdown("### Status")
            if submitted:
                if hashtag == "":
                    st.error("Hashtag is empty")
                    return
                if "#" not in hashtag:
                    st.error("Invalid hashtag")
                    return
                else:
                    st.write(f"Searching {number_of_tweets} tweets for the topic {hashtag}.")
                    with st.empty():
                        with st.spinner(text="In progress..."):
                            model = TSA(number_of_tweets, hashtag)
                        st.success('Completed!', icon="✅")
            else:
                st.write("Model has not been run")

    # --- 3. EDA ---
    with tabs[2]:
        st.subheader("Exploratory Data Analysis:")
        try:
            if model.status != "":
                df_cols = st.columns(1)
                with df_cols[0]:
                    st.markdown("### Dataframe")
                    st.dataframe(model.data)

                percent_cols = st.columns(2)
                with percent_cols[0]:
                    st.markdown("### Sentiment distribution")
                    fig = plt.figure()
                    fig.patch.set_facecolor("#0E1117")
                    plt.rcParams['text.color'] = 'white'
                    data = count_values_in_column(model.data,'sentiment')
                    names= data.index
                    size=data['Percentage']
                    circle=plt.Circle( (0,0), 0.7, color="#0E1117")
                    plt.pie(size, labels=names)
                    p=plt.gcf()
                    p.gca().add_artist(circle)
                    plt.show()
                    st.pyplot(plt)
                    plt.clf()
                with percent_cols[1]:
                    st.dataframe(data)

                wc_cols = st.columns(3)
                with wc_cols[0]:
                    st.markdown("### Most common words")
                    st.image(create_wordcloud(model.data['plain_text'].values, 'all'))
                with wc_cols[1]:
                    st.markdown("### Top negative words")
                    st.image(create_wordcloud(model.data_negative['plain_text'].values, 'negative'))
                with wc_cols[2]:
                    st.markdown("### Top positive words")
                    st.image(create_wordcloud(model.data_positive['plain_text'].values, 'positive'))
                
                st.markdown("### N-Gram")
                st.dataframe(model.n_gram)
            


        except:
            st.write("Please, run the model to get the data")
            
if __name__ == "__main__":

    main()