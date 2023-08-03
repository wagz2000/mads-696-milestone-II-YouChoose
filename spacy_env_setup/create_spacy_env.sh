
env_name="../spacy_env"

python -m venv "$env_name"

source "$env_name/bin/activate"

pip install -r spacy_requirements.txt

python -m spacy download en_core_web_sm

mv *.py "$env_name/bin/"