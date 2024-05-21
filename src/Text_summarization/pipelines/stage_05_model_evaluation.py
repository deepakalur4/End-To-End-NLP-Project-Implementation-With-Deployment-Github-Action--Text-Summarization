from Text_summarization.config.configuration import ConfigurationManager
from Text_summarization.components.model_evaluation import Modelevaluation
from Text_summarization.logging import logger


class ModelevaluationPipeline:
    def __call__(self):
        pass

    def main(self):
        try:
            config=ConfigurationManager()
            model_validationconfig=config.get_data_validation_config()()
            model_validation=ModelTrainer(config=model_validationconfig)
            model_validation.train()
        except Exception as e:
            raise e