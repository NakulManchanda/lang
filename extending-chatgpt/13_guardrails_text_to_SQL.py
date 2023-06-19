import logging
import os
from dotenv import load_dotenv
load_dotenv()

_LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
OPENAI_API_KEY=os.environ["OPENAI_API_KEY"]

# SQL Schema
SQL_SCHEMA = os.environ["SQL_SCHEMA"]
SQL_EXAMPLES = os.environ["SQL_EXAMPLES"]
SQL_CONN_STRING = os.environ["SQL_CONN_STRING"]


# pip install guardrails-ai
import json
from rich import print
from guardrails.applications.text2sql import Text2Sql

examples = []
with open(SQL_EXAMPLES, "r") as f:
    examples = json.load(f)

# RAIL Specification
app = Text2Sql(
    SQL_CONN_STRING,
    schema_file=SQL_SCHEMA,
    examples=examples,
)


print(app("List all the departments where name starts with 'S'"))



