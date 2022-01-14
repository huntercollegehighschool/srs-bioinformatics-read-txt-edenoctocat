"""
Define a function weightedstring that takes a string input protein. The function returns the weighted string of that protein based on masstable.txt.

weightedstring should read from masstable.txt. It's helpful to have those masses in a dictionary.
"""

def weightedstring(protein):
  file = open("masstable.txt", "r")
  masstable = {}
  for item in file.read().split("\n"):
    items = item.split(" ")
    masstable.update({items[0]:items[1]})
  file.close()
  weightedstr = 0
  for aa in protein:
    weightedstr += float(masstable[aa])
  return weightedstr
