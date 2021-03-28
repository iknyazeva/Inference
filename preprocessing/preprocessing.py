import pandas as pd
import numpy as np
from inference.inference import Infer


def read_data(path_to_data):
    """
    Function to read data
    Args:
        path_to_data (str): path to data, if data isn't in local files, download via path

    Returns: df (pandas DataFrame)

    """

    df = pd.read_csv(path_to_data, sep=';')
    return df


def split_data(data, column, id):
    """
    Function to split df into two groups
    Args:
        data (pandas DataFrame): original df
        column (str): division column from data, has to hold binary values
        id (int): division value of the column 0 or 1

    Returns: group (pandas DataFrame)

    """
    group = data[data[column] == id]
    return group


howell = read_data('../data/Howell1.csv')
male_0 = split_data(howell, 'male', 0).height
male_1 = split_data(howell, 'male', 1).height

inference_howell = Infer(howell)
print(inference_howell.test_independence(column_name='height', test_stat=np.mean))