import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd       
import os
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from sklearn.preprocessing import StandardScaler


@dataclass
class DataTransformationConfig:
    preprocessor_obj_path = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transfer_object(self):

        """This Function is responsible for data transformation"""

        try:
            columns = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

            num_pipeline = Pipeline(
                steps=[("scaler",StandardScaler())]
            )

            logging.info(f"Columns are : {columns}")              ### Here only creating the preprocessor object without applying on data

            preprocessor = ColumnTransformer([
                ("num_pipeline",num_pipeline,columns)
            ])
            
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        

    def initiate_data_transfromation(self,train_path,test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info("Read train and test data completed! ")
            logging.info("Obtaining preprocessor object ")

            preprocessor_obj = self.get_data_transfer_object()    # We are taking preprocessor object

            target_column_name = 'Species'
            columns = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

            input_feature_train_df = train_df.drop(columns=target_column_name,axis=1)
            target_feature_train_df =  train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=target_column_name,axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training data frame and testing dataframe")

            input_feature_train_df = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_df = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_df,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_df,np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_path,
                obj = preprocessor_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
        