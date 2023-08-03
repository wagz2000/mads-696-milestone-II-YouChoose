from youtube_transcript_api import YouTubeTranscriptApi as ytt
import pandas as pd
import sys
import json
import ast
import numpy as np

def raw_to_blob(transcript_raw):
    blob = ""

    if transcript_raw == np.nan or transcript_raw == None:
        return None

    try:
        transcript_dict = ast.literal_eval(transcript_raw)
        for line in transcript_dict:
            blob += f" {line['text']}"
        
        return blob

    except Exception as e:
        print( e )
    
    return None

def get_transcripts(input_file):
    df = pd.read_csv(input_file)
    df['Transcript_Blob'] = df['Transcripts_Raw_Json'].apply(raw_to_blob)

    df = df.drop('Transcripts_Raw_Json', axis=1)

    return df
        


if __name__ == '__main__': 
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='file with list of video ids' )
    parser.add_argument('output_file', help='name of file to write transcripts data')
    
    args = parser.parse_args()

    video_transcripts = get_transcripts(args.input_file)

    video_transcripts.to_csv(args.output_file, index=False)






