import os
import sys
from src.logger import logging
from src.exception import CustomException
import pickle

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"Saving object to {file_path}")
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
        logging.info(f"Object successfully saved at {file_path}")    
    except Exception as e:
        raise CustomException(e,sys)     

def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)    
