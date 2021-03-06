import csv
import os

# assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# create total vote counter
total_votes = 0

# create list of candidates
candidate_options = []

# create dictionary of candidates and votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results & read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # read & print header row
    headers = next(file_reader)

    for row in file_reader:
        # add to total vote count
        total_votes += 1
        # print candidate name for each row
        candidate_name = row[2]
        # append candidate name to candidate list if not part of list already
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            # begin tracking candidate's votes
            candidate_votes[candidate_name] = 0
        
        # add to candidate's vote count
        candidate_votes[candidate_name] +=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results)
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # loop through candidate list
    for candidate_name in candidate_votes:
        # retrieve candidate's vote count
        votes = candidate_votes[candidate_name]
        # calculate vote percentage
        vote_percentage = votes/total_votes * 100
        # print candidate name and vote percentage
        candidate_results = (f'{candidate_name}: received {vote_percentage:.1f}% ({votes})\n')
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
            
        # determine if candidate's votes are greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                
            # if true, sets winning_count = votes & winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            # sets winning_candidate equalt to candidate's name
            winning_candidate = candidate_name

    # create variable to hold winning candidate summary
    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')


    print(winning_candidate_summary)
    # save winning candidate results to text file
    txt_file.write(winning_candidate_summary)
