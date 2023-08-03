import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from nltk.corpus import stopwords
import json
import string
import re

#moving to here because the vscode crashes and stops displaying outputs
#with large features

def load_data(file):
    df = pd.read_csv(file)

    return df

def print_to_file(list, file):
    with open(file, 'w') as file:
        for item in list:
            file.write(str(item) + '\n')


if __name__ == '__main__' : 
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='file with list of video ids' )
    parser.add_argument('col', help='column to ' )
    args = parser.parse_args()

    df = load_data(args.input_file)
    col = args.col

    video_ts_df = df[df[col].notna()]
    video_no_ts_df = df[df[col].isna()]

    vectorizer = TfidfVectorizer(
        lowercase=True,
        max_features=1000,
        max_df=.85,
        min_df=5,
        ngram_range=(1,3)
    )

    print("begin training")
    ts_vectors = vectorizer.fit_transform(video_ts_df[col])
    print("training complete")
    feature_names = vectorizer.get_feature_names_out()

    dense = ts_vectors.todense()

    denselist = dense.tolist()

    all_keywords = []

    for transcript in denselist:
        x = 0
        keywords = []
        for word in transcript:
            if word > 0:
                keywords.append(feature_names[x])
            x = x+1
        all_keywords.append(keywords)

    print(len(all_keywords))
    print_to_file(all_keywords, f'data/all_{col}_keywords.txt')

    model = KMeans(n_clusters=1000, init='k-means++', max_iter=100, n_init=1)
    model.fit(ts_vectors)

    order_centroids = model.cluster_centers_.argsort()[:,::-1]
    terms = vectorizer.get_feature_names_out()

    with open (f'data/{col}_clusters.txt', 'w') as file:
        for i in range(1000):
            file.write(f"Cluster {i}\n")
            for j in order_centroids[i, :20]:
                file.write( " %s\n" % terms[j],)
            file.write('\n\n')