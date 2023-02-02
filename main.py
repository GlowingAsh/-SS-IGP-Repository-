import cash_on_hand, overheads, profit_loss

def main():
  """Function called main will inegrate the functions 
  called cash_on_hand, overheads, profit_loss"""
  
  # Variables are assigned to the various functions
  profit_losss = profit_loss.profit_loss_function()
  diff_cash = cash_on_hand.cash_on_hand_function()
  max_overhead_val = overheads.overheads_function()


  summary = max_overhead_val + '\n'

 # Check if diff_cash is empty
  if(len(diff_cash))==0:
 
 # If diff_cash is empty, add the cash surplus message to the summary
    summary += '[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY'

  else:
  # If diff_cash is not empty, add the diff_cash values to the summary
    for i in range(len(diff_cash)):
      summary +=  diff_cash[i] + '\n'
  
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
    
  #The content within the variable "summary" will be written in the text file file.write()
    file.write(summary)

main()