"""
Write a program (doesn't have to be a function, but can be) that reads what's in sample.txt and prints it to the console.
"""

def readfile(my_file):
  file = open(my_file, "r")
  text = file.read()
  file.close()
  return text