#Maintaining the chat history
# #from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()


model=ChatGroq(
     model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

chat_history=[(
    SystemMessage(content="You are a Helful AI Assistant")

)]

while True:
    user_input=input("You:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    result= model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)
