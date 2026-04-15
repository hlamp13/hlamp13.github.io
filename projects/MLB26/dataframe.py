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

#Merging the dataframes on the "Name" column.
merged = df1.merge(df2, on = "Name", how = "left")
merged_2 = merged.merge(df3, on = "Name", how = "left")
merged_final = merged_2.merge(df4, on = "Name", how = "left")
#Exporting the merged dataframe to CSV.
merged_final.to_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_final.csv", index=False, encoding="utf-8-sig")


#Merging existing dataframe with more career batting stats on PlayerID.
df5 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_final.csv", encoding="utf-8-sig")
df6 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\careerbatting.csv", encoding="latin1")
merged_playerid = df5.merge(df6, on = "playerID", how = "left")
#Exporting again to CSV.
merged_playerid.to_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_final_2.csv", index=False, encoding="utf-8-sig")

#Merging the existing dataframe with more career pitching stats on PlayerID.
df7 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_final_2.csv", encoding="utf-8-sig")
df8 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\careerpitching.csv", encoding="latin1")
merged_playerid_2 = df7.merge(df8, on = "playerID", how = "left")
#Exporting again to CSV.
merged_playerid_2.to_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_final_3.csv", index=False, encoding="utf-8-sig")

#Final corrections to the merged dataframe, mostly filling missing values.
df9 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\playerid.csv", encoding="utf-8-sig")
merged_playerid_3 = df9.merge(df6, on = "playerID", how = "left")
merged_playerid_3.to_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_missing_values.csv", index=False, encoding="utf-8-sig")

df10 = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_missing_values.csv", encoding="utf-8-sig")
merged_missing_pitch = df10.merge(df8, on = "playerID", how = "left")
merged_missing_pitch.to_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_merged_missing_values_pitch.csv", index=False, encoding="utf-8-sig")

position = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\careerposition.csv", encoding="latin1")
final = pd.read_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\full_mlb_stats.csv", encoding="utf-8-sig")
mlb_with_position = final.merge(position, on = "playerID", how = "left")
mlb_with_position.to_csv("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\full_mlb_stats_with_position.csv", index=False, encoding="utf-8-sig")