PYTHON = python3

all:run

run:
	$(PYTHON) -m pip install -r requirements.txt

clean:
	rm -f Parsing\ text\ from\ PDF.txt Parsing\ text\ from\ audio\ file.txt Parsing\ text\ from\ video\ file.txt

.PHONY: run clean
