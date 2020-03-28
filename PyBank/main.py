#Unit 3 Assignment: PyBank
#Author: Dan Edie

'''
Task is to create a script that will read in data from a .csv file and perform analysis
on the records, including:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The average of the changes in "Profit/Losses" over the entire period

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in losses (date and amount) over the entire period
'''
#import modules
import os
import csv

#create variable pointing at .csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Create variables
prev_month = 0
monthly_change = 0
tot_profit = 0
min_month = 0
min_value = float("inf") #infinity 
max_month = " "
max_value = 0
month_counter = 0

#read in the .csv file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader) #skips the header

    #walk through each month and budget value in the file
    for month, value in csvreader:
        curr_month = float(value) #Need to cast the profit/loss column as a float (accounts for any cents in future)
        tot_profit += curr_month #running total of profit or loss

        #Calculating the monthly change. Note: Can't do in first pass since first month has no previous data to compare with
        if month_counter != 0:
            tot_change = curr_month - prev_month #change between current month and previous month
            monthly_change += (tot_change)
            
            #compare the monthly change to the max and min values and store both the value and the month when 
            #passes math test
            if tot_change > max_value:
                max_value = tot_change
                max_month = month

            if tot_change < min_value:
                min_value = tot_change
                min_month = month

        prev_month = curr_month
        month_counter +=1


avg_change = monthly_change/(month_counter - 1)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month_counter))
print("Total: $" + str(round(tot_profit, 2)))
print("Average  Change: $" + str(round(avg_change, 2)))
print("Greatest Increase in Profits: " + str(max_month) + "   $" + str(round(max_value, 2)))
print("Greatest Decrease in Profits: " + str(min_month) + "   $" + str(round(min_value, 2)))

# Specify the file to write to
output_path = os.path.join("output", "budget_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["Total Months: "+ str(month_counter)])
    csvwriter.writerow(["Total: $" + str(round(tot_profit, 2))])
    csvwriter.writerow(["Average  Change: $" + str(round(avg_change, 2))])
    csvwriter.writerow(["Greatest Increase in Profits: " + str(max_month) + "   $" + str(round(max_value, 2))])
    csvwriter.writerow(["Greatest Decrease in Profits: " + str(min_month) + "   $" + str(round(min_value, 2))])