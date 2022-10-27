import numpy as np
import random
import pandas as pd


def get_random_matrix(num_rows: int, num_columns: int, rand_seed=None):
    '''
    Inputs:
        two integers greater than zero and
        an optional random seed argument
    Returns:
        matrix with N rows and M columns populated with
        floats from a uniform distribution between 0 and 1
    '''
    if rand_seed is not None:
        np.random.seed(rand_seed)
    matrix = np.random.rand(num_rows, num_columns)
    return matrix


def get_file_dimensions(file_name):
    '''
    Inputs:
        the name of a csv file
    Outputs:
        the dimensions of the contents of the
        file as a tuple (rows, columns)
    '''
    df = pd.read_csv(file_name, header=None)
    dimensions = df.shape
    return dimensions


def write_matrix_to_file(
        num_rows: int, num_columns: int, file_name: str, rand_seed=None):
    '''
    Inputs:
        two integers greater than zero,
        an optional random seed argument,
        and a file name to write to
    Outputs:
        Writes a file of a DataFrame with
        N rows and M columns populated with
        floats from a uniform distribution
        between 0 and 1
    Returns:
        None
    '''
    df = get_random_matrix(
        num_rows, num_columns, rand_seed)
    pd.DataFrame(df).to_csv(file_name, header=None)
    return None
