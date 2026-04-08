from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.components.data_transformation import DataTransformation
from src.TextSummarizer.logging import logger



class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self): 
        config=ConfigurationManager()
        data_transformer_config=config.get_data_transformation_config()
        data_transformer=DataTransformation(data_transformer_config)
        data_transformer.convert()