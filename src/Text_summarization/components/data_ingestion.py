import os
import urllib.request as request
import zipfile
from Text_summarization.logging import logger
from Text_summarization.utils.common import get_size
from Text_summarization.entity import (DataIngestionConfig)
from pathlib import Path

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        print(self.config.local_data_file)
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            file_name, headers=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{file_name} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists with size {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)            