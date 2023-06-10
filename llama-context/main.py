import os
import openai
from dotenv import load_dotenv
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

def build_storage(data_dir):
    documents = SimpleDirectoryReader(data_dir).load_data()

    index = GPTVectorStoreIndex.from_documents(documents)
    index.storage_context.persist()
    return index

def read_from_storage(persist_dir):
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    return load_index_from_storage(storage_context)

def adding_data_to_GPT():
    print("Adding data to GPT...")
 
    persist_dir = "./storage"
    data_dir = "./data"
    index = None

    if os.path.exists(persist_dir):
        index = read_from_storage(persist_dir)
    else:
        index = build_storage(data_dir)
    return index.as_query_engine()

def set_openai_api_key():
    load_dotenv()
    api_key = os.environ.get ("OPENAI_API_KEY")
    if api_key is None:
        print('Error: The OPENAI_API_KEY environment variable is not set')
        exit
    print('Using the OPENAI_API_KEY environment variable...')
    openai.api_key = api_key

def run_query_loop():
    query_engine = adding_data_to_GPT()
    while True:
        query = input("\nQuery: ")
        if query == "":
            print("Exiting...")
            break
        response = query_engine.query(query)
        print(response)

if __name__ == "__main__":
    set_openai_api_key()
    run_query_loop()
