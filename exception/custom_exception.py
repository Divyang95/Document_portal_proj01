from logger.custom_logger import CustomLogger
import sys 
import traceback

logger = CustomLogger().get_logger(__file__)


class DocumentPortalException(Exception):
    """Custom exception for Document Portal errors."""
    def __init__(self,error_message, error_details:sys):
        _,_,exc_tb=error_details.exc_info() 
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        self.lineno=exc_tb.tb_lineno 
        self.error_message=str(error_message)
        self.traceback_str=" ".join(traceback.format_exception(*error_details.exc_info()))

    def __str__(self):
        return f""" 
        Error in {self.error_message} occurred in file {self.file_name}
         at line {self.lineno}. Traceback: {self.traceback_str} """

if __name__ == "__main__":
    try:
        # Simulating an error
        a = 1 / 0   
        print(a)
    except Exception as e:
        app_exception = DocumentPortalException(e,sys)
        logger.error(app_exception)
        raise app_exception