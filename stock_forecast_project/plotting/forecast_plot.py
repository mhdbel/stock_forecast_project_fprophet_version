# plotting/forecast_plot.py
import os
from fbprophet.plot import plot_plotly
import logging

def plot_prophet_forecast(model, forecast):
    """
    Plots the forecast and saves it as an HTML file.
    """
    logging.info("Generating and saving Facebook Prophet forecast plot...")
    try:
        fig = plot_plotly(model, forecast)

        file_path = 'stock_forecast_project/plotting/forecast_plot.html'
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        fig.write_html(file_path)
        logging.info(f"Plot successfully saved to {file_path}")
    except Exception as e:
        logging.error(f"Error during generating or saving the forecast plot: {e}")
