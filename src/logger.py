import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log" #name of logfile which is just the date time the file was run
logs_path=os.path.join(os.getcwd(), 'logs') #path containing log files
os.makedirs(logs_path, exist_ok=True) #continue appending new files to this dir
LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE) #path of the log file

logging.basicConfig(
    #this function allows you to degine where logging messages go, what they look like, and how much detail
    filename=LOG_FILE_PATH, # where to save the logs
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s %(message)s', #format of the log message
    level=logging.INFO) #sets the threshold. INFO will ignore debug messages, ERROR will ignore everything except critical failures

if __name__=='__main__':
    logging.info('Logging has started') #only runs if the file is executed directly