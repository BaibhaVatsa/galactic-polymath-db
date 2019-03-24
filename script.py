import pandas
import collections
import os.path
import subprocess

# assumed for now
file_path = "tortoisedata.csv"

# raise errors
if file_path[-4:] != ".csv":
    raise TypeError("File is not of .csv format")
if not os.path.isfile(file_path):
    raise Exception("File does not exist")

# read and pre process file
file_data = pandas.read_csv(file_path, keep_default_na=False, keep_date_col=True)
num_cols = 0
headers = []
for header in file_data:
    headers.append(header)
    num_cols += 1