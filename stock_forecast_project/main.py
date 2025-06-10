# main.py
import logging
from data.ingestion import download_stock_data
from models.prophet_model import create_prophet_model, forecast_prophet_model
from plotting.forecast_plot import plot_prophet_forecast
from upload.bigquery_upload import upload_to_bigquery
from config import TICKER_SYMBOL, START_DATE, END_DATE, FORECAST_PERIODS

# Configure logging to output to a log file.
logging.basicConfig(
    filename='app.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    try:
        # Step 1: Download and preprocess stock data.
        stock_data = download_stock_data(TICKER_SYMBOL, START_DATE, END_DATE)
        if stock_data.empty:
            logging.warning("No stock data available.")
            return
        
        # Step 2: Create and train the Prophet model.
        model = create_prophet_model(stock_data)
        
        # Step 3: Create future date DataFrame and forecast.
        try:
            future_data = model.make_future_dataframe(periods=FORECAST_PERIODS)
            logging.info(f"Future DataFrame created with periods: {FORECAST_PERIODS}")
        except Exception as e:
            logging.error(f"Error creating future dataframe for {TICKER_SYMBOL}, possibly due to FORECAST_PERIODS configuration: {e}")
            return

        forecast = forecast_prophet_model(model, future_data)
        
        # Step 4: Plot the forecast.
        plot_prophet_forecast(model, forecast)
        
        # Step 5: Upload the forecast results to BigQuery.
        columns_to_upload = ['ds', 'yhat', 'yhat_lower', 'yhat_upper']
        upload_to_bigquery(forecast[columns_to_upload], f'{TICKER_SYMBOL}_prophet_forecast')
    except Exception as main_exception:
        logging.error(f"An unexpected error occurred in main: {main_exception}")

if __name__ == "__main__":
    main()
