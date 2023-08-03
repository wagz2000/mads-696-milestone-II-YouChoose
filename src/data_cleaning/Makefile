data/video_transcripts.csv: get_transcripts.py data/videos-stats.csv
	python get_transcripts.py data/videos-stats.csv "Video ID" data/video_transcripts.csv

data/video_transcripts_blob.csv: transcripts_blob.py data/video_transcripts.csv
	python transcripts_blob.py data/video_transcripts.csv data/video_transcripts_blob.csv

data/video_transcripts_clean.csv: transcripts_cleaner.py data/video_transcripts_blob.csv
	python transcripts_cleaner.py data/video_transcripts_blob.csv "Transcript_Blob;Title" data/video_transcripts_clean.csv


data/dislike_video_transcripts.csv: get_transcripts.py data/videos-stats.csv
	python get_transcripts.py data/videos-stats.csv video_id data/dislike_video_transcripts.csv

data/dislike_video_transcripts_blob.csv: transcripts_blob.py data/dislike_video_transcripts.csv
	python transcripts_blob.py data/dislike_video_transcripts.csv data/dislike_video_transcripts_blob.csv

data/video_transcripts_clean.csv: transcripts_cleaner.py data/dislike_video_transcripts_blob.csv
	python transcripts_cleaner.py data/dislike_video_transcripts_blob.csv "title;tags;description;Transcript_Blob" data/video_transcripts_clean.csv


data/video_transcripts_deep_clean.csv: transcripts_deeper_cleaner.py data/dislike_video_transcripts_blob.csv
	python transcripts_deeper_cleaner.py data/dislike_video_transcripts_blob.csv "title;tags;description;Transcript_Blob" data/video_transcripts_deep_clean.csv