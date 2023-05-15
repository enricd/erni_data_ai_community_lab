# --- Libraries ---

import streamlit as st
from projects.home.definitions import lab_contributors
from projects.home.utils import contributor_card
from projects.mnist.utils.utils import canvas_draw #to delete
import numpy as np
from PIL import Image
from io import StringIO
from streamlit_image_select import image_select
import projects.invoice_ocr.ocr_models.ocr_models as Modellib
import projects.invoice_ocr.img_preprocessing.img_preprocessing as Preproclib


# --- Definitions ---



# --- Functions ---
def getFunctionsFromlibrary(lib):
    Functlist = [None]

    for func in dir(lib):
        if not func.startswith("__"):
            funcCall = getattr(lib, func)
            if callable(funcCall):
                Functlist.append(func)
                
    return np.array(Functlist)

# --- Main ---

def main():
    image_raw=None
    st.set_page_config(
        page_title="ERNI Data & AI Community Lab",
        page_icon="📑",
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
    for contributor in ["ayoitu", "jalbert83", "enricd"]:  
        st.sidebar.markdown(contributor_card(
            **lab_contributors[contributor],
            ), 
            unsafe_allow_html=True)

    # --- Main Page ---
    st.header("📑 Invoice OCR")

    st.subheader("(🚧 Under Construction... 🚧)")

    cols = st.columns((8,2,8,2,6))

    with cols[0]:
        # Choose the input
        st.write("🖼️ Choose a way to select input:")
        
        with st.expander("📸 Take a picture from your camera"):
            img_file_buffer = st.camera_input("Take a picture")
            image_raw = Image.open(img_file_buffer)
            image_raw = np.array(image_raw)

        st.write ("or")

        with st.expander("📁 Choose an image file"):
            uploaded_file = st.file_uploader("Choose a image file", accept_multiple_files=False)
            if uploaded_file is not None:
                image_raw = Image.open(uploaded_file)
                image_raw = np.array(image_raw)
                st.write("filename:", uploaded_file.name)
                st.image(image_raw)

        st.write("or")

        with st.expander("📄 Choose a predeterminate file"):
            img = image_select("Choose a file", ["./projects/invoice_ocr/data/invoice_examples/ticket1.jpg", "./projects/invoice_ocr/data/invoice_examples/ticket2.jpg", "./projects/invoice_ocr/data/invoice_examples/ticket3.jpg"])
            if st.button("Send this invoice"):
                img= Image.open(img)
                img = np.array(img)
                image_raw=img
        
    with cols[1]:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("# ➡️")

    with cols[2]:
        # Show the Invoice selected
        st.write("🔧 Preprocessing...")

        PreprocImage = None
        PreprocFunction = None
        Preprocessing = getFunctionsFromlibrary(Preproclib)
        preprocessing_option = st.selectbox("Choose a preprocessing function:", Preprocessing)
        if isinstance(preprocessing_option, str):
            PreprocFunction = getattr(Preproclib, preprocessing_option)
        
        if image_raw is not None:

            # processed_img = image_preprocessing(image_raw, preprocessing_option)

            #image = Image.fromarray(image_raw).resize((28, 28))
            st.write("Raw image")
            st.image(image_raw, width=250)
            st.write(type(image_raw))

            # Convert the image to grayscale
            #image = image.convert("L")      # L: (8-bit pixels, grayscale)

            # Convert the image to a numpy array
            np_image = np.array(image_raw)

            if PreprocFunction is not None:
                PreprocImage = PreprocFunction(image_raw)
                st.write("Preprocessed image")
                st.image(PreprocImage, width=250)
                st.write(type(PreprocImage))


    with cols[3]:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("# ➡️")

    with cols[4]:
        # Prediction

        st.write("🤖 Prediction:")

        ModelFunction = None
        Models = getFunctionsFromlibrary(Modellib)
        
        model_option = st.selectbox("Choose a model function:", Models)
        if isinstance(model_option, str):
            ModelFunction = getattr(Modellib, model_option)

        if PreprocImage is not None and ModelFunction is not None:
            Text = ModelFunction(PreprocImage)
            st.write(Text)



# --- Run ---

if __name__ == "__main__":

    main()