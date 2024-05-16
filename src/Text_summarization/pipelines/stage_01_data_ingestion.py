from Text_summarization.config.configuration import ConfigurationManager
from Text_summarization.components.data_ingestion import DataIngestion
from Text_summarization.logging import logger



class DataIngestiontrainingPipeline:
    def __call__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
