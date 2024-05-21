from Text_summarization.config.configuration import ConfigurationManager
from Text_summarization.components.model_trainer import ModelTrainer
from Text_summarization.logging import logger



class ModeltrainerPipeline:
    def __call__(self):
        pass

    def main(self):
        try:
            config=ConfigurationManager()
            model_trainerconfig=config.get_modeltrainer_config()
            model_trainerconfig=ModelTrainer(config=model_trainerconfig)
            model_trainerconfig.train()
        except Exception as e:
            raise e
    
