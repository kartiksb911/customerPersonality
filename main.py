from src.exception import CustomException
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    try:
        ingestion_obj = DataIngestion()
        raw_data_path = ingestion_obj.initiate_data_ingestion()

        import pandas as pd
        df = pd.read_csv(raw_data_path)  

        transformation_obj = DataTransformation()
        scaled_data = transformation_obj.get_data_transformer_object(df)  

        model_trainer=ModelTrainer()
        model_trainer.initiate_model_trainer(scaled_data)

    except Exception as e:
        raise CustomException(e, sys)
