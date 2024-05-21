from Text_summarization.components import model_evaluation
from Text_summarization.pipelines.stage_01_data_ingestion import DataIngestiontrainingPipeline
from Text_summarization.pipelines.stage_02_data_validation import DataValidationtrainingPipeline
from Text_summarization.pipelines.stage_03_data_transformation import DataTransormationtrainingPipeline
from Text_summarization.pipelines.stage_04_model_trainer import ModeltrainerPipeline
from Text_summarization.pipelines.stage_05_model_evaluation import ModelevaluationPipeline
from Text_summarization.logging import logger



STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    data_ingestion=DataIngestiontrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    data_validation=DataValidationtrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transormation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    data_Transormation=DataTransormationtrainingPipeline()
    data_Transormation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model training Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    Model_trainer=ModeltrainerPipeline()
    Model_trainer.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Model training Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    model_evaluation=ModelevaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e