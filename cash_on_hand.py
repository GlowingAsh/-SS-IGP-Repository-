from pathlib import Path
import csv

def cash_on_hand():
    """
    created a cash on hand function to calculate cash_on_hand
    """
    prev_day = 0
    #created a variable whereby the first day, previous day, will start from 0
    cash_deficit = []
    # created a variable to calculate the cash deficit, if there was a cash deficit
    with open ('csv_reports\Cash_on_hand.csv') as csv_file:
        # opening the csv file on cash on hand to use the data
        csv_Reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0

        for row in csv_reader:
            if lne_count == 0:
                line_count += 1
                prev_day = row[1]
            else:
                if (line_count > 1 and (int(row[1]) < int(prev_day))):
                    cash_deficit.append(f'[CASH DEFICIT] DAY: {row[0]}, AMOUNT: USD{int(prev_day)- int(row[1])}')
                prev_day = int(row[1])

                

