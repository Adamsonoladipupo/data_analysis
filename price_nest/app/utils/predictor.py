import pandas as pd
from app.utils.model_loader import model

def predict_house_price(data: dict):

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)

    return prediction[0]