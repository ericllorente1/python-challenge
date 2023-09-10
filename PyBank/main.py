
import csv

margins = { }
months = [ ]
total_profit = 0
total_margin = []
with open('budget_data.csv', "r") as csv_file:
    #read csv file after every iteration
    csv_reader = csv.reader(csv_file)
    #skip the header 
    next(csv_reader)
    #for every line in the file loop
    for line in csv_reader:
        print(line)
        # #Create a dictionary using the profit amount as key to later print the corresponding month
        # margins[date[0]] = {date[1]: date[0]}
        # #create a list for every months to count the number of months at the end of the loop 
        # months.append(date[0])
        # #define profit offset to later calculate the profit change for first row
        # profit_offset = 0
        # #calculate the total_profit
        # total_profit += int(date[1])
        # #calculate monthly profit change by defining a variable for the current and previous month
        # if date == 1:
        #     #conditional for first row since it will not have a month that precedes it. 
        #     total_margin.append(int(date[1]))
        #     print(total_margin)
        
    # else:
    #     current_month = int(date[1]) 
    #     previous_month =    
    # #calculate the profit change by subtracting previous month from current month
    # profit_margin = float(current_month - previous_month)
    # #store the profit margin in a list that will be summed at the end of the loop to get the total profit margin for the data
    # total_margin.append(profit_margin)
    # #assign current month's profit to previous month for the next date iteration 
    
    
    # print(total_margin)
   

        