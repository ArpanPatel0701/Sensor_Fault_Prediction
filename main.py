from sensor.exception import SensorException
from sensor.logger import logging
import sys
import os

from sensor.configuration.mongo_db_connection import MongoDBClient

# from sensor.utils import dump_csv_file_to_mongodb_collection
# from sensor.entity.config_entity  import TrainingPipelineConfig,DataIngestionConfig

from sensor.pipeline.training_pipeline import TrainPipeline





# def test_exception():
#     try:
#         logging.info("one error show : division by zero")
#         a = 1/0
#     except Exception as e:
#         raise SensorException(e, sys)    # raise SensorExcetion(e,sys) :  error filename , error line for code and error string
#         # raise e   # raise e :  only error string without filename and error line for code
     

if __name__ =="__main__":
    # file_path = r"Dataset/aps_failure_training_set1.csv"
    # database_name = "Sansor"
    # collection_name = "sensor"
    # dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)


    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()


# if __name__=="__main__":
#     try:
#         test_exception()
#     except Exception as e:
#         print(e)




