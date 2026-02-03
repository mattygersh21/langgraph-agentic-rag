from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello Advanced RAG")
    pprint(app.invoke(input={"question": "what is agent memory?"}))