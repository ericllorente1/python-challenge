import csv
import os
#use os.path.join to create a path for the file (as provided by tutor Limei Hou)
file = os.path.join('Resources','election_data.csv')
#create an output path for the output file
outfile_path = os.path.join('analysis', 'Poll_results.txt')
#to calculate the total number of votes, create a list of candidate column
vote = []
#create a list to store all total votes for each candidate
totals_list = []
#-----------------start of loop------------------
#make a loop to append the vote list for every row in csv file
with open(file,'r') as csv_file:
    data = csv.reader(csv_file, delimiter=",")
    header = next(data)
    
    for x in data:
        vote.append(x[2])
    
#-----------------end of loop---------------------
#use dictionary comprehesion to create keys for every unique value
#the logic behind it is that keys cannot duplicate
#https://www.geeksforgeeks.org/python-initialize-a-dictionary-with-only-keys-from-a-list/
#every key will have a list that will later be appended with every vote for each candidate
c_dict = {key: [] for key in vote}
#create a list of unique values with the keys of the dictionary
#https://datatofish.com/dictionary-keys-as-list/ 
uniques = list(c_dict.keys())
#abbreviate names for reference later
charles = uniques[0]
diana = uniques[1]
raymon = uniques[2]
#Calculate total votes for entire election by counting the length of the vote list
total_votes = len(vote)
#-------------------------start of 2nd loop-------------------------------
#loop through data again and append the list for each key with the ids of voters
#each id number will represent a vote for a respective candidate
with open(file, "r") as csv_file:
    data = csv.reader(csv_file, delimiter=",")
    header = next(data)
    
    for y in data:
        if y[2] == charles:
            c_dict[charles].append(y[0])
        elif y[2] == diana:
            c_dict[diana].append(y[0])
        elif y[2] == raymon:
            c_dict[raymon].append(y[0])
#-----------------------end of 2nd loop--------------------------------------
#calculate total votes  for each candidate using the lenght of the list for each candidate
charles_total = len(c_dict[charles])
diana_total = len(c_dict[diana])  
raymon_total = len(c_dict[raymon])
#calculate percentages for each candidate
c_percent = round(float((charles_total/total_votes))*100, 3)
d_percent = round(float((diana_total/total_votes))*100, 3)
r_percent = round(float((raymon_total/total_votes))*100, 3)
#append totals_list using the same indexes as candidates list
#the order is important to later match the total to its respective candidate and determine the winner
totals_list.append(charles_total)
totals_list.append(diana_total)
totals_list.append(raymon_total)
#calculate most votes
most_votes = max(totals_list)
#find the index of the most votes to match the winning candidate
most_index = totals_list.index(most_votes)
winner = uniques[most_index]
#-------------------------printed statement-------------------------------------- 
#store the printed script in a variable to export to a file later (as advice by tutor)
printed_results = (
'Election Results \n'
'-------------------------- \n'
f'Total Votes: {total_votes} \n'
'-------------------------- \n'
f'{charles}: {c_percent}% ({charles_total}) \n'
f'{diana}: {d_percent}% ({diana_total}) \n'
f'{raymon}: {r_percent}% ({raymon_total}) \n'
'-------------------------- \n'
f'Winner: {winner} \n'
'-------------------------- \n'
)
print(printed_results)
#--------------export file----------------------
#export results into a txt file
with open(outfile_path, 'w') as outfile:
    outfile.write(printed_results)