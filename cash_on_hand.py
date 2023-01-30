from pathlib import Path
import csv

fp_read = Path.cwd()/"csv_reports/Cash_on_hand.csv"
fp_write = Path.cwd()/"summary_report.txt"
fp_write.touch()

with fp_read.open(mode= "r", encoding = "UTF-8", newline = "") as file:
    reader = csv.reader(file)
    next(reader)

    Day = []
    Cash_On_Hand = []
    
    total = 0
    previous_day_value = 0
    for row in reader:
        day = float(row[0])
        cash_on_hand = float(row[1])
        total += cash_on_hand
        if previous_day_value != 0:
            difference = cash_on_hand - previous_day_value
            if difference < 0:
              print(f"[CASH DEFICIT] DAY: {round(day,1)}, AMOUNT: SGD{round(abs(difference),2)}")
        previous_day_value = cash_on_hand



