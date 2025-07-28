import os
from datetime import datetime
import logging

class CustomLogger:
    def __init__(self):
        self.logs_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(self.logs_dir, exist_ok=True)

        self.LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
        self.LOG_FILE_PATH = os.path.join(self.logs_dir, self.LOG_FILE)

        logging.basicConfig(
            filename=self.LOG_FILE_PATH,
            format='[%(asctime)s] - %(name)s - %(levelname)s - (line:%(lineno)d) - %(message)s',
            level=logging.INFO,
        )
        
        # self.logger = logging.getLogger("DocumentPortal")

    def get_logger(self,name=__file__):
        return logging.getLogger(os.path.basename(name)) 
    
if __name__ == "__main__":
    logger = CustomLogger()
    logger = logger.get_logger(__file__)
    logger.info("Custom logger initialized successfully.")

 