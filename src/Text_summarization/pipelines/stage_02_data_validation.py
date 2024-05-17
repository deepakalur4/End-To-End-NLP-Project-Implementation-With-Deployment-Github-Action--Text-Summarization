from Text_summarization.config.configuration import ConfigurationManager
from Text_summarization.components.data_validation import DataValidation
from Text_summarization.logging import logger



class DataValidationtrainingPipeline:
    def __call__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exists()
