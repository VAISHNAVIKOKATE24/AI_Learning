# --------- Load ENV first ----------
from dotenv import load_dotenv
import os
load_dotenv()

# --------- Imports ----------
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

# --------- State ----------
class chatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# --------- LLM ----------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0
)

# --------- Node ----------
def chat_node(state: chatState):
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response]}

# --------- Graph ----------
checkpointer = MemorySaver()

graph = StateGraph(chatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)
