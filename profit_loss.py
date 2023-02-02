from pathlib import Path
import csv

def profit_loss_function():
  """
  Function called profit_loss Function
  Will compute the difference in the net profit column if the net profit on the current day is lower than the previous day.
  """
  
  # Make an empty list called profit_loss
  profit_loss = []
  
  # The Profit_Loss.csv file will be opened in read mode with UTF-8 encoding
  fp = Path.cwd()/"csv_reports"/"Profit_Loss.csv"
  
  # The file will be red and encoded in UTF-8 format 
  with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    
    # Make a reader to read the file
    reader = csv.reader(file)

    # Skip header
    next(reader) 

    #starts counting the first row of the csv file
    line_count = 0
    
    # Start with a value of 0
    prev_day_value = 0
    
    # A for loop is used in the reader to store the values of net profit into prev_day_value
    for row in reader:
        # If this is the first row
        if line_count == 0:
         # Add 1 to the line count
         line_count += 1 
         # Store the value in the first row as prev_day_value
         prev_day_value = row[4]

        else:
            # If it's not the first row
            # AND the line count is bigger than 1
            # AND the current value is less than the previous value
            if(line_count > 1 and (int(row[4]) < int(prev_day_val))): 
                # The calculations will be stored and using an f string to dsiplay the values, then it will be appended to profit_loss 
                profit_loss.append(f'[PROFIT DEFICIT] DAY: {row[0]}, AMOUNT: USD{int(prev_day_val) - int(row[4])}') 
            
            # Add 1 to the line count
            line_count += 1
            # Previous day value is assigned to the 4th index  in the row
            prev_day_val = row[4]  

# Return the profit_loss list
  return profit_loss 