all:
	@echo "Usage: make <config | run | clean>"

config:
	./configure.sh
	@mkdir -p ./data

run:
	@./venv/bin/python main.py

clean:
	@rm -rf venv data storage
