#these packages aren't sending their best people
import csv
import os

total_vote_count = 0
candidate_list = []
vote_per_candidate = []
popular_vote = []

#look out its the csv caravan coming to take our jobs
csv_path = os.path.join(".", "election_data.csv")

# "we can't just open up our borders or our CSVs" - Sean Hannity probably
with open(csv_path, newline='', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        #count the number of voters 
        total_vote_count += 1
        #if statement to add cadidates to a list if they haven't come up yet or aren't named andrew yang
        if not(row[2] in candidate_list):
            candidate_list.append(row[2])
            #add a 0 entry to list for tracking that candidate's votes
            vote_per_candidate.append(0)
        #add +1 to that candidate's vote total that tracks with their index 
        vote_per_candidate[candidate_list.index(row[2])] +=1 
    #divide vote per candidate by total vote to find popular vote because fuck me if I'm gonna calculate electoral votes
    for vote in vote_per_candidate:
        popular_vote.append(round(vote*100/total_vote_count, 5))
        #find index of highest popular vote and look up that index in candidate list
        winner = candidate_list[popular_vote.index(max(popular_vote))]
    print("Election Results")
    print("-------------------------")
    print("Total Votes: {}".format(total_vote_count))
    #loop for candidate stats
    for i in range(0,len(candidate_list)):
        print("{}: {}% ({})".format(candidate_list[i], popular_vote[i], vote_per_candidate[i]))
    print("-------------------------")
    print("The winner is {}".format(winner))
    print("-------------------------")

    