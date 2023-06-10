# Query OpenAI with Context

Based on the [How to Add Context to OpenAI GPT with LlamaIndex](https://medium.com/cyberark-engineering/how-to-add-context-to-openai-gpt-with-llama-index-1c33c6a44055) article.

Start by creating the `.env` file with the following content.
```
OPENAI_API_KEY=<openai_api_key>
```

Run `make` without arguments to see all the available options.
```
$ make
Usage: make <config | run | clean | get URL=url | getall URL=url>
```

Run the `make config` command to install all the dependencies.

Download any context information into the `data` directory.
Optionally, use `make get` or `make getall` to download one document or use
recursion to get all the references on the first level.
```
URL=https://en.wikipedia.org/wiki/War
make get URL=${URL}
```

Run the `make run` command to query the ChatGPT engine about the context information.
Enter an empty query to exit.
```
$ make run
488K    ./data
Using the OPENAI_API_KEY environment variable...
Adding data to GPT...

Query: what's up?

The context information is discussing the concept of war, including its causes,
effects, and cultural and rationalist perspectives.

Query:
Exiting...
```

Finally, tun the `make clean` command to clean up all the temporary files and directories.
