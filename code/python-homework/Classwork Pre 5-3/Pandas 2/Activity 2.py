# %%
# Import pandas, pathlib, and numpy libraries
import pandas as pd
from pathlib import Path
import numpy as np
import random
import os
print(os.getcwd())
# %%
# Use the Pathlib libary to set the path to the CSV
path = Path('./Pandas 2/people.csv')
# %%
# Use the file path to read the CSV into a DataFrame and display a few rows
df = pd.read_csv(path)
df.head()
# %%
# Use the `columns` attribute to output the column names
print(df.columns)
# %%
# Use the `dtypes` attribute to output the column names and data types
print(df.dtypes)
# %%
# Set the `columns` attribute to a new list of column names
df.columns = ["Person_ID", "First_Name", "Last_Name", "Email", "Gender", "University", "Occupation", "Salary"]
df.head()
# %%
# Use the `rename` function and set the `columns` parameter to a dictionary of new column names

# %%
# Use a list of re-ordered column names to alter the column order of the original DataFrame
df = df.reindex(columns=["Person_ID", "Last_Name", "First_Name", "Gender", "University", "Occupation", "Salary", "Email"])
# %%
# Use the `randint` function to randomly generate an `Age` from 22 to 65 for 1000 rows
df['Age'] = np.random.randint(22, 65, 1000)
df['Age_Copy'] = df['Age']
df.head()
# %%
# Use the `drop` function to delete the newly created `Age` column
df.drop('Age_Copy', axis=1, inplace = True)
df.head()
# %%
# Save the DataFrame to the `Resources` folder
output_file_name = './Pandas 2/dataframe.csv'
df.to_csv(output_file_name)
# %%
# ----------------------------------------------------------------------------------------------
# %%
# Import libraries and dependencies
import pandas as pd
from pathlib import Path
import numpy as np
# %%
# Use the Pathlib libary to set the path to the CSV
path = Path('./Pandas 2/people_cleansed.csv')
# %%
# Read in the CSV as a DataFrame
df = pd.read_csv(path)
# %%
# Select the first row of the DataFrame
df.iloc[0]
# %%
# Select the first 10 rows of the DataFrame
df.iloc[0:10]
# %%
# Select the last row of the DataFrame
df.iloc[-1]
# %%
# Select the second column of the DataFrame
df.iloc[:,1]
# %%
# Select the last column of the DataFrame, with all rows
df.iloc[:,-1]
# %%
# Select the first three columns of the DataFrame, with all rows
df.iloc[:,0:3]
# %%
# Select the 1st, 3th, 5th, 7th rows of the 2nd, 4th, and 6th columns.
df.iloc[[0,2,4,6],[1,3,5]]
# %%
# Select the first 5 rows of the 3rd, 4th, and 5th columns of the DataFrame
df.iloc[0:5,[2,3,4]]
# %%
# Modify the 'first_name' column value of the first row
df.iloc[0,2] = 'TaRa'
# %%
# Set the index as the 'First_Name' column
df.set_index('First_Name', inplace=True, drop = False)
df.head()
# %%
# Sort the index
df.sort_index(inplace=True)
df.head()
# %%
# Select the row with the index 'Andrew'
df.loc['Andrew']
# %%
# Slice the data to output the range of rows between 'Andrew' and 'Vonnie' using `loc`.
df.loc['Andrew':'Vonnie']
# %%
# Select the rows where `Gender` is equal to 'Male' using `loc`.
df.loc[df['Gender'] == 'Male']
# %%
# Change the `First_Name` value of the rows with 'Aaron' as the `First_Name` index to 'Arod'
df.loc['Aaron', 'First_Name'] = 'Arod'
df.head()
# %%
# import dependencies
import pandas as pd
from pathlib import Path
import numpy as np
# %%
# Use the Pathlib libary to set the path to the CSV
path = Path('./Pandas 2/people_cleansed.csv')
# %%
# Use the file path to read the CSV into a DataFrame and display a few rows
df = pd.read_csv(path)
# %%
# Create the variable bins to define our bounds for when we cut the dataframe.
bins = [0, 30000, 70000, 100000, 200000]

# Create names for the bins
labels = ['Low', 'Moderate', 'Above Average', 'High']
# %%
# Add a column named "Salary Level" to people_df and slice the data into the bins
df['Salary Level'] = pd.cut(df['Salary'], bins, labels = labels)

# %%
df.head()
# %%
