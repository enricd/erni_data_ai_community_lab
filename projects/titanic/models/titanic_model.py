import numpy as np
import pandas as pd
import streamlit as st
import pickle


# Load model from file
@st.cache_resource
def load_model():
    filename = "projects/titanic/models/titanic_xgboost_model.pkl"
    with open(filename, "rb") as file:
        model = pickle.load(file)

    return model