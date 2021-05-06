# %%
# initial imports
from pathlib import Path
import pandas as pd
#%%
# set the file path
path = Path('amd_stock_data.csv')
# create a Pandas dataframe from a csv file
df = pd.read_csv(path, header=None)
# get the first 10 rows from the dataframe
df.head(10)
# set colum names
df.columns = ["Date", "Close", "Volume", "Open", "High", "Low"]

# recreate the dataframe


# add columns names

# get the first 10 rows from the dataframe
df.head(10)
# get the bottom 10 rows from the dataframe
df.tail(10)
# %%
# Import Libraries
#import pandas as pd
#from pathlib import Path

path = Path('stock_data.csv')
#Load CSV data into Pandas using read_csv.
df = pd.read_csv(path)
#Identify the number of rows and columns in the DataFrame, otherwise known as its shape/structure.
print(df.shape)
#Generate a sample of the data to visually ensure data has been loaded in correctly.
df.sample(5)
#Identify the number of records in the DataFrame, and compare it with the number of rows in the original file.
df.count()
#Identify null records by calculating average percent of nulls for each Series. Hint: This step will require the mean function.
print(df.isnull().mean() * 100)
#Default null ebitda values to 0.
df['ebitda'] = df['ebitda'].fillna(0)
#Check that there are no null ebitda values using the sum function.
print(df['ebitda'].isnull().sum())
#Drop null records.
df = df.dropna()
#Validate all nulls have been dropped by calculating the sum of values that are null.
print(df.isnull().sum())
#Remove duplicate rows.
df = df.drop_duplicates()
#Now that nulls and duplicates have been wrangled, clean up the data a little more by removing the $ currency symbols
#from the price field. Then, use the astype function to cast price to a float.
df['price'] = df['price'].str.replace("$", "")
df['price'] = df['price'].astype('float')
print(df.dtypes)
# %%
# # Import libraries and dependencies
# Set the path
path = Path('loans.csv')
# Read in the CSV as a DataFrame
df = pd.read_csv(path)
# %%
#Retrive rows with index 0 up to 10 (not including)
df.iloc[0:10]
# %%
# Describe summary statistics for csv data
df.describe()
# %%
# Filter the DataFrame down to the following, keep all rows
#loan_amnt, term, int_rate, emp_title, annual_inc, purpose
filtered_df = df.filter(items=['loan_amnt', 'term', 'int_rate', 'emp_title', 'annual_inc', 'purpose'])
# %%
# Conditional indexing to filter DataFrame where 'term' is equal to '36 months'
filtered_df.loc[filtered_df['term'] == '36 months']
# %%
# Change row values within the 'term' column from '36 months' to '3 Years'
filtered_df.loc[filtered_df['term'] == '36 months', 'term'] = '3 Years'

# %%
# Change row values within the 'emp_title' column from NaN to 'Unknown'
filtered_df.loc[filtered_df['emp_title'].isnull(), 'emp_title'] = 'Unknown'
filtered_df.head()
# %%
# Describe summary statistics for three-year loans
filtered_df.loc[filtered_df['term'] == '3 Years'].describe()
# %%
# Calculate unique values and counts for employee titles of 3 year customer loans
print(filtered_df.loc[filtered_df['term'] == '3 Years']['emp_title'].value_counts())
# %%
# Calculate unique values and counts for loan purposes of 3 year customer loans
print(filtered_df.loc[filtered_df['term'] == '3 Years']['purpose'].value_counts())
# %%
# Display summary statistics where annual income is greater than $80,000 to find count and mean
filtered_df.loc[(filtered_df['term'] == '3 Years') & (filtered_df['annual_inc'] > 80000)].describe()
# %%
# Display summary statistics where annual income is less than $80,000 to find count and mean
filtered_df.loc[(filtered_df['term'] == '3 Years') & (filtered_df['annual_inc'] < 80000)].describe()
# %%
# Import libraries and dependencies
from matplotlib import pyplot as plt
# %%
# Set the path
path = Path('sp500_companies.csv')
# Read in the CSV as a DataFrame
df = pd.read_csv(path)
# %%
# Count the frequency of each sector from the list of companies
print(df['Sector'].value_counts())
# %%
# Plot a pie chart from the distribution of company sectors
plt.pie(df['Sector'].value_counts())
# %%
# Grab the `Symbol` and `Market Cap` columns
filtered_df = df.filter(items=['Symbol', 'Market Cap'])
# Set the 'Symbol' as the index
# Drop the extra 'Symbol' column
filtered_df.set_index('Symbol', drop=True, inplace=True)
# Filter down to 20 companies with the largest market caps
filtered_df.sort_values('Market Cap', ascending=False, inplace=True)
filtered_df = filtered_df.head(20)
# Display the DataFrame
print(filtered_df)
# %%
# Plot a bar chart of the top 20 market cap companies
plt.figure(figsize=(15, 5))
plt.title('Top 20 Market Cap Companies')
plt.ylim(top=9e11)
plt.bar(filtered_df.index, filtered_df['Market Cap'])
# %%
# Plot a scatter plot to display the relationship between price vs. earnings/share
plt.scatter(df['Earnings/Share'],df['Price'])
# %%
