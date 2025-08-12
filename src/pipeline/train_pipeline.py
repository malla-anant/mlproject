import os
import sys
from src.exception import CustomException
from src.utils import save_object
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    try:
        print(">>> Starting Data Ingestion...")
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        print(">>> Starting Data Transformation...")
        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
            train_data_path, test_data_path
        )

        print(">>> Starting Model Training...")
        model_trainer = ModelTrainer()
        best_model_score, best_model_name, model_path = model_trainer.initiate_model_trainer(
            train_arr, test_arr
        )

        print(f">>> Training Completed. Best Model: {best_model_name} with score: {best_model_score}")
        print(f">>> Preprocessor saved at: {preprocessor_path}")
        print(f">>> Model saved at: {model_path}")

    except Exception as e:
        raise CustomException(e, sys)
