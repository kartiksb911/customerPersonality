import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            scaler_path = os.path.join("artifacts", "scaler.pkl")  
            model = load_object(file_path=model_path)
            scaler = load_object(file_path=scaler_path)
            scaled_features = scaler.transform(features)
            prediction = model.predict(scaled_features)
            return prediction
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, annual_income, spending_score):
        self.annual_income = annual_income
        self.spending_score = spending_score                                     
                 
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "Annual Income (k$)": [self.annual_income],
                "Spending Score (1-100)": [self.spending_score]
            }
            df = pd.DataFrame(custom_data_input_dict)
            return df
        except Exception as e:
            raise CustomException(e, sys)
