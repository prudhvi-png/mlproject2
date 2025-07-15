from src.exception import CustomException
from src.logger import logging
import pandas as pd  
import os
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
import sys
from data_transformation import DataTransformation


@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw.csv")
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):

        logging.info("Entered the data Ingestion mode")
        try:


            df = pd.read_csv("notebooks\\Data\\Iris.csv")

            logging.info("read the dataset as DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)


            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)## Saving the converted Df info folder

            logging.info("train test split initiated")

            train_set, test_set = train_test_split(df,test_size=0.20,random_state=42)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            logging.info("Ingestion of data set is completed successfully")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    data_ingestion_obj = DataIngestion()
    train_data,test_data = data_ingestion_obj.initiate_data_ingestion()

    data_transform_obj = DataTransformation()
    train_arr, test_arr, preprocessor_path = data_transform_obj.initiate_data_transfromation(train_data, test_data)


