import logging
import os
from dotenv import load_dotenv
load_dotenv()

_LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
OPENAI_API_KEY=os.environ["OPENAI_API_KEY"]
SERPAPI_API_KEY=os.environ["SERPAPI_API_KEY"]

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain


# load document
from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("popular/sample.pdf")
documents = loader.load()

chain = load_qa_chain(llm=OpenAI(), chain_type="map_reduce")

# take user input python in while loop
while True:
    query = input("Ask me a question: ")
    print(chain.run(input_documents=documents, question=query))