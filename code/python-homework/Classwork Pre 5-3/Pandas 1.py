# %%
# Import libraries and dependencies
import pandas as pd
from pathlib import Path
import seaborn as sns
from matplotlib import pyplot as plt
# %%
# Set file paths
hd_data = Path("HD.csv")
jnj_data = Path("JNJ.csv")
intc_data = Path("INTC.csv")
amd_data = Path("AMD.csv")
mu_data = Path("MU.csv")
nvda_data = Path("NVDA.csv")
tsm_data = Path("TSM.csv")

# Read the individual CSV datasets
hd = pd.read_csv(hd_data, index_col="date")
jnj = pd.read_csv(jnj_data, index_col="date")
intc = pd.read_csv(intc_data, index_col="date")
amd = pd.read_csv(amd_data, index_col="date")
mu = pd.read_csv(mu_data, index_col="date")
nvda = pd.read_csv(nvda_data, index_col="date")
tsm = pd.read_csv(tsm_data, index_col="date")

intc.head()
# %%
# Use the `concat` function to combine the DataFrames by matching indexes (or in this case `date`)

# %%
# Use the `pct_change` function to calculate daily returns for each stock

# %%
# Use the `corr` function to calculate correlations for each stock pair

# %%
# Create a heatmap from the correlation values

# %%
# Create a heatmap from the correlation values and adjust the scale

# %%
#Which semiconductor stock would be the best candidate to add to the existing portfolio?

# %%
# Import libraries and dependencies
import numpy as np 
import pandas as pd 
from pathlib import Path 
from matplotlib import pyplot as plt
# %%
