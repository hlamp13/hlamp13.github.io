# hlamp13.github.io
Independent research portfolio.


## MLB Hall of Fame position player analysis
### First need to sort through raw data.
### Filter out pitchers in the position player data.
### Filter out players who were "not deserving" of Hall of Fame election.
### Need to find consistant terms of Hall of Fame election.
### Looking to analyze player stats on how long it takes for them to get to the HOF.
import pandas as pd
import numpy as np
import pip
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "statsmodels"])
import statsmodels.api as sm

df = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\MLB Statistical Analysis\\MLBHOFpos.csv", encoding="latin1")

print(df.head())

X = df[['ASG', 'WAR/pos', 'HR', 'OPS']]
Y = df['Years to HOF']
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
print(model.summary())
