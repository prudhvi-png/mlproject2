import logging
import os
from datetime import datetime


## Initsilizing the file name 

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

## Settting drectory for storing logs
logs_path = os.path.join(os.getcwd(),'logs')

# Step 3: Creatng a log files in the directory
log_file_path = os.path.join(logs_path,LOG_FILE)

## Configuring the log file
logging.basicConfig(
    filename = log_file_path,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)


if __name__ == "__main__":
    logging.info("Logging started")