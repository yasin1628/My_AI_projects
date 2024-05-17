import os
import sys
from src.exception import customexception
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class Data_ingestion_config:
    train_path : str = os.path.join('artifacts', 'train.csv')
    test_path : str = os.path.join('artifacts', 'test.csv')
    raw_path : str = os.path.join('artifacts', 'data.csv')

class Data_Ingestion:
    def __init__(self):
        self.ingestion_config = Data_ingestion_config()
    def iniate_data_ingestion(self):
        logging.info("Enteres the data ingestion method or component")

        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read dataset as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_path, index = False,header = True)

            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_path, index = True, header = True)
            test_set.to_csv(self.ingestion_config.test_path, index = True, header = True)
            
            logging.info("The data ingestion is completed")

            return (self.ingestion_config.train_path,
                    self.ingestion_config.test_path)
        except Exception as e:
            raise customexception(e,sys)
        
if __name__ == "__main__":
    obj = Data_Ingestion()
    obj.iniate_data_ingestion()


    