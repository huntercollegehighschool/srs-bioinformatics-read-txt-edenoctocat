import os
program = input("A or B? ").upper()

while program not in ["A", "B"]:
  os.system('clear')
  print("Invalid input.")
  program = input("A or B? ").upper()

if program == "A":
  from Asampleread import readfile
  print(readfile("sample.txt"))

elif program == "B":
  import Baminoacids
  protein = "SKADYEK"
  print(Baminoacids.weightedstring(protein))
  