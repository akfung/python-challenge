#these packages aren't sending their best people
import csv
import os

vote_count = 0
candidate_list = []

#look out its the csv caravan coming to take our jobs
csv_path = os.path.join(".", "election_data.csv")

# "we can't just open up our borders or our CSVs" - Sean Hannity probably
with open(csv_path, newline='', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        #count the number of voters 
        vote_count += 1
        #if statement to add cadidates to a list if they haven't come up yet or aren't named andrew yang
        if not(row[2] in candidate_list):
            candidate_list.append(row[2])
    print(candidate_list)
    print(vote_count)