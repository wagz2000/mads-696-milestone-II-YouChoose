
$envName = "..\spacy_env"

python -m venv $envName

Copy-Item -Path *.py -Destination "$envName\"

. "$envName\Scripts\activate.ps1"

pip install -U pip setuptools wheel
pip install spacy
pip install pandas
pip install nltk
pip install gensim

python -m spacy download en_core_web_sm

