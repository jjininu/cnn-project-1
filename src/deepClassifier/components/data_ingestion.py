

import os
from tkinter import E

import urllib.request as request
from zipfile import ZipFile
from deepClassifier.entity.entity import DataIngestionConfig
from deepClassifier.config.config import ConfigurationManager
from tqdm import tqdm
from deepClassifier import logger



from deepClassifier.utils.common import get_size
from deepClassifier.utils.common import read_yaml, create_directories


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info(f"download the file from the url")

        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
                )
                logger.info(f"downloding {filename}complitted with size of {get_size(filename)} and data inforation /n {headers}")
        except Exception as e:
            logger.info(f"file already exist  of size {get_size(self.config.local_data_file)}")
            raise e
            
    def _get_updated_list_of_files(self, list_of_files):
        logger.info(f"filter relevnat files")
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]
        

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        logger.info(f"unziping the file  transfer")
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)
        
        if os.path.getsize(target_filepath) == 0:
            os.remove(target_filepath)

    def unzip_and_clean(self):
        logger.info(f"unziping file")
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)


  