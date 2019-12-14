import csv
import os
csv_array = []

csv_path = os.path.join(".", "budget_data.csv")
with open(csv_path, newline='', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    total_profit = 0
    #loop through rows in the CSV
    for row in csv_reader:
        #write rows to array to find total rows
        csv_array.append(row)
        #add the profit value to total_profit
        total_profit += float(row[1])
        
    total_months = len(csv_array)
    print(total_profit)
    print(total_months)
