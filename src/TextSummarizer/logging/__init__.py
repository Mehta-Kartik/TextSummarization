import os
import sys
import logging

log_dir="logs"
loggin_str='[%(asctime)s]:%(levelname)s %(module)s %(message)s'
log_filepat=os.path.join(log_dir,"continous_logs.log")

os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=loggin_str,

    handlers=[
        logging.FileHandler(log_filepat),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger('summarizelogger')