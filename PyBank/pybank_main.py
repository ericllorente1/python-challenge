#create several lists to separate the data for calculations
import csv
import os 
file = os.path.join('Resources', 'budget_data.csv') 
output_file = os.path.join('analysis', 'results.txt')
months = []
#all profit changes will be stored in all_changes to calculate the change for each month and the average change for the data
all_changes = []
#the profit for every month will be stored in profits_list and added up at the end to find the total profit for the data
profits_list = []
#start code to read csv file 
with open(file, "r") as csv_file:
    content = csv.reader(csv_file, delimiter=",")
    #skip the first row because it has no usable data
    header = next(content)
# -------------------start of loop-------------------------------------------------------------------
    #make loop for every line in the csv file and store the contents in lists
    for line in content:
        #add month to months list
        months.append(line[0])
        #add the iteration's profit to the profits list
        profits_list.append(int(line[1]))
        #total profit, average change, number of months, max and min will be calculated with lists outside of loop
#-----------------------------------end of loop ------------------------------------------------------------
#make a loop to find the monthly change using the profits_list
#use the length of the profits list to determine the number of iterations
#Since iterations start at 0, subtract 1 to have the correct number of iterations
for element in range(len(profits_list) - 1):
            #subtract the profit of the current element to the next element and add result to all changes list
            all_changes.append(float(profits_list[element + 1] - profits_list[element]))
#-----------------------------------end of loop---------------------------------------------------------
#calculate average change for all profit changes using all changes list
average_change = round(sum(all_changes)/len(all_changes), 2)
#calculate total number of months using the lenght of months list
months_total = len(months)
#calculate the total profit using the sum of the profits list
total_profit = sum(profits_list)
#calculate the greatest increase and decrease by using the max and min functions on the all_changes list
#convert the data type to integers since they were floats to calculate the average
greatest_increase = int(max(all_changes))
greastest_decrease = int(min(all_changes))
#create an index number to match the month of the change in the months list
max_index = all_changes.index(greatest_increase)
min_index = all_changes.index(greastest_decrease)
#use the index number to find the month that matches the max and min
#add 1 to each index to match the correct month
max_match = months[max_index + 1]
min_match = months[min_index + 1]
#-----------------------print results------------------------------------
printed_results = (
'Financial Analysis \n'
'---------------------------- \n'
f"Total Months: {months_total} \n"
f"total: ${total_profit} \n"
f"Average Change: ${average_change} \n"
f"Greatest Increase in Profits: {max_match} (${greatest_increase}) \n"
f"Greatest Decrease in Profits: {min_match} (${greastest_decrease}) \n"
)
print(printed_results)
#------------------------create txt file and print to terminal----------------------
with open(output_file, 'w') as outfile:
    outfile.write(printed_results)


        


    

            
