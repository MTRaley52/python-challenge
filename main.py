# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# csvpath = "../Resources/accounting.csv"
#attempt/csvpath = os.path.join('python', 'PyBank', 'budget_data.csv')
csvpath = os.path.join('budget_data.csv')
#C:\Users\mtral\PythHW\HW3\PyBank2



with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    print(type(csvreader))
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
Months = []
NetRev = []

for row in csvreader:
      Months.append(row[0])
      NetRev.append(int(row[1]))

# print(Months)
# # #Objectives:
# # #The total number of months included in the dataset
# # #The net total amount of "Profit/Losses" over the entire period
# # #The average of the changes in "Profit/Losses" over the entire period
# # #The greatest increase in profits (date and amount) over the entire period
# #The greatest decrease in losses (date and amount) over the entire period
# # #two columns: Date and Profit/Losses


#empty list to store first column then second column of data   
Months = []
NetRev = []

with open(csvpath, 'r') as csvfile:
     csvread = csv.reader(csvfile)

#The total number of months included in the dataset
total_months = len(Months)
print(total_months)
#Finding the largest positive and negative numbers
greatest_inc = NetRev[0]
greatest_dec = NetRev[0]
TotalRevenue = 0

#The net total amount of "Profit/Losses" over the entire period
for p in range(len(NetRev)):
      if NetRev[p] >= greatest_inc:
          greatest_inc = NetRev[p]
          greatest_inc_Month = Months[p]
      elif NetRev[p] <= greatest_dec:
          greatest_dec = NetRev[p]
          greatest_dec_Month = Months[p]
      TotalRevenue += NetRev[p]

# # #The greatest increase in profits (date and amount) over the entire period
NetRevDelta = []
for x in range(1, len(NetRev)):
          NetRevDelta.append((int(NetRev[x]) - int(NetRev[x-1])))
          greatest_INC = max(NetRevDelta) #greatest delta increase
          greatest_DEC = min(NetRevDelta) #greatest delta decrease

Delta_average = sum(NetRevDelta) / len(NetRevDelta)

  
#The average of the changes in "Profit/Losses" over the entire period
#CAN ALSO USE THIS: average_change = round(TotalRevenue/total_months, 2)

output_dest = os.path.join('..','PyBank2')

# Print the Final Results
print("Financial Analysis")

print("....................................................................................")

print("total months: " + str(total_months))

print("Total: " + "$" + str(sum(NetRev)))

print("Average change: " + "$" + str(Delta_average))

print("Greatest Increase in Profits: " + str(Months[NetRevDelta.index(max(NetRevDelta))+1]) + " " + "$" + str(greatest_INC))

print("Greatest Decrease in Profits: " + str(Months[NetRevDelta.index(min(NetRevDelta))+1]) + " " + "$" + str(greatest_DEC))
 
#  Export a text file with the results

file = open("pybankresults.txt","w")
#w = writing
file.write("Financial Analysis" + "\n")
#\n move a row down 
file.write("...................................................................................." + "\n")

file.write("total months: " + str(total_months) + "\n")

file.write("Total: " + "$" + str(sum(NetRev)) + "\n")

file.write("Average change: " + "$" + str(Delta_average) + "\n")

file.write("Greatest Increase in Profits: " + str(Months[NetRevDelta.index(max(NetRevDelta))+1]) + " " + "$" + str(greatest_INC) + "\n")

file.write("Greatest Decrease in Profits: " + str(Months[NetRevDelta.index(min(NetRevDelta))+1]) + " " + "$" + str(greatest_DEC) + "\n")

file.close()
