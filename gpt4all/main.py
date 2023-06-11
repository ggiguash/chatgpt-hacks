from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

local_path = './models/gpt4all-converted.bin' 
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

template = """
Query: {query}

"""

prompt = PromptTemplate(template=template, input_variables=["query"])
llm = GPT4All(model=local_path, callback_manager=callback_manager, verbose=True)
llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=False)

while True:
    query = input("\nQuery: ")
    if query == "":
        print("Exiting...")
        break
    llm_chain.run(query)
