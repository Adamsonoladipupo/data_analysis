import streamlit as st


def render_prediction_form():

    st.subheader("House Features")

    col1, col2 = st.columns(2)

    with col1:

        longitude = st.number_input(
            "Longitude",
            value=-122.23
        )

        housing_median_age = st.number_input(
            "Housing Median Age",
            min_value=1.0,
            value=20.0
        )

        total_rooms = st.number_input(
            "Total Rooms",
            min_value=1,
            value=2000
        )

        population = st.number_input(
            "Population",
            min_value=1.0,
            value=1000.0
        )

        median_income = st.number_input(
            "Median Income",
            min_value=0.0,
            value=3.5
        )

    with col2:

        latitude = st.number_input(
            "Latitude",
            value=37.88
        )

        total_bedrooms = st.number_input(
            "Total Bedrooms",
            min_value=1,
            value=400
        )

        households = st.number_input(
            "Households",
            min_value=1.0,
            value=300.0
        )

        ocean_proximity = st.selectbox(
            "Ocean Proximity",
            [
                "<1H OCEAN",
                "INLAND",
                "NEAR OCEAN",
                "NEAR BAY",
                "ISLAND"
            ]
        )

    input_data = {
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity
    }

    return input_data