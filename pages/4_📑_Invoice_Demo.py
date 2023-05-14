from PIL import Image
import streamlit as st

from projects.home.definitions import lab_contributors
from projects.home.utils import contributor_card
from projects.Invoice.Utils.utils import OCRImage2Text, ImageRender

import cv2
import numpy as np



def main():

    st.set_page_config(
            page_title="ERNI Data & AI Community Lab",
            page_icon="📑",
            layout="wide",
            initial_sidebar_state="expanded",
            menu_items={
                "Report a bug": "https://github.com/enricd",
                "About": """This is a demo Streamlit app made by Enric Domingo for the ERNI's Data and AI Community.
                            \nCode: https://github.com/enricd/erni_data_ai_community_lab/"""
            }
        )

    # --- Sidebar ---
    st.sidebar.markdown("OCR for invoices text extraction.")
    st.sidebar.markdown("## Project Contributors:")
    # Create a card for each contributor
    for contributor in ["enricd"]:
        st.sidebar.markdown(contributor_card(
            **lab_contributors[contributor],
            ),
            unsafe_allow_html=True)

    st.header("📑 OCR for invoices text extraction.")

    st.markdown("#")


    imFileLoader = st.file_uploader("load image", type=['jpg', 'png', 'jpeg'], accept_multiple_files=False)

    cols = st.columns(4)
    result = None
    resultDenoise = None
    imageDenoise = None
    with cols[0]:
        st.write("Image loaded")
        if imFileLoader is not None:
            image = Image.open(imFileLoader)

            ## Image to numpy array
            imageNp = np.array(image.convert('RGB'))
            imageDenoise = ImageRender(imageNp)

            ## Resize for viewing comforably on the web
            imageResize = cv2.resize(imageNp, (240,320))
            st.image(imageResize)
            if (st.button("Extract")):
                Tolerance = imageNp.shape[1]//20
                result = OCRImage2Text(imageNp,Tolerance)
                resultDenoise = OCRImage2Text(imageDenoise,Tolerance)


    with cols[1]:
        st.write("Image Denoised")
        if imageDenoise is not None:
            st.image(cv2.resize(imageDenoise, (240,320)))
    with cols[2]:
        st.write("Text from original")
        if result is not None:
            st.write(result)
    with cols[3]:
        st.write("Text from denoised")
        if resultDenoise is not None:
            st.write(resultDenoise)


if __name__ == "__main__":

    main()
