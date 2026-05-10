import streamlit as st


def display_prediction(prediction: float):

    st.divider()

    st.subheader("Predicted House Price")

    st.metric(
        label="Estimated Median House Value",
        value=f"${prediction:,.2f}"
    )

    st.success("Prediction completed successfully.")