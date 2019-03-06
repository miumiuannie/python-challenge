# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Set the total number of votes
    total_votes = 0

    # List of name of the candidates
    candidates_list = []
    candidates_name = []

    # Set the vote counter and percentage 
    candidates_vote = [0, 0, 0, 0]
    candidates_vote_percent = [0, 0, 0, 0]
    candidates_winner = []

    # Loop through entire file to calculate total votes
    for row in csvreader:
        total_votes += 1
        candidates_list.append(str(row[2]))

for row[2] in candidates_list:
     if row[2] not in candidates_name:
        candidates_name.append(row[2])
     if row[2] == candidates_name[0]:
        candidates_vote[0] += 1
     elif row[2] == candidates_name[1]:
        candidates_vote[1] += 1
     elif row[2] == candidates_name[2]:
        candidates_vote[2] += 1
     elif row[2] == candidates_name[3]:
        candidates_vote[3] += 1

# Calculate the Percentage
candidates_vote_percent[0] = round(100 * (candidates_vote[0] / total_votes), 4)
candidates_vote_percent[1] = round(100 * (candidates_vote[1] / total_votes), 4)
candidates_vote_percent[2] = round(100 * (candidates_vote[2] / total_votes), 4)
candidates_vote_percent[3] = round(100 * (candidates_vote[3] / total_votes), 4)

# Determin the winner
if candidates_vote[0] == max(candidates_vote[0], candidates_vote[1], candidates_vote[2], candidates_vote[3]):
    candidates_winner = candidates_name[0]
elif candidates_vote[1] == max(candidates_vote[0], candidates_vote[1], candidates_vote[2], candidates_vote[3]):
    candidates_winner = candidates_name[1]
elif candidates_vote[2] == max(candidates_vote[0], candidates_vote[1], candidates_vote[2], candidates_vote[3]):
    candidates_winner = candidates_name[2]
elif candidates_vote[3] == max(candidates_vote[0], candidates_vote[1], candidates_vote[2], candidates_vote[3]):
    candidates_winner = candidates_name[3]

# Show Output
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
print(f"{candidates_name[0]}: {candidates_vote_percent[0]}% ({candidates_vote[0]})")
print(f"{candidates_name[1]}: {candidates_vote_percent[1]}% ({candidates_vote[1]})")
print(f"{candidates_name[2]}: {candidates_vote_percent[2]}% ({candidates_vote[2]})")
print(f"{candidates_name[3]}: {candidates_vote_percent[3]}% ({candidates_vote[3]})")
print("-----------------------------")
print(f"Winner: {candidates_winner}")

# Create a text file
output_path = os.path.join("Output", "Election_Results.txt")

# Write the results into the text file
with open(output_path, 'w', newline='') as text_file:
    f = open ("Election_Results.txt","w")
    f.write("Election Results")
    f.write("-----------------------------")
    f.write(f"Total Votes: {total_votes}")
    f.write("-----------------------------")
    f.write(f"{candidates_name[0]}: {candidates_vote_percent[0]}% ({candidates_vote[0]})")
    f.write(f"{candidates_name[1]}: {candidates_vote_percent[1]}% ({candidates_vote[1]})")
    f.write(f"{candidates_name[2]}: {candidates_vote_percent[2]}% ({candidates_vote[2]})")
    f.write(f"{candidates_name[3]}: {candidates_vote_percent[3]}% ({candidates_vote[3]})")
    f.write("-----------------------------")
    f.write(f"Winner: {candidates_winner}")
