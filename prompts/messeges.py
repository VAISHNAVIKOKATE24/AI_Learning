from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage , AIMessage
import os
#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

load_dotenv()

model=ChatGroq(
     model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

messages=[
    SystemMessage(content="Hello U are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain")
]

result = model.invoke(messages)
AIMessage(content=result.content)
messages.append(AIMessage(content=result.content))

print(messages)