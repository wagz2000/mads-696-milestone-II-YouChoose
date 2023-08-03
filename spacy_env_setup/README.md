this will set up a python environment specific for running spacy scripts since it is a pain and conflicts with local enviroments

please run from within the containing folder "spacy_env_setup"

to run, execute the bash script: create_spacy_env.sh

./create_spacy_env.sh


run on windows: 

powershell -ExecutionPolicy Bypass -File .\create_spacy_env.ps1


navigate to the new env:

    cd ../spacy_env


activate the env:

 ./Scripts/activate


run the data cleaning script 

python transcripts_deeper_cleaner.py ../data/dislike_video_transcripts_blob.csv "title;tags;description;Transcript_Blob" 0 5  ../data/video_transcripts_deep_clean_spacey_sample.csv


transcripts_deeper_cleaner.py == the name of the script to run

data file to clean == dislike_video_transcripts_blob.csv

list of columns to clean separated by semicolons == "title;tags;description;Transcript_Blob"

start row == 0

end row == 5

name of output file == video_transcripts_deep_clean_spacey_sample.csv
