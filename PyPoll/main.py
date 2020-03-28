##Unit 3 Assignment: PyPoll
#Author: Dan Edie

'''
Task is to create a script that will read in data from a .csv file and perform analysis
on the records, including:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.
'''
#import modules
import os
import csv

#create variable pointing at .csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#create variables
vote_total = 0
voteDict = {}
can_names = []
high_vote = 0

#read in the .csv file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader) #skips header

    for vote in csvreader:
        
        if vote[2] not in can_names:
            can_names.append(vote[2])

            voteDict[vote[2]] = 0

        voteDict[vote[2]] += 1

        vote_total += 1

##Returning the results

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(vote_total))
print("-------------------------")

# Specify the file to write to
output_path = os.path.join("output", "poll_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    '''
    Write the output out. There has to be a more elegant way to print to terminal and 
    to a file as well; Google search returned some things, but I had trouble with them.
    Looking forward to seeing if the solution/comments on how to do so
    '''

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Total Votes: "+ str(vote_total)])
    csvwriter.writerow(["-------------------------"])

    '''
    Again, there has to be a more elegant way to do this (in the loop above)
    But, I had trouble coming up with a way to effectively get the information from
    the dictionary without knowing the key/s (for future elections)
    '''
    for canName in can_names:
      can_votes = voteDict[canName]
      vote_perc = round(can_votes/vote_total * 100, 3)

      csvwriter.writerow([canName + ": " + str(vote_perc) + "%" + " (" + str(can_votes) + ")"])
      print(canName + ": " + str(vote_perc) + "%" + " (" + str(can_votes) + ")")

      #check to see who got the highest total votes, and declare them the winner
      if can_votes > high_vote:
        high_vote = can_votes
        winner = canName

    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Winner: " + winner])
    csvwriter.writerow(["-------------------------"])

print("-------------------------")
print("Winner: " + winner)
print("-------------------------")