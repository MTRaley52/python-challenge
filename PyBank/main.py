# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# csvpath = "../Resources/accounting.csv"
#first attempt/csvpath = os.path.join('python', 'PyBank', 'budget_data.csv')
csvpath = os.path.join('budget_data.csv')
#C:\Users\mtral\python-challenge\PyBank\budget_data.csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

csv_header = next(csvreader)
  #print(f"CSV Header: {csv_header}")
for row in csvreader:
        #print(row)


    months = []
    revenue = []

with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile)