"""
Take this tamplate as a starting point for your Streamlit app and adapt it to your needs.
"""

# --- Libraries ---

import streamlit as st
from projects.home.definitions import lab_contributors
from projects.home.utils import contributor_card
from projects.mnist.utils.utils import canvas_draw #to delete
import numpy as np
from PIL import Image
from io import StringIO
from streamlit_image_select import image_select
# import numpy as np
# import pandas as pd
# from pathlib import Path
# etc...


# --- Definitions ---

# DATA_PATH = Path("projects/titanic/data")


# --- Functions ---



# --- Main ---

def main():
    image_raw=None
    st.set_page_config(
        page_title="ERNI Data & AI Community Lab",
        page_icon="🔠",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            # "Report a bug": "https://github.com/enricd",
            "About": """This is a demo Streamlit app made by the ERNI's Data and AI Community.
                        \nCode: https://github.com/enricd/erni_data_ai_community_lab/"""
        }
    )

    # --- Sidebar ---
    st.sidebar.markdown("OCR (Optical Character Recognition) project to automatically extract text and information from invoices and receipts images.") 

    st.sidebar.markdown("## Project Contributors:")
    # Create a card for each contributor
    for contributor in ["ayoitu", "jalbert83", "enricd"]:  # TODO: add contributors keys/names
        st.sidebar.markdown(contributor_card(
            **lab_contributors[contributor],
            ), 
            unsafe_allow_html=True)

    # --- Main Page ---
    st.header("🔠 Invoice OCR")

    st.subheader("(🚧 Under Construction... 🚧)")

    cols = st.columns((2,8,2,8,2,5,2))

    with cols[1]:
        # Choose the input
        st.write("✍️ Choose a way to select input:")
        
        #if st.button('Take a picture from your camera'):
        with st.expander('📸 Take a picture from your camera'):
            img_file_buffer = st.camera_input("Take a picture")
            if img_file_buffer is not None:
                # To read image file buffer as a PIL Image:
                img = Image.open(img_file_buffer)

                # To convert PIL Image to numpy array:
                image_raw = np.array(img)

                # Check the shape of img_array:
                # Should output shape: (height, width, channels)
                st.write(image_raw.shape)
        st.write ('or')
        with st.expander('📁 Choose a image file'):
            uploaded_file = st.file_uploader("Choose a image file", accept_multiple_files=False)
            if uploaded_file is not None:
                image_raw = Image.open(uploaded_file)
                image_raw = np.array(image_raw)
                st.write("filename:", uploaded_file.name)
                st.image(image_raw)
        st.write('or')
        with st.expander('📄 Choose a predeterminate file'):
            img = image_select("Choose a file", ["./projects/invoice_ocr/data/invoice_examples/ticket1.jpg", "./projects/invoice_ocr/data/invoice_examples/ticket2.jpg", "./projects/invoice_ocr/data/invoice_examples/ticket3.jpg"])
            if st.button('Send this invoice'):
                img= Image.open(img)
                img = np.array(img)
                image_raw=img
        
    with cols[2]:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("# ➡️")

    with cols[3]:
        # Show the Invoice selected
        st.write("🐜 That is the invoice selected")
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
            st.image(image_raw, width=250)
        



# --- Run ---

if __name__ == "__main__":

    main()