from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# See https://github.com/nomic-ai/gpt4all/blob/main/gpt4all-chat/metadata/models.json
# for a full list of GPT4All models
local_path = './models/ggml-gpt4all-j-v1.3-groovy.bin'
callbacks = [StreamingStdOutCallbackHandler()]

template = """
Query: {query}

"""

prompt = PromptTemplate(template=template, input_variables=["query"])
llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True)
llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=False)

while True:
    query = input("\nQuery: ")
    if query == "":
        print("Exiting...")
        break
    llm_chain.run(query)
