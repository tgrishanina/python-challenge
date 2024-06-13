# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

bank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#Create our function:
#Find total months in dataset
#find net profit/ losses over entire period
#find changes in profits/ losses over entire period, then avg of those changes
#greatest increase in profits (date and amount) over entire period
#greatest decrease in profits (date and amount) over entire period.
def print_records(budget_data):
    total_months = 0
    net_profits = 0
    changes = []
    dates = []
    prev_profit = 0
    
    with open(bank_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skip the header row
        
        for row in csvreader:
            #add to the total months
            total_months += 1
            profit = float(row[1])
            #add the profit from each row to get the total profit
            net_profits += profit
            
            # Skip the first month as there is no previous profit
            if total_months > 1:  
                change = profit - prev_profit
                #add the difference between profits to our "changes" list
                changes.append(change)
                #add the corresponding date to our "dates" list
                dates.append(row[0])
            
            # Update prev_profit for the next iteration
            prev_profit = profit  
        
        #calculate average change
        avg_change = sum(changes) / (total_months - 1)
        #find greatest profits
        profits_increase = max(changes)
        #find greatest losses
        profits_decrease = min(changes)
        #find date for greatest profits
        increase_date = dates[changes.index(profits_increase)]
        #find date for greatest losses
        decrease_date = dates[changes.index(profits_decrease)]

        #return our calculations as a string so we can export them later
        results_text = f"""
        Total Months: {total_months}
        Total: ${net_profits}
        Average Change: ${avg_change:.2f}
        Greatest Increase in Profits: {increase_date} (${profits_increase})
        Greatest Decrease in Profits: {decrease_date} (${profits_decrease})
        """
    
        return results_text


with open(bank_csv, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    data = [row for row in csvreader]

#call the function
print_records(data)

results_text = str(print_records(data))

#export the results
file_path = "../Analysis/results.txt"

with open(file_path, 'w') as file:
    file.write(results_text)

#print the results in the terminal
print(results_text)