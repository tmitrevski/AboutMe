import pandas as pd

budget_data=pd.read_csv('/Users/tmitrevski/Projects/public/code/python-homework/budget_data.csv', sep=',') #Read in the file from my local directory

months = len(budget_data.index) # Number of months is equal to the length of the number of indicies, assuming no date duplicates
total = budget_data['Profit/Losses'].sum() # Total is just the sum of all Profits and Losses

budget_data['Differences']=budget_data['Profit/Losses'].diff() # Add a column with the MTM differences of the Profits and Losses

average_change = budget_data['Differences'].mean() # Take the average of all of the differences

greatest_increase = budget_data.nlargest(1, 'Differences', keep='first') # Take the largest positive difference
greatest_decrease = budget_data.nsmallest(1, 'Differences', keep='first') # Take the largest negative difference

filename = "PyBank Output.txt"
PyBank_output = open(filename, "w+") #Open the file for read and write, should create it automatically if it doesn't exist.

PyBank_output.write("Financial Analysis\n") # Below here is writing to the file and string formatting
PyBank_output.write("---------------------------\n")

months_formatted_text = "Total Months: {}".format(months)
PyBank_output.write(months_formatted_text + "\n")

total_formatted_text = "Total: ${:,.2f}".format(total)
PyBank_output.write(total_formatted_text + "\n")

average_change_formatted_text = "Average Change: ${:,.2f}".format(average_change)
PyBank_output.write(average_change_formatted_text + "\n")

greatest_increase_formatted_text = "Greatest Increase in Profits: {} ${:,.2f}".format(greatest_increase['Date'].item(), greatest_increase['Differences'].item())
PyBank_output.write(greatest_increase_formatted_text + "\n")

greatest_decrease_formatted_text = "Greatest Decrease in Profits: {} ${:,.2f}".format(greatest_decrease['Date'].item(), greatest_decrease['Differences'].item())
PyBank_output.write(greatest_decrease_formatted_text  + "\n")

PyBank_output.seek(0) # Go back to the beginning of the file
print(PyBank_output.read()) # Read the file to the terminal

PyBank_output.close() # Close the file