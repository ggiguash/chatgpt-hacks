WGET_OPTS:=-l1 -nd -e robots=off

all:
	@echo "Usage: make <config | run | clean | get URL=url | getall URL=url>"

config:
	./configure.sh
	@mkdir -p ./data

get:
	@rm -rf data storage
	@wget $(WGET_OPTS) -P ./data/ "$(URL)"

getall:
	@rm -rf data storage
	@wget $(WGET_OPTS) -r -P ./data/ "$(URL)"

run:
	find ./data -type f -exec file {} \; | grep -v " text" | awk -F: '{print $$1}' | xargs -n1 rm -f
	@du -sh ./data
	@./venv/bin/python main.py

clean:
	@rm -rf venv data storage
