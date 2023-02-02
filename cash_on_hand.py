from pathlib import Path
import csv

def cash_on_hand():
    prev_day = 0
    cash_deficit = []
    with open ('csv_reports\Cash_on_hand.csv') as csv_file:
        csv_Reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0

        for row in csv_reader:
            if lne_count == 0:
                line_count += 1
                prev_day = row[1]

