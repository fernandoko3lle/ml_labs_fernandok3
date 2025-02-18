'''Data loading utilities for the California Housing Prices dataset.
'''
import tarfile
from pathlib import Path
from urllib import request

import pandas as pd

HOUSING_URL = ('https://raw.githubusercontent.com/ageron/handson-ml2/'
               'master/datasets/housing/housing.tgz')


def fetch_housing_data(data_dir: Path) -> None:
    '''Downloads the California Housing Prices dataset.

    Downloads the California Housing Prices dataset from Aurelien Geron's
    GitHub repository and saves it to the specified directory.

    Args:
        data_dir: The directory to which the dataset will be saved.

    Returns:
        None
    '''
    if not data_dir.exists():
        data_dir.mkdir(parents=True)

    # Fetch the housing data.
    tgz_path = data_dir / 'housing.tgz'
    request.urlretrieve(HOUSING_URL, tgz_path)

    # Extract the housing data.
    with tarfile.open(tgz_path) as housing_tgz:
        housing_tgz.extractall(path=data_dir, filter='data')


def load_housing_data(data_dir: Path) -> pd.DataFrame:
    '''Loads the California Housing Prices dataset.

    Loads the California Housing Prices dataset from the specified directory.

    Args:
        data_dir: The directory from which the dataset will be loaded.

    Returns:
        A pandas DataFrame containing the California Housing Prices dataset.
    '''
    csv_path = data_dir / 'housing.csv'
    df = pd.read_csv(csv_path)
    return df
