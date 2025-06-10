# data/ingestion.py
import time
import pandas as pd
import yfinance as yf
import logging
import os
from utils.logging_utils import log_dataframe_shape

def download_stock_data(ticker, start_date, end_date, retries=3, delay=5):
    """
    Downloads historical stock data from Yahoo Finance.
    Implements a retry mechanism in case of transient failures.
    """
    logging.info(f"Starting download for {ticker} from {start_date} to {end_date}...")
    attempt = 0
    while attempt < retries:
        try:
            historical_data = yf.download(ticker, start=start_date, end=end_date)
            if historical_data.empty:
                logging.warning(f"Attempt {attempt+1}: No data found for {ticker} from {start_date} to {end_date}")
                attempt += 1
                if attempt < retries:
                    time.sleep(delay)
                else:
                    return pd.DataFrame()
                continue

            log_dataframe_shape(historical_data, "Downloaded stock data")

            if 'Close' not in historical_data.columns:
                logging.error("The 'Close' column is missing in the stock data.")
                return pd.DataFrame()

            # Reset index and rename columns to suit Prophet’s requirements
            historical_data.reset_index(inplace=True)
            historical_data.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)
            historical_data['ds'] = pd.to_datetime(historical_data['ds']).dt.tz_localize(None)
            historical_data['y'] = historical_data['y'].astype(float)

            # Save the downloaded data for backup/analysis
            file_path = f'{ticker}_original_data.csv'
            historical_data.to_csv(file_path, index=False)
            logging.info(f"Successfully downloaded and saved stock data for {ticker}")
            log_dataframe_shape(historical_data, "Processed stock data")
            return historical_data[['ds', 'y']]
        except Exception as e:
            logging.error(f"Attempt {attempt+1} failed downloading stock data: {e}")
            attempt += 1
            if attempt < retries:
                time.sleep(delay)
            else:
                return pd.DataFrame()
