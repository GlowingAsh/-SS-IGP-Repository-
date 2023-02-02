# •	Profit & Loss csv : The program will compute the difference 
# in the net profit column if net profit on the current day is lower than the previous day. 

# ludwig is

from pathlib import Path
import csv

def profit_loss_function():
  """
  -function will return days where net profit is lower than the previous days with the differences
  """
  
  #create an empty list
  profit_loss = []
  
  #create a file to csv file.
  fp = Path.cwd()/"csv_reports"/"Profit_Loss.csv"
  
  #read the csv file to append Net Profit
  with fp.open(mode="r", encoding="UTF-8", newline="") as file:
  
    reader = csv.reader(file)
    next(reader) #skip header
  
    line_count = 0
    prev_day_value = 0
    
    #loop through all the rows
    for row in reader:
      if line_count == 0:
        line_count += 1 
        prev_day_value = row[4]
      else:
        if(line_count > 1 and (int(row[4]) < int(prev_day_val))):
        
          profit_loss.append(f'[PROFIT DEFICIT] DAY: {row[0]}, AMOUNT: USD{int(prev_day_val) - int(row[4])}') 
        line_count += 1 
        prev_day_val = row[4]                                                                   
  return profit_loss
