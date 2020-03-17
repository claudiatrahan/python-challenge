#dependencies
import csv
import os

# input
csvpath = os.path.join('..','Raw_Data','election_data.csv')

poll ={}
total_votes = 0
candidates = []
candidates_list = []
candidates_votes = []
num_votes = []
total_votes = 0

with open(csvpath) as election_file:
    reader = csv.reader(election_file, delimiter=',')
    print(reader)
    csv_header = next(reader)
    for line in reader:
        total_votes += 1
        candidates_votes.append(line[2])
