# •	Profit & Loss csv : The program will compute the difference 
# in the net profit column if net profit on the current day is lower than the previous day. 

from pathlib import Path
import csv

fp = Path.cwd()/"Profit_Loss.csv"

with fp.open(mode="r", emcoding="UTF-8", newline="") as file:
  
