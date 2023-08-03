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

def cleaner(text, stop_words, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):

    if pd.isnull(text):
        return None

    try:
        nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
        doc = nlp(text)
        new_text = new_text = [token.lemma_ 
            for token in doc if token.pos_ in allowed_postags]
        lemmas = ' '.join(new_text)
        cleaned = simple_preprocess(lemmas, deacc=True)

    except Exception as e:
        print( e )
    
    return None

def clean_transcripts(input_file, cols):
    stop_words = set(stopwords.words('english'))
    more_stop_words = {'oh', 'yeah', 'im', 'ive', '♪' }
    stop_words = stop_words | more_stop_words 
    df = pd.read_csv(input_file)
    for col in cols:
        df[f"{col}_DeepClean"] = df[col].apply(cleaner, args=(stop_words))

    return df


if __name__ == '__main__': 
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='file with list of video ids' )
    parser.add_argument('columns_to_clean', help='semicolon <;> separtated list of columns to perform the cleaning on')
    parser.add_argument('output_file', help='name of file to write transcripts data')
    
    args = parser.parse_args()

    cols = args.columns_to_clean.split(';')
    video_transcripts = clean_transcripts(args.input_file, cols)

    video_transcripts.to_csv(args.output_file, index=False)






