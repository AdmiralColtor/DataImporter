from os import path
from loadAdmiralCSV import get_samples_in_order
from postExperimentAnalysis import get_avg_resistance, get_dataframes, assign_units_to_resistance

data_dir = "../data"
sample_files = get_samples_in_order(data_dir)

dataframes = get_dataframes(sample_files)

# map data to resistance getter function
avg_resistances = map(get_avg_resistance, dataframes)

# map resistances to string with unit attached
resistance_strings = map(assign_units_to_resistance, avg_resistances)

# save to output file
data_out = path.join(data_dir, "averageResistances.txt")
with open(data_out, 'w') as out_file:
    for i, resistance_string in enumerate(list(resistance_strings)):
        out_file.write(f"Sample {i+1}: {resistance_string}\n")
