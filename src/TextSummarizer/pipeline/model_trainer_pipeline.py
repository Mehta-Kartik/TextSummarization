from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.components.model_trainer import ModelTrainer

from src.TextSummarizer.logging import logger



class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self): 
        config=ConfigurationManager()
        data_transformer_config=config.get_model_trainer_config()
        data_transformer=ModelTrainer(data_transformer_config)
        data_transformer.train()