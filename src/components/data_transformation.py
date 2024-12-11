import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler
from src.utils import save_object  

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "scaler.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self, data):
        try:
            scaler = StandardScaler()
            scaled_data = scaler.fit_transform(data)
            logging.info("Data has been scaled using StandardScaler")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=scaler
            )
            logging.info(f"Scaler object saved at {self.data_transformation_config.preprocessor_obj_file_path}")

            return scaled_data

        except Exception as e:
            raise CustomException(e, sys)
