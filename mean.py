# WAP to find mean, median and mode in the given dataset.
import csv

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
# Sorting the file data to get the height of the people. We will remove the list using pop()
file_data.pop(0)
# First we remove the title list from data using pop() then we create empty list new_data then we use a loop on file_data to get the elements inside the nested list and append them to the new data list
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

# Finding Mean
n = len(new_data)
total = 0
# for loop is used to sum of the values 
for x in new_data:
    total += x
mean = total/n  
print("mean or average is " + str(mean))