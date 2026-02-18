import pandas as pd
import numpy as np
import pip

df1 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_all_war.csv", encoding="latin1")

df2 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_hof_batters.csv", encoding="latin1")

df3 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_hof_pitchers.csv", encoding="latin1")

df4 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_tot_hof.csv", encoding="latin1")

merged = df1.merge(df2, on = "Name", how = "left")
merged_2 = merged.merge(df3, on = "Name", how = "left")
merged_final = merged_2.merge(df4, on = "Name", how = "left")

print(merged_final.head())

merged_final.to_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_final.csv", index=False)
