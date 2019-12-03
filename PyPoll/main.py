import os
import csv

filepath = os.path.join('Resources', 'election_data.csv')

poll = {}

total_votes = 0

with open(filepath, newline = 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1

candidate = []
candidate_votes = []
vote_percentage = []

for key in poll.items():
    candidate.append(key)

for value in poll.items():
    candidate_votes.append(value)

for n in candidate_votes:
    vote_percentage.append(n/total_votes * 100)








