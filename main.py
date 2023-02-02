import cash_on_hand,overheads, profit_loss

def main():
  diff_cash = cash_on_hand.cash_on_hand_function()
  max_overhead_val = overheads.overheads_function()
  profit_losss = profit_loss.profit_loss_function()

  summary = max_overhead_val + '\n'

  if(len(diff_cash))==0:
    summary += '[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY'
  else:
    for i in range(len(diff_cash)):
      summary +=  diff_cash[i] + '\n'
  if(len(profit_losss))==0:
    summary += '[NET PROFT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY '
  else:
    for i in range(len(profit_losss)):
      summary +=  profit_losss[i] + '\n'

  with open("summary_report.txt","a+") as f:
    f.write(summary) 
    
main()