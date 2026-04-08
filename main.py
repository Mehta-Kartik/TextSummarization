from src.TextSummarizer.logging import logger
# logger.info("Hello World")

from src.TextSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME} initiated")
    data_ingest_pipeline=DataIngestionTrainingPipeline()
    data_ingest_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    print(e)