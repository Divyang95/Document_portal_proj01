import sys 
from dotenv import load_dotenv
import pandas as pd 
from logger.custom_logger import CustomLogger 
from exception.custom_exception import DocumentPortalException 
from model.models import * 
from prompt.prompt_library import PROMPT_REGISTRY 
from utils.model_loader import ModelLoader
from langchain.output_parsers import OutputFixingParser
from langchain_core.output_parsers import JsonOutputParser


class DocumentComparatorLLM:
    def __init__(self):
        pass 

    def compare_documents(self):
        """
        compares two documents and returns a structured comparison
        """
        pass 
    def format_response(self):
        """
        Formats the response from the LLM into a structured format
        """
        pass 
    

