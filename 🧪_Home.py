import streamlit as st

from projects.home.definitions import streamlit_description


def main():

    st.set_page_config(
        page_title="ERNI Data & AI Community Lab",
        page_icon="🧪",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Report a bug": "https://github.com/enricd",
            "About": "This is a demo Streamlit app made by Enric Domingo for the ERNI's Data and AI Community."
        }
    )

    st.title("🧪📈 The ERNI Data & AI Community Lab 🤖🧠")

    cols = st.columns((2, 1, 6))

    with cols[0]:
        st.markdown("#")
        st.markdown("#")
        st.image("projects/home/images/erni_logo.png",
                 use_column_width=True)    
        st.image("projects/home/images/data_ai_logo_light_blue.png", 
                 caption="ERNI Data & AI Community",
                 use_column_width=True)
        
    with cols[2]:
        st.markdown("#")
        st.markdown("#")
        st.write("We are building this project and apps using Streamlit:")
        st.image("projects/home/images/streamlit_logo.png",
                 )  
        
        st.subheader("A faster way to build and share data apps")

        with st.expander("Expand for more info..."):
            st.write(streamlit_description)

        st.write("Check it out: [Streamlit.io](https://streamlit.io)")



if __name__ == "__main__":

    main()


