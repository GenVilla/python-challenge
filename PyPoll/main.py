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

winner_list = []

for name in winner_list:
    if max(candidate_votes) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]

if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

output_file = os.path.join('Output', 'election_results_' + str(filepath) +'.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in winner_list:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

with open(output_file, 'r') as readfile:
    print(readfile.read())








