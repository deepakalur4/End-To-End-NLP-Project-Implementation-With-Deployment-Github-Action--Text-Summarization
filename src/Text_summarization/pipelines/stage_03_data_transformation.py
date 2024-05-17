from Text_summarization.config.configuration import ConfigurationManager
from Text_summarization.components.data_transfornation import DataTransformation
from Text_summarization.logging import logger



class DataTransormationtrainingPipeline:
    def __call__(self):
        pass

    def main(self):
        try:
            config=ConfigurationManager()
            data_transformationconfig=config.get_data_transformation_config()
            data_transformation=DataTransformation(config=data_transformationconfig)
            data_transformation.convert()
        except Exception as e:
            raise e
    
