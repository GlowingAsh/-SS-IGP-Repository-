from pathlib import Path
import csv

fp_read = Path.cwd()/"csv_reports/Cash_on_hand.csv"
fp_write = Path.cwd()/"summary_report.txt"
fp_write.touch()

with fp_read.open(mode= "r", encoding = "UTF-8", newline = "") as file:

    Day = []
    Cash_on_hand = []
    
