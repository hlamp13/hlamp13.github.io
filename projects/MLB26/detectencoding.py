import pandas as pd
import numpy as np
import pip
import chardet

with open("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_all_war.csv", "rb") as f:
    result = chardet.detect(f.read())
    print("all_war: ", result)

with open("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_hof_batters.csv", "rb") as f:
    result = chardet.detect(f.read())
    print("hof_batters: ", result)

with open("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_hof_pitchers.csv", "rb") as f:
    result = chardet.detect(f.read())
    print("hof_pitchers: ", result)

with open("C:\\Users\\hlamp\\OneDrive\\IndependentResearch\\hlamp13.github.io\\projects\\MLB26\\mlb_tot_hof.csv", "rb") as f:
    result = chardet.detect(f.read())
    print("tot_hof: ", result)

# all_war:  {'encoding': 'iso8859-16', 'confidence': 0.011144443809739354, 'language': 'pl', 'mime_type': 'text/plain'}
# hof_pitchers:  {'encoding': 'iso8859-3', 'confidence': 0.005101429149549982, 'language': 'eo', 'mime_type': 'text/plain'}
# hof_pitchers:  {'encoding': 'iso8859-3', 'confidence': 0.005101429149549982, 'language': 'eo', 'mime_type': 'text/plain'}
# tot_hof:  {'encoding': 'MacRoman', 'confidence': 0.010303553199317004, 'language': 'ms', 'mime_type': 'text/plain'}