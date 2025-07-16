import sys 
import os
from dataclasses import dataclass

from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier
)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,recall_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object




@dataclass
class ModelTrainerConfig:
    trained_model_config = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def evaluate_model(self,true,predicted):
        try:

            score = accuracy_score(true,predicted)
            return score
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_model_training(self,train_array,test_array):

        try:
            logging.info("spliting the training and testing data")

            x_train,x_test,y_train,y_test = (
                train_array[:,:-1],
                test_array[:,:-1],
                train_array[:,-1],
                test_array[:,-1]
            )
        
            models = {
                "AdaBoostClass" :AdaBoostClassifier(),
                "GradientBoostClass" : GradientBoostingClassifier(),
                "Random Forest Classifier" : RandomForestClassifier(),
                "Kneighbours Classifier" : KNeighborsClassifier(),
                "Tree Classifier" : DecisionTreeClassifier(),
                "Xgboost Classfier" :XGBClassifier()
            }

            models_report = {}
            best_model = None
            best_score = 0

            for name,model in models.items():

                model.fit(x_train,y_train)   ## Fitting the model

                predicted = model.predict(x_test)

                score = self.evaluate_model(y_test,predicted)

                models_report[name] = score

                logging.info(f"{name} Accuracy : {accuracy_score}")

                if score > best_score:
                    best_score = score
                    best_model = model

            ## Saving the best model

            save_object(
                file_path = self.model_trainer_config.trained_model_config,
                obj = best_model
            )
            return best_score


        except Exception as e:
            pass


    