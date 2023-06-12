# ChatGPT Hacks

## Project Index
* [GPT LLama Index](./gpt-llama): Inspired by
[How to Add Context to OpenAI GPT with LlamaIndex](https://medium.com/cyberark-engineering/how-to-add-context-to-openai-gpt-with-llama-1c33c6a44055).

* [GPT4All LangChain](./gpt4all-langchain): Inspired by
[GPT4All is the Local ChatGPT for Your Documents](https://artificialcorner.com/gpt4all-is-the-local-chatgpt-for-your-documents-and-it-is-free-df1016bc335)

## Prerequisites
Change the current directory into one of the sub-projects and use the `make`
command to execute the necessary steps.

Run `make` without arguments to see all the available options.
```
$ make
Usage: make <config | run | clean | get URL=url | getall URL=url>
```

Run the `make config` command to install all the dependencies.

Download your context information into the `data` directory.

> Optionally, use `make get` or `make getall` to download one document or use
> recursion to get all the references on the first level.
> ```
> URL=https://en.wikipedia.org/wiki/War
> make get URL=${URL}
> ```

### Project-Specific Prerequisites
The [GPT LLama Index](./gpt-llama/) code uses OpenAI ChatGPT API, which requires
a key for connecting to the server. Create the `gpt-llama/.env` file containing
your OpenAI API Key.
```
OPENAI_API_KEY=<your_openai_api_key>
```

## Usage
Run the `make run` command to start a question-response loop with the LLM engine.
Ask questions, including queries about your context information.
> Enter an empty query to exit the loop.

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

## Cleanup
Run the `make clean` command to clean up all the temporary files and directories.
