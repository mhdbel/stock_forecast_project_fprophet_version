# stock_forecast_project_fprophet_version

This project is a complete pipeline for forecasting stock prices using Facebook Prophet. It downloads historical stock data from Yahoo Finance, preprocesses it, trains a forecast model, generates future predictions, visualizes the forecast using Plotly, and uploads key forecast data to Google BigQuery.

## Project Structure

- **config.py**: Reads configuration from environment variables.
- **data/ingestion.py**: Contains functions to download and preprocess stock data.
- **models/prophet_model.py**: Contains functions to build and forecast with the Prophet model.
- **plotting/forecast_plot.py**: Contains functions to generate interactive plots.
- **upload/bigquery_upload.py**: Contains functions to upload results to BigQuery.
- **utils/logging_utils.py**: Utility functions (e.g., logging DataFrame shapes).
- **main.py**: Application entry point that ties everything together.
- **requirements.txt**: List of required Python packages.

## Setup and Installation

1. Clone this repository.
2. Create a virtual environment:
   ```bash
   python -m venv venv
