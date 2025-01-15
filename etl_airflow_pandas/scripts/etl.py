import pandas as pd
from logger_config import setup_logger

logger = setup_logger("ETL_Pipeline", "logs/etl_pipeline.log")

def extract():
    logger.info("Extraction started.")
    try:
        data = pd.read_csv('data/raw_data.csv')
        data.to_csv('data/temp/extracted_data.csv', index=False)
        logger.info("Extraction completed successfully.")
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        raise

def transform():
    logger.info("Transformation started.")
    try:
        data = pd.read_csv('data/temp/extracted_data.csv')
        data['new_column'] = data['existing_column'] * 2  # Exemple de transformation
        data.to_csv('data/temp/transformed_data.csv', index=False)
        logger.info("Transformation completed successfully.")
    except Exception as e:
        logger.error(f"Transformation failed: {e}")
        raise

def load():
    logger.info("Loading started.")
    try:
        data = pd.read_csv('data/temp/transformed_data.csv')
        data.to_csv('data/final_data.csv', index=False)  # Simule le chargement dans un fichier final
        logger.info("Loading completed successfully.")
    except Exception as e:
        logger.error(f"Loading failed: {e}")
        raise
