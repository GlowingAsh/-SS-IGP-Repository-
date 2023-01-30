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

    def highest_overhead(data):
    max_overhead = 0
    category = ""
    for item in data:
        if item["Overheads"] > max_overhead:
            max_overhead = item["Overheads"]
            category = item["Category"]
    return category

    highest = highest_overhead(data)
    print(f"The category with the highest overhead is: {highest}")











