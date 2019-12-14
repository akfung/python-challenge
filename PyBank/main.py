import csv
import os
#set empty array for csv and variables for tracking values
csv_array = []
total_profit = 0
greatest_increase = 0
greatest_increase_month = ''
greatest_decrease = 0
greatest_decrease_month = ''

csv_path = os.path.join(".", "budget_data.csv")
with open(csv_path, newline='', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
   
    #loop through rows in the CSV
    for row in csv_reader:
        #write rows to array to find total rows
        csv_array.append(row)
        #add the profit value to total_profit
        total_profit += float(row[1])
        #if statement to check if row has the highest or lowest profit/loss so far
        if float(row[1]) > greatest_increase:
            greatest_increase = float(row[1])
            greatest_decrease_month = row[0]
        elif float(row[1]) < greatest_decrease:
            greatest_decrease = float(row[1])
            greatest_decrease_month = row[0]

    #count total months and use to calculate avg profit
    total_months = len(csv_array)
    average_profit = total_profit/total_months
    #print all this shit
    print("Financial Analysis")
    print("-------------------")
    print("Total profit: {}".format(total_profit))
    print("Total Months: {}".format(total_months))
    print("Average Profit: {}".format(average_profit))
    print("Greatest increase: {} on {}".format(greatest_increase, greatest_increase_month))
    print("Greatest decrease: {} on {}".format(greatest_decrease, greatest_decrease_month))

#write to text file
#add each entry to new line for readability
file = open("financials.txt", "w")
file.write("Financial Analysis\n")
file.write("-------------------\n")
file.write("Total profit: {}\n".format(total_profit))
file.write("Total Months: {}\n".format(total_months))
file.write("Average Profit: {}\n".format(average_profit))
file.write("Greatest increase: {} on {}\n".format(greatest_increase, greatest_increase_month))
file.write("Greatest decrease: {} on {}\n".format(greatest_decrease, greatest_decrease_month))
file.close()