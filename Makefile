init:
	pipenv install

run:
	pipenv run python main.py

test:
	pipenv run python -m unittest discover -s tests