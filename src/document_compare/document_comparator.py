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
        load_dotenv()
        self.log = CustomLogger().get_logger(__name__) 
        self.loader = ModelLoader()
        self.llm = self.loader.load_llm()
        self.parser = JsonOutputParser(pydantic_object=SummaryResponse)
        self.fixing_parser = OutputFixingParser.from_llm(parser=self.parser, llm = self.llm)
        self.prompt = PROMPT_REGISTRY.get("document_comparator")
        # self.prompt = PROMPT_REGISTRY["document_comparator"]
        self.chain = self.prompt | self.llm | self.parser | self.fixing_parser

        self.log.info("DocumentComparatorLLM intialized with model and parser.") 




    def compare_documents(self):
        """
        compares two documents and returns a structured comparison
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error in compare_documents: {e} ")
            raise DocumentPortalException("An error occurred while comparing documents.", sys)
        

    def _format_response(self):
        """
        Formats the response from the LLM into a structured format
        """
        try:
            pass

        except Exception as e:
            self.log.error("Error formatting response into dataframe", error= str(e) )
            raise DocumentPortalException("An error ocurred while comparing documents.", sys) 
        



