from src.TextSummarizer.logging import logger
# logger.info("Hello World")

from src.TextSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.TextSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.TextSummarizer.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.TextSummarizer.pipeline.model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME} initiated")
    data_ingest_pipeline=DataIngestionTrainingPipeline()
    data_ingest_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    print(e)

STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f"{STAGE_NAME} initiated")
    data_transformation_pipeline=DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    print(e)



STAGE_NAME="Model Trainer Stage"

try:
    logger.info(f"{STAGE_NAME} initiated")
    model_trainer_pipeline=ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    print(e)



STAGE_NAME="Model Evaluation Stage"

try:
    logger.info(f"{STAGE_NAME} initiated")
    model_evaluate_pipeline=ModelEvaluation()
    model_evaluate_pipeline.initiate_model_evaluation()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    print(e)
