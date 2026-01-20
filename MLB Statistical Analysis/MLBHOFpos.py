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

