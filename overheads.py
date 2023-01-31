from pathlib import Path
import csv

fp_read = Path.cwd()/"csv_reports"/"Overheads.csv"

with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    category = [] # List called category to store values under Category
    overheads = [] # List called overheads to store values under Overheads

    for row in reader:
        category.append(row[0]) # Value in index 0 will be appended into Category
        overheads.append(float(row[1])) # Value in index 1 will be appended into Overheads, since there is decimals in the values, it will be stored as a float value
        

def highest_oh(category, overheads):
    """
    Function will be able to identify the highest overhead category 
    and state the the percentage of the category
    The only two values in the function will be category and overheads.
    """
    highest = 0
    highest_category = ""

    for index, value in enumerate(overheads):
        if value > highest:
            highest = value
            highest_category = category[index]
            
    return f"[HIGHEST OVERHEAD] {highest_category}: {highest}"

print(highest_oh(category, overheads))

        






















