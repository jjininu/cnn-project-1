

from collections import namedtuple
from dataclasses import dataclass
from importlib.resources import path
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL: str
    local_data_file:Path
    unzip_dri:Path
