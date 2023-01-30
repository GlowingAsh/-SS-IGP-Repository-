# •	Cash-On-Hand csv: The program will compute the difference 
# in Cash-on-Hand if the current day is lower than the previous day. 

from pathlib import Path
import csv

fp_read = Path.cwd()/"Cash on Hand.csv"
fp_write = Path.cwd()/"summary_report.txt"
fp_write.touch()
