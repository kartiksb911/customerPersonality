import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path = os.path.join("artifacts", "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            data_file_path = "notebook/data/Mall_Customers.csv"
            
            if not os.path.exists(data_file_path):
                raise FileNotFoundError(f"CSV file not found at {data_file_path}")
    
            df = pd.read_csv(data_file_path)
            logging.info("Reading the CSV data")

            columns_to_drop = [0, 1, 2]  
            df = df.drop(df.columns[columns_to_drop], axis=1)
            logging.info(f"Dropped columns: {columns_to_drop}")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Raw data saved at {self.ingestion_config.raw_data_path}")

            return self.ingestion_config.raw_data_path
        
        except Exception as e:
            raise CustomException(e, sys)
