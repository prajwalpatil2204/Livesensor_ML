from sensor.exception import SensorException
import sys
import os
from sensor.logger import logging

from sensor.pipeline.training_pipeline import TrainPipeline

#from sensor.utils2 import dump_csv_file_to_mongo_collection
'''def test_exception():
    try :
        logging.info("Ya pe zero division error ayegi")
        a = 10 /0
    except Exception as e:
        raise SensorException(e,sys)'''

if __name__ == "__main__":
    
    #file_path = "C:/Users/Prajwal/Machine_Learning/LiveSensor/aps_failure_training_set.csv"
    #database_name = "livesensor_ML_project"
    #collection_name  = "sensor"
    
    

    #dump_csv_file_to_mongo_collection(file_path,database_name,collection_name)
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
    
    '''try:
        test_exception()
    except Exception as e:
        print(e)'''

