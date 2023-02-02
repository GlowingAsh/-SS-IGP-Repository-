from pathlib import Path
import csv

def profit_loss_function():
  """
  Function called profit_loss Function
  Will compute the difference in the net profit column if the net profit on the current day is lower than the previous day.
  """
  
  # Creates an empty list
  profit_loss = []
  
  # # The Profit_Loss.csv file will be opened in read mode with UTF-8 encoding
  fp = Path.cwd()/"csv_reports"/"Profit_Loss.csv"
  
  # Read the csv file 
  with fp.open(mode="r", encoding="UTF-8", newline="") as file:
  
    reader = csv.reader(file)

    # Skip header
    next(reader) 
    #starts counting the first row of the csv file
    line_count = 0
   
    prev_day_value = 0
    
    # A for loop is used in the reader to store the values of net profit into prev_day_value
    for row in reader:
        if line_count == 0:
         line_count += 1 
         prev_day_value = row[4]
        else:
            if int(row[4]) < int(prev_day_value):
                profit_loss.append(f'[PROFIT DEFICIT] DAY: {row[0]}, AMOUNT: USD{int(prev_day_value) - int(row[4])}') 
            
            elif int(row[4]) > int(prev_day_value):
                profit_loss.append(f'[NET PROFIT SURPLUS] DAY: {row[0]}, AMOUNT: USD{int(row[4]) - int(prev_day_value)}')
            line_count += 1 
            prev_day_value = row[4]         
  # Return keyword to return profit loss together with f-string
  return profit_loss
