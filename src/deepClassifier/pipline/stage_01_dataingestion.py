from deepClassifier.components.data_ingestion import *
from deepClassifier.config.config import ConfigurationManager
from deepClassifier import logger

stage_name = "DATA INGESTION"
def main() :
    try:
        
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()
    except Exception as e:
        raise e

    if __name__ == "__main__":
        try:
            logger.info(f"<<<<<<<<<<<<<<<<<<<<{stage_name} started>>>>>>>>>>>>>>>>>>>>>>>>")
            main()
            logger.info(f"<<<<<<<<<<<<<<<<<<<<{stage_name} complited>>>>>>>>>>>>>>>>>>>>>>>>")
        except Exception as e:
            raise e