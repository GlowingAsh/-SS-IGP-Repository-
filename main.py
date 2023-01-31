# Code will connect all the three different functions into one file

import cash_on_hand, overheads, profit_loss

def main():
  """
  Function will integrate the different different functions higest_overheads, cash_on_hand and profitloss function
  """
  overheads.highest_overhead()
  cash_on_hand.cash_on_hand_function()
  profit_loss.profitloss_function()
  
  return main()


from pathlib import Path
fp = Path.cwd()/"summary_report.txt" 

with fp.open(mode="w", encoding="UTF-8") as file:
  file.write(f"{main()}")
