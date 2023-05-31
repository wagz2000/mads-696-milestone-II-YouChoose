import pandas as pd
import numpy as np
import string
import nltk

# run this if first time
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def cleaner(text, stop_words, stemmer):

    if pd.isnull(text):
        return None

    try:
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokenized = word_tokenize(text)
        tokenized = [stemmer.stem(token) for token in tokenized if token not in stop_words]

        return ' '.join(tokenized)
    except Exception as e:
        print( e )
    
    return None

def clean_transcripts(input_file):
    stop_words = set(stopwords.words('english'))
    df = pd.read_csv(input_file)
    stemmer = PorterStemmer()
    df['Transcript_Clean'] = df['Transcript_Blob'].apply(cleaner, args=(stop_words, stemmer))
    df['Title_Clean'] = df['Title'].apply(cleaner, args=(stop_words, stemmer))


    return df


if __name__ == '__main__': 
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='file with list of video ids' )
    parser.add_argument('output_file', help='name of file to write transcripts data')
    
    args = parser.parse_args()

    video_transcripts = clean_transcripts(args.input_file)

    video_transcripts.to_csv(args.output_file, index=False)






