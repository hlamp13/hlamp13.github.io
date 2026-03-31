import pandas as pd
import numpy as np
import pip
import re

#all_war
df1 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_all_war.csv", encoding="latin1")

#batters
df2 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_hof_batters.csv", encoding="latin1")

#pitchers
df3 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_hof_pitchers.csv", encoding="latin1")

#tot_hof
df4 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_tot_hof.csv", encoding="latin1")

merged = df1.merge(df2, on = "Name", how = "left")

merged_2 = merged.merge(df3, on = "Name", how = "left")
merged_final = merged_2.merge(df4, on = "Name", how = "left")

merged_final.to_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_final.csv", index=False, encoding="utf-8-sig")

merged_final["clean name"] = merged_final["Name"].str.strip()

merged_final["first"] = merged_final["clean name"].str.split(" ").str[0]
merged_final["last"] = merged_final["clean name"].str.split(" ").str[-1]

merged_final["first"] = merged_final["first"].str.replace(r"[^a-zA-Z]", "", regex=True).str.lower()
merged_final["last"] = merged_final["last"].str.replace(r"[^a-zA-Z]", "", regex=True).str.lower()

merged_final["playerID"] = (
    merged_final["last"].str[:5].str.ljust(5, "x") +
    merged_final["first"].str[:2].str.ljust(2, "x") +
    "01"
)

merged_final.to_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_final_1.csv", index=False, encoding="utf-8-sig")
df5 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_final_1.csv", encoding="utf-8-sig")
df6 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\careerbatting.csv", encoding="latin1")

merged_playerid = df5.merge(df6, on = "playerID", how = "left")

merged_playerid.to_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_final_2.csv", index=False, encoding="utf-8-sig")

df7 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_final_2.csv", encoding="utf-8-sig")
df8 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\careerpitching.csv", encoding="latin1")
merged_playerid_2 = df7.merge(df8, on = "playerID", how = "left")
merged_playerid_2.to_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_final_3.csv", index=False, encoding="utf-8-sig")

df9 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\playerid.csv", encoding="utf-8-sig")

merged_playerid_3 = df9.merge(df6, on = "playerID", how = "left")

merged_playerid_3.to_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_missing_values.csv", index=False, encoding="utf-8-sig")
