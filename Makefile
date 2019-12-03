init:
	. venv/bin/activate
	python -m pip install -r requirements.txt

run:
	python main.py

test:
	python -m pytest 