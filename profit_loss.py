from pathlib import Path
import csv

fp = Path.cwd()/"Profit_Loss.csv"

with fp.open(mode="r", emcoding="UTF-8", newline="") as file:
  
