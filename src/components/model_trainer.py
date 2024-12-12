import os
import sys
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from src.utils import save_object
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, scaled_data):
        try:
            k_means = KMeans(n_clusters=5, init="k-means++", random_state=42)
            y_kmeans = k_means.fit_predict(scaled_data)
            print(f"Cluster labels: {y_kmeans}")
            logging.info(f"Cluster labels: {y_kmeans}")

            silhouette_scr1 = silhouette_score(scaled_data, k_means.labels_)
            print(f"Silhouette score: {silhouette_scr1}")
            logging.info(f"Silhouette score: {silhouette_scr1}")

            save_object(file_path=self.model_trainer_config.trained_model_file_path, obj=k_means)
            logging.info(f"Trained model saved at {self.model_trainer_config.trained_model_file_path}")
        
        except Exception as e:
            raise CustomException(e, sys)
