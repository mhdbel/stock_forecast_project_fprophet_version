# models/prophet_model.py
import pandas as pd
from fbprophet import Prophet
import logging
from utils.logging_utils import log_dataframe_shape

def create_prophet_model(data_frame):
    """
    Preprocess the data and train the Facebook Prophet model.
    """
    logging.info("Creating Facebook Prophet model...")
    try:
        data_frame['ds'] = pd.to_datetime(data_frame['ds'])
        data_frame['y'] = data_frame['y'].astype(float)
        log_dataframe_shape(data_frame, "Data used for Prophet training")
        model = Prophet(daily_seasonality=True)
        model.fit(data_frame)
        logging.info("Prophet model created and fitted successfully.")
        return model
    except Exception as e:
        logging.error(f"Error in creating or fitting the Prophet model: {e}")
        raise

def forecast_prophet_model(model, future_data):
    """
    Generate a forecast using the trained Prophet model.
    """
    logging.info("Forecasting with Facebook Prophet model...")
    try:
        forecast = model.predict(future_data)
        log_dataframe_shape(forecast, "Forecast DataFrame")
        return forecast
    except Exception as e:
        logging.error(f"Error during forecasting: {e}")
        return pd.DataFrame()
