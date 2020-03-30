Sera-weatherbot

Train Rasa Core
******************
python -m rasa_core.train -d domain.yml -s data/stories.md -o models/dialogue -c policy.yml

Train Rasa Core Interactively
**************************************
python -m rasa_core.train interactive -o models/dialogue -d domain.yml -c policy.yml -s data/stories.md --nlu models/c


Various Steps to Train and Run Rasa NLU and Core
Install miniconda/anaconda

https://docs.conda.io/en/latest/miniconda.html

Check conda version

conda --version
Conda Update

conda update conda
Create Virtual Env

conda create -n botenv python=3.6
Activate Virtual Env

conda activate botenv
Initial commands to install Rasa NLU to Virtual Env i.e. botenv

pip install rasa_nlu
To Update existing one

pip install -U rasa_nlu
For dependencies spaCy+sklearn

pip install rasa_nlu[spacy]
python3 -m spacy download en
python3 -m spacy download en_core_web_md
python3 -m spacy link en_core_web_md en
Tensorflow pip install rasa_nlu[tensorflow]

Train Rasa NLU

python3 -m rasa_nlu.train -c nlu_config.yml --data data/nlu.md -o models --fixed_model_name nlu --project current --verbose
Run Rasa NLU

python3 -m rasa_nlu.server --path ./models
Initial commands to install Rasa Core & SDK

pip install rasa_core
pip install rasa_core_sdk
To Update existing one

pip install -U rasa_core
Train Rasa Core

python3 -m rasa_core.train -d domain.yml -s data/stories.md -o models/dialogue -c policy.yml
Train Rasa Core Interactively

python3 -m rasa_core.train interactive -o models/dialogue -d domain.yml -c policy.yml -s data/stories.md --nlu models/current/nlu
Run Rasa Core

python3 -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml
Debug Rasa Core

python3 -m rasa_core.run -d models/dialogue -u models/current/nlu --debug
Python Train and Run NLU

python3 nlu_model.py
Train and Run CORE

python3 dialogue_model.py
To run the custom action

python3 -m rasa_core_sdk.endpoint --actions actions
