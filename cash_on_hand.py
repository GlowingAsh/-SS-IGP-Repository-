from pathlib import Path
import csv

def cash_on_hand_function():
    """
    created a cash on hand function to calculate cash_on_hand

    Function called cash_on_hand_function
    Will compute the difference in Cash-On-Hand if the current day is lower than the previous day
    """
<<<<<<< HEAD

=======
>>>>>>> 4a9dfa2adf13fe60eff88c2d11a737372fa63550
    # created a variable whereby the first day, previous day, will start from 0
    prev_day = 0
    
    # created a variable to calculate the cash deficit, if there was a cash deficit
    # the empty list would be used to store the cash deficit
    cash_deficit = []
    
    # create a file to csv file
    fp = Path.cwd()/"csv_reports\Cash_on_hand.csv"
    
    # opening the csv file on cash on hand to use the data
    with fp.open (mode="r", encoding="UTF-8", newline="") as file:
        
        reader = csv.reader(file)
        line_count = 0
        
        # loop through all the rows to execute the body of code once for each item
        for row in reader:

            # equility operator to compare if line_count equals to 0
            if line_count == 0:
<<<<<<< HEAD

                # increments the value by 1
=======
                # increments the row number
>>>>>>> 4a9dfa2adf13fe60eff88c2d11a737372fa63550
                line_count += 1
                prev_day = row[1]
             
            # Or else the follow code below will be activated    
            else:
                if (line_count > 1 and (int(row[1]) < int(prev_day))):
                    # use '.append' to append the cash deficit as a list back to the empty list
                    cash_deficit.append(f'[CASH DEFICIT] DAY: {row[0]}, AMOUNT: USD{int(prev_day)- int(row[1])}')
                # use int() to convert string to a float
                prev_day = int(row[1])
                # increments the row number
                line_count += 1

        # return keyword to return cash deficit together with f-string
        return cash_deficit
