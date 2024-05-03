import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Recipe Recommendation System! 👋")

st.sidebar.success("Select a recommendation app.")

st.markdown(
    """
    A Recipe recommendation web application using Scikit-Learn, FastAPI and Streamlit.
    """
)
