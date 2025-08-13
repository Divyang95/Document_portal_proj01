import uuid 
from pathlib import Path 
import sys 
from datetime import datetime, timezone 
from langchain_community.document_loaders import PyPDFLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_community.vectorstores import FAISS 
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from utils.model_loader import ModelLoader

class DocumentIngestor:
    SUPPORTED_EXTENSIONS = {'.pdf', '.docx', '.txt', '.md'}
    def __init__(self, temp_dir:str = "D:\LLMOPS_Krishnaik\Document_portal_proj01\data\multi_doc_chat",faiss_dir:str='faiss_index', session_id:str|None=None):
        try:
            self.log = CustomLogger.get_logger(__name__)

            # base dirs
            self.temp_dir = Path(temp_dir) #Convertes temp_dir as path object so that we can apply method over it
            self.faiss_dir = Path(faiss_dir) # as it becomes path object so we can apply mkdir methods over it 
            self.temp_dir.mkdir(parents=True, exist_ok=True)# parent true means if any folder missing in that path it will create automatically
            self.faiss_dir.mkdir(parents=True, exist_ok=True)

            # sessionized paths
            self.session_id = session_id or f"session_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4.hex[:8]}"
            self.session_temp_dir = self.temp_dir/self.session_id
            self.session_faiss_dir = self.faiss_dir/self.session_id 
            self.session_temp_dir.mkdir(parents=True, exist_ok=True)
            self.session_faiss_dir.mkdir(parents=True, exist_ok=True)

            self.model_loader = ModelLoader()
            self.log.info(
                "DocumentIngestor Intialized",
                temp_base=str(self.temp_dir),
                faiss_base=str(self.faiss_dir),
                session_id=self.session_id,
                temp_path=str(self.session_temp_dir),
                faiss_path=str(self.session_faiss_dir)
                )


        except Exception as e:
            self.log.error('Failed to intialize DocumentIngestor', error=str(e))
            raise DocumentPortalException("Initialization error in DocumentIngestor", sys) 

    def ingest_files(self, documents):
        try:
            embeddings = ModelLoader().load_embeddings()
            vectorstore = FAISS.from_documents(documents, embeddings)
            return vectorstore.as_retriever()
        except Exception as e :
            pass  

    def _create_retriever(self,documents):
        pass    

