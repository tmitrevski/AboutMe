# %%
# Import libraries and dependencies
import numpy as np
import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt
import os

print(os.getcwd())
# %%
# Set the file paths
bk_data = Path("./Resources/bk_data.csv")
fang_data = Path("./Resources/fang_data.csv")
jnj_data = Path("./Resources/jnj_data.csv")
luv_data = Path("./Resources/luv_data.csv")
mu_data = Path("./Resources/mu_data.csv")
nke_data = Path("./Resources/nke_data.csv")
sbux_data = Path("./Resources/sbux_data.csv")
t_data = Path("./Resources/t_data.csv")
wdc_data = Path("./Resources/wdc_data.csv")
wrk_data = Path("./Resources/wrk_data.csv")

# Read the CSVs and set the `date` column as a datetime index to the DataFrame
bk_df = pd.read_csv(bk_data, index_col="date", infer_datetime_format=True, parse_dates=True)
fang_df = pd.read_csv(fang_data, index_col="date", infer_datetime_format=True, parse_dates=True)
jnj_df = pd.read_csv(jnj_data, index_col="date", infer_datetime_format=True, parse_dates=True)
luv_df = pd.read_csv(luv_data, index_col="date", infer_datetime_format=True, parse_dates=True)
mu_df = pd.read_csv(mu_data, index_col="date", infer_datetime_format=True, parse_dates=True)
nke_df = pd.read_csv(nke_data, index_col="date", infer_datetime_format=True, parse_dates=True)
sbux_df = pd.read_csv(sbux_data, index_col="date", infer_datetime_format=True, parse_dates=True)
t_df = pd.read_csv(t_data, index_col="date", infer_datetime_format=True, parse_dates=True)
wdc_df = pd.read_csv(wdc_data, index_col="date", infer_datetime_format=True, parse_dates=True)
wrk_df = pd.read_csv(wrk_data, index_col="date", infer_datetime_format=True, parse_dates=True)

# Display a few rows
wrk_df.head()
# %%
# Create a new pivot table where the columns are the closing prices for each ticker
bk_df['Ticker'] = "BK"
fang_df['Ticker'] = "FANG"
jnj_df['Ticker'] = "JNJ"
luv_df['Ticker'] = "LUV"
mu_df['Ticker'] = "MU"
nke_df['Ticker'] = "NKE"
sbux_df['Ticker'] = "SBUX"
t_df['Ticker'] = "T"
wdc_df['Ticker'] = "WDC"
wrk_df['Ticker'] = "WRK"
all_df = pd.concat([bk_df, fang_df, jnj_df, luv_df, mu_df, nke_df, sbux_df, t_df, wdc_df, wrk_df], axis = 'rows', join = 'inner')
all_df.head()
# %%
all_pt = all_df.pivot_table(values = 'close', index = 'date', columns = 'Ticker')
all_pt.sort_index(ascending = True)
all_pt.head()

# %%
# Use the `pct_change` function to calculate daily returns
all_returns = all_pt.pct_change()
all_returns.head()
# %%
# Use the `std` function and multiply by the square root of the number of trading days in a year to get annualized volatility
volatility = all_returns.std() * np.sqrt(252)
print(volatility)
# %%
# Drop the five stocks with the highest volatility in daily returns
all_returns.drop(labels=['MU','WDC','WRK','FANG','JNJ'], axis=1, inplace=True)
all_returns.head()
# %%
# Set weights for corresponding risk profile of stocks, use the `dot` function to multiply each weight by the corresponding stock daily return
# BK, LUV, NKE, SBUX, T
weights = [0.5, 0.2, 0.15, 0.10, 0.05]
p_returns = all_returns.dot(weights)
p_returns.head()
# %%
# Use the `cumprod` function to calculate cumulative returns
cum_ret = (1 + p_returns).cumprod()
# %%
# Plot the returns of the portfolio in terms of money
investment = 10000
(investment * cum_ret).plot()

# %%