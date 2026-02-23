from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

chat_template=ChatPromptTemplate([
    'system',"you are a helpful {Domain} Expert"
    'human', "Explain a simple terms the {Topic}"
])

prompt=chat_template.invoke({"Domain":"Cricker","Topic":"Bolling"})

print(prompt)