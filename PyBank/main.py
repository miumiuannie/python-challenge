# Modules
import os
import csv

# Variables to Track
date_list = []
profit_losses_list = []
total_months = 0
total_revenue = 0
value = 0
change = 0 

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    first_row = next(csvreader)
    total_months += 1
    # Loop through all the rows of data we collect
    for row in csvreader:

        # Calculate the totals
        date_list.append((row[0]))
        total_months += 1
        total_revenue += int(row[1])
        #total_revenue += 1
        #profit_losses_list.append(float(row[1]))
    
    # Build list of Profit/Losses changes month to month and calculate change
        change = int(row[1])-value
        profit_losses_list.append(change)
        value = int(row[1])
        average_change = sum(profit_losses_list)/len(profit_losses_list)
    
    # Determine the greatest increase and greatest decrease 
    greatest_increase = max(profit_losses_list)
    greatest_index = profit_losses_list.index(greatest_increase)
    greatest_date = date_list[greatest_index] 

    greatest_decrease = min(profit_losses_list)
    worst_index = profit_losses_list.index(greatest_decrease)
    worst_date = date_list[worst_index]
 
    # Show Output
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_revenue}")
    print(f"Average Change:${average_change}")
    print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})") 
    print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

    
    # create a path to a text file in the Output folder
    output_path = os.path.join("Output", "Financial_Analysis.txt")
    
    # Write the results into the text file
    with open(output_path, 'w', newline='') as text_file:  
        output = open("Financial_Analysis.txt", "w")
    line1 = "Financial Analysis"
    line2 = "---------------------"
    line3 = str(f"Total Months: {str(total_months)}")
    line4 = str(f"Total: ${str(total_revenue)}")
    line5 = str(f"Average Change: ${str(round(average_change,2))}")
    line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
    line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
    output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))