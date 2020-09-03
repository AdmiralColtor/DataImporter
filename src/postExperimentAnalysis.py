import pandas as pd
from loadAdmiralCSV import get_samples_in_order
from typing import List


def get_dataframes(data_files: List) -> pd.DataFrame:
    dataframes = list(map(pd.read_csv, data_files))

    return dataframes


def get_avg_resistance(dataframe) -> float:
    Z_RES = "|Z| (Ohms)"

    return dataframe[Z_RES].mean()


def assign_units_to_resistance(resistance: float) -> str:
    abs_resistance = abs(resistance)

    unit = "ohms"
    if 0 <= abs_resistance < 1e3:
        resistance = resistance/1e0
        unit = "ohms"
    elif 1e3 <= abs_resistance < 1e6:
        resistance = resistance/1e3
        unit = "kilo ohms"
    elif 1e6 <= abs_resistance < 1e9:
        resistance = resistance/1e6
        unit = "mega ohms"
    # this can be continued...

    return f"{resistance} {unit}"
