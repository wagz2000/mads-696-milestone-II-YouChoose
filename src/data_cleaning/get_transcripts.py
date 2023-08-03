from youtube_transcript_api import YouTubeTranscriptApi as ytt
import pandas as pd
import sys
import numpy as np
from multiprocessing import Pool, cpu_count


def get_transcript(video_id):
    sys.stdout.write('.')
    is_generated = np.nan
    raw_transcript = None
    try:
        transcripts = ytt.list_transcripts(video_id)
        transcripts = transcripts.find_transcript(['en'])
        is_generated = transcripts.is_generated
        raw_transcript = transcripts.fetch()

    except:
        print(f"{video_id} has no transcript")
    
    return video_id, is_generated, raw_transcript

def get_transcripts(df, id_col):
    
    ret_transcripts = df[id_col].apply(get_transcript)
    print(ret_transcripts)
    ret_df = pd.DataFrame(ret_transcripts.tolist(), columns=[id_col, 'Is_Generated', 'Transcripts_Raw_Json'])
    # Join df with ret_df
    #df = pd.concat([df, ret_df], axis=1)
    df = df.merge( ret_df, on=id_col, how='left')

    
    return df

def get_transcripts_parallel(input_file, id_col):
    df = pd.read_csv(input_file)

    #df = df.head(100)

    num_cores = cpu_count()
    print( num_cores )

    df_split = np.array_split(df, num_cores)

    with Pool(num_cores) as pool:
        df = pd.concat(pool.starmap( get_transcripts, [(d, id_col) for d in df_split]))

        
    return df



if __name__ == '__main__': 
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='file with list of video ids' )
    parser.add_argument('video_id_column', help='name of column with video ids')
    parser.add_argument('output_file', help='name of file to write transcripts data')
    
    args = parser.parse_args()

    # video_transcripts = get_transcripts(args.input_file, args.video_id_column)
    video_transcripts = get_transcripts_parallel(args.input_file, args.video_id_column)

    video_transcripts.to_csv(args.output_file, index=False)






