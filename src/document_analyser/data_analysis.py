import os
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from langchain_core.output_parser import JsonOutputParser
from langchain.output_parser import OutputFixingParser 


class DocumentAnalyzer:
    """
    Analyses documents using a pre-trained model
    Automatically logs all actions and supports session-based organization
    """

    def __init__(self):
        pass

    def analyse_metadata(self):
        pass
    

