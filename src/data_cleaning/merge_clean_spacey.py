import pandas as pd

files = [
    '../data/video_transcripts_mix_clean_0_5000.csv', 
    '../data/video_transcripts_mix_clean_5000_10000.csv',
    '../data/video_transcripts_mix_clean_10000_15000.csv',
    '../data/video_transcripts_mix_clean_15000_20000.csv',
    '../data/video_transcripts_mix_clean_20000_25000.csv',
    '../data/video_transcripts_mix_clean_25000_30000.csv',
    '../data/video_transcripts_mix_clean_30000_35000.csv',
    '../data/video_transcripts_mix_clean_35000_40000.csv']

dfs = []

for file in files:
    dfs.append(pd.read_csv(file))

merged = pd.concat(dfs)

merged.to_csv('../data/video_transcripts_mix_clean.csv', index=False)