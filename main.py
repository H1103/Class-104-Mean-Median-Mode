import csv
from os import read 
# csv module is one of the modules in python which provides classes for reading and writing tabular information in csv file format.
with open('SOCR-HeightWeight.csv', newLine =' ') as f:
# csv.reader() is used to read and return the current row and then moves on to the next line
     reader = csv.reader(f)
     file_data = list(reader) # adds the data ot the list
     
