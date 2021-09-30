# Install dependencies:

python -m pip install -r requirements.txt

for i in {1..10}; do ./vai.sh; done

# How to create and initialize a virtual environment

https://docs.python.org/3/library/venv.html
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/

python -m venv env

para ativar:

env\scripts\activate

para desativar:

env\scripts\deactivate
