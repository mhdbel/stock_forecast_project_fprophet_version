# upload/bigquery_upload.py
from google.cloud import bigquery
from datetime import datetime
import logging
from config import DATASET_ID, PROJECT_ID
from utils.logging_utils import log_dataframe_shape

# Initialize the BigQuery client using the configuration settings.
client = bigquery.Client(project=PROJECT_ID)

def upload_to_bigquery(data_frame, table_name):
    """
    Upload a DataFrame to BigQuery.
    The table name includes a timestamp to ensure uniqueness.
    """
    logging.info(f"Starting upload to BigQuery for table {table_name}...")
    try:
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        full_table_name = f"{DATASET_ID}.{table_name}_prophet_{timestamp}"
        log_dataframe_shape(data_frame, "Data to be uploaded")
        data_frame.to_gbq(
            destination_table=full_table_name,
            project_id=PROJECT_ID,
            if_exists='fail'
        )
        logging.info(f"Successfully uploaded data to BigQuery table {full_table_name}")
    except Exception as e:
        logging.error(f"An error occurred while uploading data to BigQuery: {e}")
