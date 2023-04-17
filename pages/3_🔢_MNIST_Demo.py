import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st

from projects.home.definitions import lab_contributors
from projects.home.utils import contributor_card
from projects.mnist.utils.utils import canvas_draw
from projects.mnist.model.model_utils import load_model, MLP, CNN, mlp_predict, cnn_predict


def main():

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


    # --- Sidebar ---
    st.sidebar.markdown("**Computer Vision** model to recognise single digit integer characters.")
    st.sidebar.markdown("## Project Contributors:")
    # Create a card for each contributor
    for contributor in ["enricd"]:
        st.sidebar.markdown(contributor_card(
            **lab_contributors[contributor],
            ), 
            unsafe_allow_html=True)

    st.header("🔢 MNIST Computer Vision Model Inference")

    st.markdown("#")

    # Load the model
    mlp_model = load_model("projects/mnist/model/model.pth")
    cnn_model = load_model("projects/mnist/model/CNN_model.pth")


    cols = st.columns((2,8,2,8,2,5,2))

    with cols[1]:
        # Draw a number on the canvas
        st.write("✍️ Draw a number from 0 to 9:")
        image_raw = canvas_draw()
        if image_raw is not None:
            st.write(image_raw.shape)
            if np.sum(image_raw[:, :, 0:3]) == 0:
                image_raw = None

    with cols[2]:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("# ➡️")

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

    with cols[4]:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("# ➡️")

    with cols[5]:
        # Prediction
        st.write("🤖 Prediction:")
        if image_raw is not None:
            mlp_pred, mlp_prob = mlp_predict(mlp_model, np_image)
            st.info(f"### MLP: {mlp_pred} ({mlp_prob:.2f}%)")

            cnn_pred, cnn_prob = cnn_predict(cnn_model, np_image)
            st.info(f"### CNN: {cnn_pred} ({cnn_prob:.2f}%)")


    cols2 = st.columns(3)
    with cols2[2]:
        with st.expander("MLP Pytorch model architecture..."):
            st.write(mlp_model)
        with st.expander("CNN Pytorch model architecture..."):
            st.write(cnn_model)



if __name__ == "__main__":

    main()



