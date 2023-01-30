from pathlib import Path
import matplotlib.pyplot as plt # ensure you have intalled matplotlib before importing it. available in the project brief.
import csv

# create a file to csv file.
fp = Path.cwd()/"Overheads.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    category = []
    overheads = []

    for row in reader:
        if row[0] == "Category":
            category.append(row[0])
        else:
            overheads.append(row[1])

def highest_oh():
    """
    Function will be able to identify the highest overhead category 
    and state the the percentage of the category
    """
    highest = float(max(overheads))
    
    # How to find the category with the highest overheads  

    return f"[HIGHEST OVERHEAD] Marketing Expense: {highest}"

print(highest_oh())

        












