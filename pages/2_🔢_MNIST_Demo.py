import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st

from projects.mnist.utils.utils import canvas_draw
from projects.mnist.model.model_utils import load_model, predict, MLP


st.set_page_config(
        page_title="ERNI Data & AI Community Lab",
        page_icon="🔢",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Report a bug": "https://github.com/enricd",
            "About": """This is a demo Streamlit app made by Enric Domingo for the ERNI's Data and AI Community.
                        \nCode: https://github.com/enricd/erni_data_ai_community_lab/"""
        }
    )


st.sidebar.markdown("**Computer Vision** model to recognise single digit integer characters.")


st.header("🔢 MNIST Computer Vision Model Inference")
st.subheader("(🚧 Under Construction... 🚧)")
st.subheader("(Preliminary basic model, not yet much trained... )")

st.markdown("#")

# Load the model
model = load_model()


cols = st.columns((2,8,1,8,1,5,2))

with cols[1]:
    # Draw a number on the canvas
    st.write("✍️ Draw a number from 0 to 9:")
    image_raw = canvas_draw()
    if image_raw is not None:
        st.write(image_raw.shape)
        if np.sum(image_raw[:, :, 0:3]) == 0:
            image_raw = None

with cols[3]:
    # Downscale the numpy image to 28x28 pixels
    st.write("🐜 Downscaling to 28x28 pixels...")
    if image_raw is not None:
        image = Image.fromarray(image_raw).resize((28, 28))

        st.image(image, width=250)
        st.write(image.size)

        # Convert the image to grayscale
        image = image.convert('L')      # L: (8-bit pixels, grayscale)

        # Convert the image to a numpy array
        np_image = np.array(image)

with cols[5]:
    # Prediction
    st.write("🤖 Prediction:")
    if image_raw is not None:
        pred, prob = predict(model, np_image)
        st.info(f"### MLP: {pred}")
        #st.info(f"### MLP: {pred} ({prob:.2f}%)")
        st.metric("**MLP Model**", f"{pred} ({prob:.2f}%)")

        # TODO: add a CNN model




