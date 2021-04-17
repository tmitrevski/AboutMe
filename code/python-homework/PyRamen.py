# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = str(Path.home())+'/Projects/public/resources/menu_data.csv'
sales_filepath = str(Path.home())+'/Projects/public/resources/sales_data.csv'

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list

with open(menu_filepath, 'r') as f:
    reader = csv.reader(f)
    reader.__next__()
    menu = list(reader)
# @TODO: Read in the sales data into the sales list

with open(sales_filepath, 'r') as f:
    reader = csv.reader(f)
    reader.__next__()
    sales = list(reader)
        

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for x in sales:

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    quantity = float(x[3])
    menu_item = x[4]

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if menu_item not in report:
        report[menu_item] = {"01-count": 0,
        "02-revenue": 0,
        "03-cogs": 0,
        "04-profit": 0
        }

    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for y in menu:

        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        item = y[0]
        price = float(y[3])
        cost = float(y[4])

        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        
        if menu_item == item:

            # @TODO: Print out matching menu data
            
            # ^^ Printing this spams the terminal on every match

            # @TODO: Cumulatively add up the metrics for each item key
            report[menu_item]["01-count"] += quantity
            report[menu_item]["02-revenue"] += price * quantity
            report[menu_item]["03-cogs"] += cost * quantity
            report[menu_item]["04-profit"] += profit * quantity

        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        
        # else:
        #    print("{menu_item} does not equal {item}! NO MATCH!")
        # ^^ Can't put this here. We are iterating through the sales list and then iterating that sales item against everything
        #    in the menu, every time. Printing this here spams the terminal. Would need a different approach.
            
    # @TODO: Increment the row counter by 1
    row_count += 1

# @TODO: Print total number of records in sales data

print(str(row_count) + "\n")


# @TODO: Write out report to a text file (won't appear on the command line output)
filename = "PyRamen Output.txt"
PyRamen_output = open(filename, "w+") #Open the file for read and write, should create it automatically if it doesn't exist.

PyRamen_output.write("Sales Report\n") # Below here is writing to the file and string formatting
PyRamen_output.write("---------------------------\n")

for sym, rec in report.items():
    PyRamen_output.write(sym + ":\n")
    for sym2, rec2 in rec.items():
        PyRamen_output.write(sym2 + ": " + str(rec2) + "\n")
    PyRamen_output.write("\n")       

PyRamen_output.seek(0) # Go back to the beginning of the file
print(PyRamen_output.read()) # Read the file to the terminal

PyRamen_output.close() # Close the file