import pandas as pd
from os import listdir as ls
from typing import List


"""
Get all files corresponding to a sample in a directory. Return value is
a list of file names ordered starting with sample 1, then sample 2, then sample 3
and so on...
"""
def get_samples_in_order(directory: str) -> List:
    # get all files in directory (this will collect even non-csv files)
    data_files = ls(directory)

    """
    Build a list of file names that correspond to samples. Samples are files
    containing the string Potentiostatic EIS.
    """

    sample_files = []
    for file_name in data_files:
        if "Potentiostatic EIS" in file_name:
            sample_files.append(file_name)

    """
    Sort samples, this will order the files by their index
    So, we get that the first element is the file starting with 2__, the second
    is the file starting with 4__, the third is the file starting with 6__
    and so on
    """
    sample_files = sorted(sample_files)

    return sample_files
