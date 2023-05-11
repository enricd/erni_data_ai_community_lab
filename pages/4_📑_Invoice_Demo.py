from PIL import Image
import streamlit as st

from projects.home.definitions import lab_contributors
from projects.home.utils import contributor_card
from projects.Invoice.Utils.utils import OCRImage2Text

import cv2
import numpy as np
import easyocr


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


    cols = st.columns(2)
    result = None

    with cols[0]:
        st.write("Load a photo of an invoice")
        imFileLoader = st.file_uploader("load image", type=['jpg','png','jpeg'], accept_multiple_files=False)
        if imFileLoader is not None:
            image = Image.open(imFileLoader)

            ## Image to numpy array
            imageNp = np.array(image.convert('RGB'))

            ## Resize for viewing comforably on the web
            imageResize = cv2.resize(imageNp, (240,320))
            st.image(imageResize)
            if (st.button("Process...")):
                result = OCRImage2Text(imageNp)


    with cols[1]:
        st.write("Text extracted")
        if result is not None:
            st.write(result)


if __name__ == "__main__":

    main()
