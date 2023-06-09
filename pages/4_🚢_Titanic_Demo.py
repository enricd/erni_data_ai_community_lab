import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns

from projects.home.definitions import lab_contributors
from projects.home.utils import contributor_card
from projects.titanic.definitions import titanic_info
from projects.titanic.models.titanic_model import load_model


DATA_PATH = Path("projects/titanic/data")
TRAIN_PATH = DATA_PATH / "train.csv"
TEST_PATH = DATA_PATH / "test.csv"

@st.cache_data
def load_data():
    train_df = pd.read_csv(TRAIN_PATH)
    test_df = pd.read_csv(TEST_PATH)

    return train_df, test_df


def main():

    st.set_page_config(
        page_title="ERNI Data & AI Community Lab",
        page_icon="🚢",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Report a bug": "https://github.com/enricd",
            "About": """This is a demo Streamlit app made by Enric Domingo for the ERNI's Data and AI Community.
                        \nCode: https://github.com/enricd/erni_data_ai_community_lab/"""
        }
    )

    # --- Sidebar ---
    st.sidebar.markdown("**ML Binary Classification** problem.")

    st.sidebar.markdown("## Project Contributors:")
    # Create a card for each contributor
    for contributor in ["enricd"]:
        st.sidebar.markdown(contributor_card(
            **lab_contributors[contributor],
            ), 
            unsafe_allow_html=True)


    train_df, test_df = load_data()

    model = load_model()
    

    st.header("🚢 Survival Prediction on the Titanic - Kaggle")
    st.subheader("(🚧 Under Construction... 🚧)")

    tabs = st.tabs(["📄 Info",
                "📊 EDA",
                "🤖 Model",      
                ])
    
    # --- 1. Info ---
    with tabs[0]:
        st.subheader("Project Info:")

        info_cols = st.columns((6, 1, 6))

        with info_cols[0]:
            st.image("projects/titanic/images/titanic.png")
            st.markdown(titanic_info)

        with info_cols[2]:
            st.video("https://www.youtube.com/watch?v=8yZMXCaFshs&ab_channel=Kaggle")


    # --- 2. EDA ---
    with tabs[1]:
        st.subheader("Exploratory Data Analysis:")

        st.markdown("##### Matplotlib and Seaborn plots:")
        eda_cols1 = st.columns(2)
        with eda_cols1[0]:
            sns.histplot(train_df['Age'], bins=20, kde=False)
            plt.xlabel('Age')
            plt.ylabel('Count')
            plt.title('Age Distribution')
            st.pyplot(plt)
            plt.clf()

        with eda_cols1[1]: 
            # Create violin plot of age and fare distribution by passenger class
            sns.violinplot(x='Pclass', y='Age', data=train_df)
            plt.xlabel('Passenger Class')
            plt.ylabel('Age')
            plt.title('Age Distribution by Passenger Class')
            plt.show()
            st.pyplot(plt)
            plt.clf()



    # --- 3. Model ---
    with tabs[2]:
        st.subheader("🚧 (Model not yet connected to inputs) 🚧")

        st.subheader("Inference:")

        with st.form("Enter the passenger data"):
            name = st.text_input("Name (not used by the model)")
            f_cols = st.columns(3)
            with f_cols[0]:
                pclass = st.selectbox("Passenger Class", [1, 2, 3])
                sibsp = st.number_input("Number of Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)
                embarked = st.selectbox("Embarked", ["S", "C", "Q"])
            with f_cols[1]:
                sex = st.selectbox("Sex", ["Male", "Female"])
                parch = st.number_input("Number of Parents/Children Aboard", min_value=0, max_value=10, value=0)
            with f_cols[2]:
                age = st.number_input("Age", min_value=0, max_value=100, value=0)
                fare = st.number_input("Fare", min_value=0.0, max_value=1000.0, value=0.0)

            submitted = st.form_submit_button("Predict")
            
        if submitted:
            st.write("Name:", name, "(Model not yet connected to inputs)")

        # file_input = st.file_uploader("Upload input file")
        # if file_input:
        #     inputs = pd.read_csv(file_input)
        #     preds = model.predict(inputs)
        #     st.write(preds)

if __name__ == "__main__":

    main()