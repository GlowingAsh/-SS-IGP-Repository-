from pathlib import Path
import csv

def overheads_function():
    """
    Function called overheads 
    Will identify the highest overhead category and state the %
    """
    
    # File path will be under csv_reports folder, selecting the Overheads.csv file
    fp = Path.cwd()/"csv_reports\Overheads.csv"

    # The overheads. csv file will be opened in read mode with UTF-8 encoding
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    
        # Create a reader object to read the file
        reader = csv.reader(file)
        
        # Skip the first line of the file
        next(reader)
        
        # Variable maximum_value and maximum_overhead is assigned 0
        maxixmum_value = 0
        maximum_overhead = 0

        # A for loop is used in the reader 
        for row in reader:

            # The % sign is stripped of the 1st index column values, which is the overhead values
            overhead_value = float(row[1].strip("%"))

            # String will check if the overhead_value is graeter than the maximum_value
            if overhead_value > maxixmum_value:

                #The loop will be repeated till the maximum value is found, and the maximum value will be assigned to overhead_value
                maxixmum_value = overhead_value

                #The row will be assigned to the maximum_overhead
                maximum_overhead = row

        # A variable called max_overhead_value will be assigned to the string, f string is used to contain the values of the category and value of overhead
        max_overhead_value = f"[HIGHEST OVERHEADS] {maximum_overhead[0].upper()}: {maximum_overhead[1]}%"

    # For loop will then return the final values
    return max_overhead_value
       






















