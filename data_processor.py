import numpy as np
import random
import pandas as pd

def get_random_matrix(num_rows: int, num_columns: int, rand_seed = None):
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
    df = pd.read_csv(file_name, header = None)
    dimensions = df.shape
    return dimensions

def write_matrix_to_file(num_rows, num_columns, file_name):
    return None
