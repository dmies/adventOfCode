init:
	. venv/bin/activate

run:
	python main.py

test:
	python -m unittest discover -s tests