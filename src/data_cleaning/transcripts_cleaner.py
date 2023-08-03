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

def clean_data(input_file, cols):
    stop_words = set(stopwords.words('english'))
    df = pd.read_csv(input_file)
    stemmer = PorterStemmer()

    for col in cols:
        df[f"{col}_Clean"] = df[col].apply(cleaner, args=(stop_words, stemmer))

    return df


if __name__ == '__main__': 
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='file with list of video ids' )
    parser.add_argument('columns_to_clean', help='semicolon <;> separtated list of columns to perform the cleaning on')
    parser.add_argument('output_file', help='name of file to write transcripts data')
    
    args = parser.parse_args()

    cols = args.columns_to_clean.split(';')

    video_transcripts = clean_data(args.input_file, cols)

    video_transcripts.to_csv(args.output_file, index=False)






