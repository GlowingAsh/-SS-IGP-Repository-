from pathlib import Path
import csv

def overheads_function():
    """
    Function called overheads will identify the highest overhead category and state the %
    """
    high_overhead= []
    # List created called high_overhead to store the value of the highest overhead

    fp = Path.cwd()/"csv_reports\Overheads.csv"
    # File path will be under csv_reports folder, selecting the Overheads.csv file

    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        #skips the first line
        line_count = 0
        # 
        max_value = 0
        #
        for row in reader:
            if line_count == 0:
                line_count += 1
            else:
                if(line_count > 1 and (float(row[1]) > float(max_value))):
                    max_value = float(row[1])
                max_overhead = row
                line_count += 1
        max_overhead_value = f"[HIGHEST OVERHEADS] {max_overhead[0].upper()}: {max_overhead[1]}%"
        return max_overhead_value






















