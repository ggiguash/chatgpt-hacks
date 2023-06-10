all:
	@echo "Usage: make <config | run | clean | download URL=url>"

config:
	./configure.sh
	@mkdir -p ./data

download:
	@rm -rf data storage
	wget -l1 -nd -e robots=off -P ./data/ "$(URL)"

run:
	@./venv/bin/python main.py

clean:
	@rm -rf venv data storage
