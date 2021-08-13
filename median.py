# WAP to find the median for a given dataset
import csv

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

# this for loop expressing the value in terms of rows and columns
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(n_num)
n = len(new_data)
new_data.sort()

# using floor division to ge the nearest whole number 
if n%2==0:
    # getting the first number
    median1 = float(new_data[n//2]) # floor division is shown by the symbol "//"
    median2 = float(new_data[n//2-1]) # this is getting the 2nd number
    # getting the mean of those two numbers
    median = (median1+median2)/2
else: 
    median = new_data[n//2]
    print(n)
print("median is:" + str(median))
    
