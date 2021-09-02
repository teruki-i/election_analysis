# The data we need to retrieve.
# 1. total votes casted
# 2. complete list of candidates who received votes
# 3. percentages of votes won by each candidate
# 4. total number of votes won by each candidate
# 5. election winner based on popular vote

import csv
import os

# assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open election results & read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Print each row in the CSV file.
    # for row in file_reader:
        #print(row)
    
    # read & print header row
    headers = next(file_reader)
    print(headers)




# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     #txt_file.write("Counties in the Election \n")
     #txt_file.write("------------------------ \n")
     #txt_file.write("Arapahoe \n")
     #txt_file.write("Denver \n")
     #txt_file.write("Jefferson")

