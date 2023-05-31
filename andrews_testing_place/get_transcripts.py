from youtube_transcript_api import YouTubeTranscriptApi as ytt
import pandas as pd
import sys


def get_transcript(video_id):
    sys.stdout.write('.')
    try:
        transcripts = ytt.list_transcripts(video_id)
        transcripts = transcripts.find_transcript(['en'])
        is_generated = transcripts.is_generated
        raw_transcript = str(transcripts.fetch())
        return is_generated, raw_transcript

    except:
        print(f"{video_id} has no transcript")
    
    return None, None

def get_transcripts(input_file):
    df = pd.read_csv(input_file)
    df['Is_Generated'], df['Transcripts_Raw_Json'] = zip(*df['Video ID'].apply(get_transcript))
            

    
    return df
        




if __name__ == '__main__': 
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='file with list of video ids' )
    parser.add_argument('output_file', help='name of file to write transcripts data')
    
    args = parser.parse_args()

    video_transcripts = get_transcripts(args.input_file)

    video_transcripts.to_csv(args.output_file, index=False)






