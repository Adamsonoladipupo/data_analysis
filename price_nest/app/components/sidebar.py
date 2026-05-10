import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("Price Nest")

        st.markdown("""
        ### About

        PriceNest predicts housing prices using machine learning.

        ### Tech Stack

        - Python
        - Streamlit
        - Scikit-learn
        - Pandas
        - Joblib

        ### Model

        Trained using California housing data.
        """)

        st.divider()

        st.info(
            "Enter house details to receive a predicted median house value."
        )