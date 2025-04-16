# plotting/forecast_plot.py
from fbprophet.plot import plot_plotly
from plotly.offline import plot
import logging

def plot_prophet_forecast(model, forecast):
    """
    Plots the forecast using Plotly offline mode.
    """
    logging.info("Plotting Facebook Prophet forecast...")
    try:
        fig = plot_plotly(model, forecast)
        plot(fig)  # Automatically opens the plot in the default web browser.
        logging.info("Plot successfully generated.")
    except Exception as e:
        logging.error(f"Error during plotting the forecast: {e}")
