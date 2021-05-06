# %%
import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt
# %%
# Read in csv
csv_path = Path("class_data.csv")
aapl_df = pd.read_csv(csv_path)
aapl_df.head()
# %%
# Set `Date` as index
aapl_df.set_index('Date', drop=True, inplace=True)
aapl_df.head()
# %%
# Check for nulls
filtered_aapl_df = aapl_df.loc[aapl_df['Close'].isnull()]
filtered_aapl_df.head()
# %%
# Drop missing values

# %%
# Validate no more missing values

# %%
# Calculate daily returns
aapl_df['Differences'] = aapl_df['Close'].diff()
aapl_df.head()
# %%
# Sort data by `Close` in descending order
aapl_df.sort_values('Close', ascending=False, inplace=True)
aapl_df.head()
# %%
# Slice out top 5
filtered_aapl_df = aapl_df.head(5)
# %%
# Plot top 5 performing days
plt.figure(figsize=(15, 5))
plt.plot(filtered_aapl_df.index, filtered_aapl_df['Close'])
# %%
# Alternatively, visualizing the returns as a bar chart:
plt.figure(figsize=(15, 5))
plt.bar(filtered_aapl_df.index, filtered_aapl_df['Close'])
# %%
# Read in CSV file
csv_path = Path("crypto_data.csv")
crypto_data = pd.read_csv(csv_path, index_col='data_date', parse_dates=True, infer_datetime_format=True)
crypto_data.head()
# %%
# Drop extraneous columns
crypto_data = crypto_data.drop(columns=['data_time','timestamp'])
crypto_data = crypto_data.dropna()
crypto_data.head()
# %%
# Group data by cryptocurrency and plot on the same chart
crypto_data.groupby('cryptocurrency')['data_priceUsd'].plot(legend=True)
# %%
# Calculate average price across two years for each cryptocurrency
grouped_mean = crypto_data.groupby('cryptocurrency').mean()
print(grouped_mean)
# %%
# Calculate max price across two years for each cryptocurrency
grouped_max = crypto_data.groupby('cryptocurrency').max()
print(grouped_max)
# %%
# Calculate min price across two years for each cryptocurrency
grouped_min = crypto_data.groupby('cryptocurrency').min()
print(grouped_min)
# %%
# What does the data say about crypto performance in the past two years? Should you get back in the game?
# %%
from datetime import datetime, date, timedelta
# %%
# Read csv data
csv_path = Path("google_finance.csv")
goog_df = pd.read_csv(
   csv_path, parse_dates=True, index_col="Date", infer_datetime_format=True
)
goog_df.head()
# %%
# Check for nulls
goog_df.isnull().mean() * 100

# Drop nulls
goog_df = goog_df.dropna()

# Drop duplicates
goog_df = goog_df.drop_duplicates()

# Validate no more missing values
goog_df.isnull().sum()
# %%
# Group by year and month
grouped_goog = goog_df.groupby([goog_df.index.year, goog_df.index.month]).last()
# %%
# Access Close for May 2019 Using Multi-Indexing Lookup
grouped_goog.loc[2019,5]
# %%
grouped_goog = goog_df.groupby([goog_df.index.year]).mean()
grouped_goog.loc[2019]
# %%
# Read in data
fin_leaders_america_path = Path('fin_leaders_america.csv')
investors_leadership_path = Path('invstrs_leadership.csv')
fin_leaders_mem_path = Path('fin_leaders_members.csv')
investors_leadership_mem_path = Path('invstrs_leadership_members.csv')

fin_leaders_america_df = pd.read_csv(fin_leaders_america_path, index_col="MemberName")
investors_leadership_df = pd.read_csv(investors_leadership_path, index_col='MemberName')
fin_leaders_mem_df = pd.read_csv(fin_leaders_mem_path, index_col='MemberName')
investors_leadership_mem_df = pd.read_csv(investors_leadership_mem_path, index_col='MemberName')
# %%
# Concat dues data using rows axis and inner join
#joined_rows = pd.merge([fin_leaders_america_df,investors_leadership_df])
joined_rows = fin_leaders_america_df.merge(investors_leadership_df, on=['MemberName','DuesOwed','DuesPaid'])
print(joined_rows)
# %%
# Concat member data using rows axis and inner join
joined_columns = pd.concat([fin_leaders_mem_df,investors_leadership_mem_df], axis = 'columns', join = 'inner')
print(joined_columns)
# %%
# Concat dues and member data using columns axis and inner join
all_joined = pd.concat([joined_columns, joined_rows], axis = 'columns', join = 'inner')
print(all_joined)
# %%
%