from decouple import config

PROJECT_ID = config('BIGQUERY_PROJECT_ID')
DATASET_ID = config('BIGQUERY_DATASET_ID')
TICKER_SYMBOL = config('TICKER_SYMBOL')
START_DATE = config('START_DATE')
END_DATE = config('END_DATE')
FORECAST_PERIODS = int(config('FORECAST_PERIODS', default=365))