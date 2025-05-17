from sensor.exception import SensorException
from sensor.logger import logging
import sys
import os


def test_exception():
    try:
        logging.info("one error show : division by zero")
        a = 1/0
    except Exception as e:
        raise SensorException(e, sys)    # raise SensorExcetion(e,sys) :  error filename , error line for code and error string
        # raise e   # raise e :  only error string without filename and error line for code
     


if __name__=="__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)



