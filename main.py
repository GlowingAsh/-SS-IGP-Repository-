import cash_on_hand, overheads, profit_loss

def main():
  """
  Function called main will inegrate the functions 
  called cash_on_hand, overheads, profit_loss
  """
  
  # Variables are assigned to the various functions
  profit_losss = profit_loss.profit_loss_function()
  cash_diff = cash_on_hand.cash_on_hand_function()
  max_overhead_value = overheads.overheads_function()

  # Max_overhead_value will be assigned to the summary variable, and creating a new line
  summary = max_overhead_value + '\n'

  # Check if cash_diff is empty
  if(len(cash_diff))==0:
 
    # If diff_cash is empty, add the cash surplus message to the summary
    summary += '[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY'

  else:
    # If cash_diff is not empty, add the cash_diff values to the summary
    for i in range(len(cash_diff)):
      summary +=  cash_diff[i] + '\n'
  
  # Check if profit_loss is empty    
  if(len(profit_losss))==0:
  
    # If profit_loss is empty, add the profit surplus message to the sumary 
    summary += '[NET PROFT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY '
  
  else:
  # If profit_loss is not empty, add the profit_loss values to the summary
    for i in range(len(profit_losss)):
      summary +=  profit_losss[i] + '\n'
  
  # Importing path from pathlibrary
  from pathlib import Path
  
  # File path created to summary_report.txt
  fp = Path.cwd()/"summary_report.txt"

  # Text file will be opened in write mode and is encoded in UTF-8 format
  with fp.open(mode="w", encoding="UTF-8") as file:
    
    # The content within the variable "summary" will be written in the text file file.write()
    file.write(summary)

main()