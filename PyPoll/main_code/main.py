# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

poll_csv = os.path.join('..', 'Resources', 'election_data.csv')

#Create our function:
#find total number of votes cast
#find complete list of candidates who received votes
#find the percentage of votes each candidate won
#find the total number of votes each candidate won
#the winner of the election based on the popular vote
def print_votes(election_data):
    total_votes = 0
    total_candidates = set()
    votes_won = {}
    winner = {"name": "", "votes": 0}
    results_text = ""
    
    with open(poll_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        # Skip the header row
        next(csvreader)  
        
        for row in csvreader:
            #add to the total votes
            total_votes +=1
            
            #find total number of candidates
            candidates = str(row[2])
            total_candidates.add(candidates)
            total_candidates_count = len(total_candidates)
            
            #find the total number of votes each candidate won
            if candidates in votes_won:
                votes_won[candidates] +=1
            else:
                votes_won[candidates] = 1  

        #display the total votes
        results_text += f"Total Votes: {total_votes}\n"
        
        #find the percentage of votes each candidate won
        for candidate, votes in votes_won.items():
            percentage = (votes / total_votes)*100
            #display each candidates number and percentage of votes
            results_text += f"{candidate}: {percentage:.3f}% ({votes})\n"
            

    # Find the winner
    winner["name"] = max(votes_won, key=votes_won.get)
    winner["votes"] = votes_won[winner["name"]]
        
    #display the winner's name
    results_text += f"Winner: {winner['name']}\n"
    
    return results_text


#call the function
print_votes(poll_csv)
results_text = str(print_votes(poll_csv))
print(results_text)


#export as a text file
file_path = "../Analysis/results.txt"

with open(file_path, 'w') as file:
     file.write(results_text)