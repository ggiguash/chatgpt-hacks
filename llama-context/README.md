# Query OpenAI with Context

Based on the [How to Add Context to OpenAI GPT with LlamaIndex](https://medium.com/cyberark-engineering/how-to-add-context-to-openai-gpt-with-llama-index-1c33c6a44055) article.

Start by creating the `.env` file with the following content.
```
OPENAI_API_KEY=<openai_api_key>
```

Run the `make config` command to install all the dependencies.

Download any context information into the `data` directory. For example, use `wget`
to pull contents from a web site recursively.
```
URL=https://www.bbc.com/news/world-europe-65860294
wget -l1 -nd -e robots=off -P ./data/ "${URL}"
```

Run the `make run` command to query the ChatGPT engine about the context information.
```
$ make run
Using the OPENAI_API_KEY environment variable...
Adding data to GPT...

Query: what's up?

Ukraine is preparing to launch a counter-offensive against Russian forces in the region. The offensive is expected to last no more than five months and will involve punching through Russian lines to the Sea of Azov. If successful, any Russian troops west of the breach will be vulnerable and dependent on supply lines through the Crimean Peninsula. Ukraine is operating under a number of significant restraints, the main one being the lack of fighter jets capable of providing support from the air.

Query: 
Exiting...
```

Finally, tun the `make clean` command to clean up all the temporary files and directories.
