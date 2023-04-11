import streamlit as st
import matplotlib.pyplot as plt

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
            st.markdown("#### Form")
            with st.form("Enter the data and click submit to start the analysis"):
                hashtag = st.text_input("Hashtag")
                number_of_tweets = st.number_input("Number of tweets", min_value=1, max_value=1000, value=10, step=1)

                submitted = st.form_submit_button("Submit")
        
        with model_cols[1]:
            st.markdown("### Status")
            if submitted:
                st.write(f"Searching {number_of_tweets} tweets for the topic {hashtag}. Please wait...")
                model = TSA(number_of_tweets, hashtag)
                st.write(model.status)
        
        with model_cols[2]:
            st.markdown("### How to")

    # --- 3. EDA ---
    with tabs[2]:
        st.subheader("Exploratory Data Analysis:")
        try:
            if model.status != "":
                st.markdown("### Dataframe")
                st.dataframe(model.data)
                st.image(create_wordcloud(model.data['plain_text'].values, 'all'))
                st.image(create_wordcloud(model.data_negative['plain_text'].values, 'negative'))
                st.image(create_wordcloud(model.data_positive['plain_text'].values, 'positive'))
                st.dataframe(count_values_in_column(model.data, 'sentiment'))
                st.dataframe(model.n_gram)
                
                data = count_values_in_column(model.data,'sentiment')
                names= data.index
                size=data['Percentage']
                circle=plt.Circle( (0,0), 0.7, color='white')
                plt.pie(size, labels=names, colors=['green', 'blue', 'red'])
                p=plt.gcf()
                p.gca().add_artist(circle)
                plt.show()
                st.pyplot(plt)
                plt.clf()


        except:
            st.write("Please, run the model to get the data")
            
if __name__ == "__main__":

    main()