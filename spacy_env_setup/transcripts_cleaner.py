import pandas as pd
import numpy as np
import string
import nltk
import re

# run this if first time
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.corpus import stopwords

import spacy
from gensim.utils import simple_preprocess
import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel
from tqdm import tqdm
import time
from concurrent.futures import ThreadPoolExecutor


sum_ = 0

def cleaner(text, stop_words, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    start_time = time.time()
    if pd.isnull(text):
        return None

    try:
        nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
        doc = nlp(text)
        new_text = new_text = [token.lemma_ 
            for token in doc if token.pos_ in allowed_postags 
            and token.lemma_ not in stop_words]
        lemmas = ' '.join(new_text)
        cleaned = simple_preprocess(lemmas, deacc=True)

        return cleaned

    except Exception as e:
        print( e )
    
    return None

def apply_cleaner(row, col, stop_words, pbar):
    cleaned = cleaner(row[col], stop_words, ['NOUN', 'ADJ', 'VERB', 'ADV'])
    pbar.update(1)
    return cleaned


def clean_data(input_file, cols, start_i, end_i):
    stop_words = set(stopwords.words('english'))
    more_stop_words = {'oh', 'yeah', 'im', 'ive', '♪', 'www', 'com', 'https', 'https' }
    stop_words = stop_words | more_stop_words 
    df = pd.read_csv(input_file)

    if end_i > df.shape[0]:
        end_i = df.shape[0] - 1
    df = df.iloc[start_i:end_i]

    for col in cols:
        print(col)
        with tqdm(total=len(df)) as pbar:
            df[f"{col}_Clean"] = df.apply(lambda row: apply_cleaner(row, col, stop_words, pbar ), axis=1)

    return df


if __name__ == '__main__': 
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='file with list of video ids' )
    parser.add_argument('columns_to_clean', help='semicolon <;> separtated list of columns to perform the cleaning on')
    parser.add_argument('start', help='start index')
    parser.add_argument('end', help='stop index')
    parser.add_argument('output_file', help='name of file to write transcripts data')
    
    args = parser.parse_args()

    cols = args.columns_to_clean.split(';')
    video_transcripts = clean_data(args.input_file, cols, int(args.start), int(args.end))
    video_transcripts.to_csv(f'{args.output_file}_{args.start}_{args.end}.csv', index=False)






