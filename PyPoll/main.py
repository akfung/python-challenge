import csv
import os

csv_path = os.path.join(".", "election_data.csv")
with open(csv_path, newline='', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)