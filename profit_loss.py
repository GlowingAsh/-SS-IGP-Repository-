# •	Profit & Loss csv : The program will compute the difference 
# in the net profit column if net profit on the current day is lower than the previous day. 

from pathlib import Path
import csv


# create a file to csv file.
fp = Path.cwd()/"Profit_Loss.csv"

def profit_loss():
  """
  -function will return days where net profit is lower than the previous days with the differences
  """

  profit = []

  # Open the csv file
  with fp.open(mode="r", encoding="UTF-8", newline="") as file:
      # Read the csv file using the csv reader
      reader = csv.reader(file)
      # Skip the first row which is the header
      next(reader) 
       # Initialize the previous day value to 0
      prev_day_val = 0

      # Loop through all rows in the csv file
      for row in reader:
            # If the previous day value is 0 (first iteration)
            if prev_day_val == 0:
                # Assign the current day value as the previous day value
                prev_day_val = row[4]
            else:
                # If the current day value is less than the previous day value
                if int(row[4]) < int(prev_day_val):
                    # Calculate the deficit and store it in the profit_loss list
                    profit_loss.append(f'[PROFIT DEFICIT] DAY: {row[0]}, AMOUNT: USD{int(prev_day_val) - int(row[4])}')
                # Update the previous day value with the current day value
                prev_day_val = row[4]
  # Return the profit_loss list containing the deficit information
  return profit_loss  
