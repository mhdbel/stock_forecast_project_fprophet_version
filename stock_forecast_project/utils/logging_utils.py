#logging_utils.py
import logging

def log_dataframe_shape(df, description="DataFrame"):
    """Logs the shape of the DataFrame along with a custom description."""
    logging.info(f"{description} shape: {df.shape}")
