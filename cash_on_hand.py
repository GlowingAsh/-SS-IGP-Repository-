from pathlib import Path
import csv

def cash_on_hand_function():
    """
    Function called cash_on_hand_function
    Will compute the difference in Cash-On-Hand if the current day is lower than the previous day
    """

    # Created a variable to calculate the cash deficit, if there was a cash deficit
    # The empty list would be used to store the cash deficit
    cash_deficit = []
    
    # Create a file to csv file
    fp = Path.cwd()/"csv_reports\Cash_on_hand.csv"
    
    # Opening the csv file on cash on hand to use the data
    with fp.open (mode="r", encoding="UTF-8", newline="") as file:
        
        reader = csv.reader(file)
        line_count = 0
        
        # Loop through all the rows to execute the body of code once for each item
        for row in reader:

            # Equility operator to compare if line_count equals to 0
            if line_count == 0:

                # Increments the value by 1
                line_count += 1
                prev_day = row[1]
             
            # Or else the follow code below will be activated    
            else:
                if (line_count > 1 and (int(row[1]) < int(prev_day))):
                    
                    # Use '.append' to append the cash deficit as a list back to the empty list
                    cash_deficit.append(f'[CASH DEFICIT] DAY: {row[0]}, AMOUNT: USD{int(prev_day)- int(row[1])}')
               
                # Use int() to convert string to a float
                prev_day = int(row[1])

                # Increments the row number
                line_count += 1

    # Return keyword to return cash deficit together with f-string
    return cash_deficit
