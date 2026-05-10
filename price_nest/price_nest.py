import streamlit as st

from app.components.sidebar import render_sidebar
from app.components.prediction_form import render_prediction_form
from app.components.result_card import display_prediction

from app.utils.predictor import predict_house_price


st.set_page_config(
    page_title="Price Nest",
    layout="wide"
)


render_sidebar()


st.title("Price Nest")

st.write(
    "Predict housing prices using our model"
)


input_data = render_prediction_form()


if st.button("Predict House Price"):

    try:

        prediction = predict_house_price(input_data)

        display_prediction(prediction)

    except Exception as error:

        st.error(f"Prediction failed: {error}")