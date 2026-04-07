import os
from box.exceptions import BoxValueError
import yaml
from src.TextSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
# ConfigBox from the python-box library (python-box==6.0.2 in your requirements.txt) is a dot-notation dictionary that makes nested dictionary access feel like object attributes.

from pathlib import Path
from typing import Any

# ensure_annotations from the ensure library is a decorator that enforces Python type annotations at runtime.
@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    '''
    Reading a yaml file and returning it

    Args:
        path_to_yaml(str):path as input
    
    Raises:
        ValueError:if yaml file is empty
        e: Empty file
    
    Returns:
        ConfigBox:ConfigBox type
    '''

    try:
        with open(path_to_yaml) as file_yaml:
            content=yaml.safe_load(file_yaml)
            logger.info(f"yaml file: {path_to_yaml} loaded and returned successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    '''
    create a list of directories
    Args:
        path_to_directores (list): List of path of directories
        verbose(bool,optional): ignore if multiple dirs is to be created
    '''
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"{path} created successfully")
