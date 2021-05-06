# %%
# -*- coding: utf-8 -*-
"""Refresher activity.

This script will use variables, conditionals, lists, dicts, and functions
to print out different greetings for customers based on their
business tier (determined by revenue).
"""

# List of dicts
customers = [
    { "first_name": "Tom", "last_name": "Bell", "revenue": 0 },
    { "first_name": "Maggie", "last_name": "Johnson", "revenue": 1032 },
    { "first_name": "John", "last_name": "Spectre", "revenue": 2543 },
    { "first_name": "Susy", "last_name": "Simmons", "revenue": 5322 }
]

# @TODO Define a function that accepts a customer first_name, last_name, and
# revenue and returns a custom greeting with the full name.
# Use these ranges to determine the business tier (and corresponding message)
# for each customer.
#   Platinum = 3001+
#   Gold = 2001-3000
#   Silver = 1001-2000
#   Bronze = 0-1000
def create_greeting(first_name, last_name, revenue):
    # @TODO: YOUR CODE HERE!
    if revenue < 0:
        tier = "None"
    elif revenue >= 0 and revenue <= 1000:
        tier = "Bronze"
    elif revenue >= 1001 and revenue <= 2000:
        tier = "Silver"
    elif revenue >= 2001 and revenue <= 3000:
        tier = "Gold"
    else:
        tier = "Platinum"
    greeting = "Welcome " + first_name + " " + last_name + ". You are a " + tier + " level member."
    return greeting

# @TODO: Loop through the list of customers and use your function to print
# custom greetings for each customer.
for i in range(len(customers)):
    first_name = customers[i]["first_name"]
    last_name = customers[i]["last_name"]
    revenue = customers[i]["revenue"]
    print(create_greeting(first_name, last_name, revenue))
# %%
# -*- coding: utf-8 -*-
"""
Zero-Coupon Bond Valuation.

This script will calculate the present value of zero-coupon bonds, compare the present value to the price of the bond, and determine the corresponding action (buy, not buy, neutral).
"""

# @TODO: Create a function to calculate present value

def present_value(future_value, discount_rate, compounding_periods, years):
    PV = future_value*(1/((1+discount_rate/compounding_periods)**(compounding_periods*years)))
    return PV




# Intialize the zero-coupon bond parameters, assume compounding period is equal to 1
price = 700
future_value = 1000
discount_rate = .1
compounding_periods = 1
years = 5

# @TODO: Call the calculate_present_value() function and assign to a variables
Present_Value = present_value(future_value, discount_rate, compounding_periods, years)
print(round(Present_Value, 2))
# @TODO: Determine if the bond is worth it
if Present_Value > price:
    print("Purchase the Bond!")
elif Present_Value < price:
    print("Do not purchase the Bond!")
else:
    print("I do not feel strongly about this one way or the other.")

# %%
# -*- coding: utf-8 -*-
"""Student Activity: Financial Analysis using NPV.

This script will choose the optimal project scenario to
undertake based on max NPV values.
"""

# @TODO: Import the NumPy Financial (numpy_financial) library

import numpy_financial as npf

# @TODO: You may need to run `pip install numpy-financial` in your terminal to install the library

# Discount Rate
discount_rate = .1

# Initial Investment, Cash Flow 1, Cash Flow 2, Cash Flow 3, Cash Flow 4
cash_flows_conservative = [-1000, 400, 400, 400, 400]
cash_flows_neutral = [-1500, 600, 600, 600, 600]
cash_flows_aggressive = [-2250, 800, 800, 800, 800]

# @TODO: Initialize dictionary to hold NPV return values
npv_dict = {}

# @TODO: Calculate the NPV for each scenario
npv_dict["Conservative"] = npf.npv(discount_rate, cash_flows_conservative)
npv_dict["Neutral"] = npf.npv(discount_rate, cash_flows_neutral)
npv_dict["Aggressive"] = npf.npv(discount_rate, cash_flows_aggressive)

# @TODO: Manually Choose the project with the highest NPV value

max_key = max(npv_dict, key=npv_dict.get)
max_value = round(npv_dict[max_key],2)
print(max_key)
print(max_value)
print(f"The project scenario with the max NPV value is {max_key} with a NPV of {max_value}")
# %%
# -*- coding: utf-8 -*-
"""Student Do: E-Commerce Traffic.

This script will parse through a text file and sum the total
number of customers and the count of days in the text file to
calculate the daily average of customer traffic for an e-commerce
business.
"""

# @TODO: From the pathlib library, import the main class Path
from pathlib import Path

# @TODO: Check the current directory where the Python program is executing from

# @TODO: Set the path using Pathlib
filepath = Path('customer_traffic.txt')
# Initialize variables
customer_total = 0
day_count = 0

# @TODO: Open the file in "read" mode ('r') and store the contents in the variable 'file'
with open(filepath, 'r') as file:
    # @TODO: Parse the file line by line
    for line in file:

        # @TODO: Convert the number in the text file from string to int (allows for numerical calculations)
        customer_total += int(line)
        day_count += 1
        # @TODO: Sum the total and count of the numbers in the text file



# @TODO: Print out customer_total and day_count
print(f"Customer Total: {customer_total}\nDay Count: {day_count}")



# @TODO: Calculate the average

average = customer_total/day_count

# @TODO: Set output file name
output_file_name = 'Assignment.txt'

# @TODO: Open the output path as a file object
with open(output_file_name, 'w') as file:

    # @TODO: Write daily_average to the output file, convert to string
    file.write(str(average))

# %%
