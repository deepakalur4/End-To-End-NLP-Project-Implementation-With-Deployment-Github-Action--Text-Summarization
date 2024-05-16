from Text_summarization.pipelines.stage_01_data_ingestion import DataIngestiontrainingPipeline
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