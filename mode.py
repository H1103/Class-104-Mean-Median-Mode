import csv
from collections import Counter

with open('SOCR-HeightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []


for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(n_num)

# Calculating mode
# From collection we are importing counter and passing the new_data to Counter() and storing in in a var called data then we create a dictionary with the range of height as keys and the occurences of the heights as values which start at 0.
data = Counter(new_data)
mode_data_for_range = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }
# We are using a loop on data.item() using if and elif we'll check if the heihgt is lying between given ranges. 
# We will also need to convert the string to float using float(). 
# If the height lies in range the occurence count will increase
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0

for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")
