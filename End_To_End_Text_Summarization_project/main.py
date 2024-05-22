from Text_Summarizer.logging import logger
from Text_Summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Text_Summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Text_Summarizer.pipeline.stage_04_data_trainer import DataTrainingPipeline

Stage_Name = "Data Ingestion Stage"

try:
    logger.info(f"Starting {Stage_Name}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Completed {Stage_Name}")
except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = "Data Validation Stage"
try:
    logger.info(f"Starting {Stage_Name}")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"Completed {Stage_Name}")
except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = "Data Transformation Stage"
try:
    logger.info(f"Starting {Stage_Name}")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"Completed {Stage_Name}")
except Exception as e:
    logger.exception(e)
    raise e 

Stage_Name = "Data Training Stage"
try:
    logger.info(f"Starting {Stage_Name}")
    data_training = DataTrainingPipeline()
    data_training.main()
    logger.info(f"Completed {Stage_Name}")
except Exception as e:
    logger.exception(e)
    raise e 