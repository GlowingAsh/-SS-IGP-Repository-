# •	Profit & Loss csv : The program will compute the difference 
# in the net profit column if net profit on the current day is lower than the previous day. 

from pathlib import Path
import csv


#create a file to csv file.
fp = Path.cwd()/"csv_reports"/"Profit_Loss.csv"

#read the csv file to append Net Profit
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
  reader = csv.reader(file)
  next(reader) #skip header
  
 # create empty lists to store the net profit, day and the differences 
  net_profit = []
  days = []
  differences = []
  
  #append the empty lists 
  for data in reader(file):
      net_profit.append(data[4])
      

def profit_loss():
  """
  -function will return days where net profit is lower than the previous days with the differences
  """
  
